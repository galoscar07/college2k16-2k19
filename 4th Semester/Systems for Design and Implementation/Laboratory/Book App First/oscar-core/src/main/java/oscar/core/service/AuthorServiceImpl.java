package oscar.core.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import oscar.core.model.Author;
import oscar.core.repository.AuthorRepository;

import java.util.List;
import java.util.Optional;

@Service
public class AuthorServiceImpl implements AuthorService {
    private static final Logger LOG = LoggerFactory.getLogger(AuthorServiceImpl.class);

    @Autowired
    private AuthorRepository authorRepository;

    @Override
    public List<Author> getAll() {
        LOG.trace("getAll --- method entered");

        List<Author> result = authorRepository.findAllWithBooks();

        LOG.trace("getAll: result={}", result);
        return result;
    }

    @Override
    public Optional<Author> findAuthor(Long id) {
        LOG.trace("findAuthor: id={}", id);
        Optional<Author> author = authorRepository.findById(id);
        LOG.trace("findBook: author={}", author);
        return author;
    }

    @Override
    public Author addAuthor(Author author) {
        LOG.trace("addAuthor: author={}", author);
        authorRepository.save(author);
        LOG.trace("addAuthor --- method finished");
        return author;
    }
}
