package oscar.web.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import oscar.core.model.Book;
import oscar.core.service.BookService;
import oscar.web.converter.BookConverter;
import oscar.web.dto.BookDto;

import java.util.List;

@RestController
public class BookController {
    private static final Logger log = LoggerFactory.getLogger(BookController.class);

    @Autowired
    private BookService bookService;

    @Autowired
    private BookConverter bookConverter;

    @RequestMapping(value = "/books", method = RequestMethod.GET)
    public Iterable getAll() {
        log.trace("getAll");
        List<Book> books = bookService.getAll();
        log.trace("getAll: books={}", books);
        return bookConverter.convertModelsToDtos(books);
    }

    @RequestMapping(value = "/books", method = RequestMethod.POST)
    public BookDto createBook(@RequestBody final BookDto bookDto) {
        log.trace("createBook: bookDto={}", bookDto);
        Book book = bookService.addBook(bookConverter.convertDtoToModel(bookDto));
        BookDto result = bookConverter.convertModelToDto(book);
        log.trace("createBook: result={}", result);
        return result;
    }
}
