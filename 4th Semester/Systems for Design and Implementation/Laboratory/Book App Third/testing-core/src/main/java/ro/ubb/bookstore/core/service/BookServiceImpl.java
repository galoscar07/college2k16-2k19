package ro.ubb.bookstore.core.service;

import org.springframework.beans.factory.annotation.Autowired;
import ro.ubb.bookstore.core.model.Book;
import ro.ubb.bookstore.core.repository.AuthorRepository;
import ro.ubb.bookstore.core.repository.BookRepository;

import java.util.List;
import java.util.Optional;

public class BookServiceImpl implements BookService {

    @Autowired
    private BookRepository bookRepository;

    @Autowired
    private AuthorRepository authorRepository;

    @Override
    public List<Book> getAll() {
        List<Book> result = bookRepository.findAllWithPurchasesAndClients();
        return result;
    }

    @Override
    public Optional<Book> findBook(Long id) {
        Optional<Book> book = bookRepository.findById(id);
        return book;
    }

    @Override
    public Book addBook(Book book) {
        bookRepository.save(book);
        return book;
    }
}
