package oscar.core.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import oscar.core.model.Author;
import oscar.core.model.Book;
import oscar.core.repository.AuthorRepository;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class BookServiceImpl implements BookService {
    private static final Logger LOG = LoggerFactory.getLogger(BookServiceImpl.class);

    @Autowired
    private AuthorRepository authorRepository;

    @Override
    @Transactional
    public List<Book> getAll() {
        LOG.trace("getAll --- method entered");

        List<Author> authors = authorRepository.findAllWithBooks();
        List<Book> books = new ArrayList<>();
        authors.forEach(a->books.addAll(a.getBooks()));

        LOG.trace("getAll: result={}", books);
        return books;
    }

    @Override
    @Transactional
    public Book addBook(Book book) {
        Author author = authorRepository.findById(book.getAuthor().getId()).get();
        author.getBooks().add(book);
        return book;
    }
}
