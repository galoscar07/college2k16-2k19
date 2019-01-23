package oscar.web.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import oscar.core.model.Author;
import oscar.core.service.AuthorService;
import oscar.web.converter.AuthorConverter;
import oscar.web.dto.AuthorDto;

import java.util.List;

@RestController
public class AuthorController {
    private static final Logger log = LoggerFactory.getLogger(AuthorController.class);

    @Autowired
    private AuthorService authorService;

    @Autowired
    private AuthorConverter authorConverter;

    @RequestMapping(value = "/authors", method = RequestMethod.GET)
    public Iterable getAll() {
        log.trace("getAll");
        List<Author> authors = authorService.getAll();
        log.trace("getAll: authors={}", authors);
        return authorConverter.convertModelsToDtos(authors);
    }

    @RequestMapping(value = "/authors", method = RequestMethod.POST)
    public AuthorDto createAuthor(@RequestBody final AuthorDto authorDto) {
        log.trace("createAuthor: authorDto={}", authorDto);
        Author author = authorService.addAuthor(authorConverter.convertDtoToModel(authorDto));
        AuthorDto result = authorConverter.convertModelToDto(author);
        log.trace("createAuthor: result={}", result);
        return result;
    }
}
