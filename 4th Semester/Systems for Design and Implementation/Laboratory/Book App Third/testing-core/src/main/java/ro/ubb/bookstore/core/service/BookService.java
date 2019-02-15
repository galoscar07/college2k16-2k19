package ro.ubb.bookstore.core.service;

import ro.ubb.bookstore.core.model.Book;

import java.util.List;
import java.util.Optional;

public interface BookService {
    List<Book> getAll();

    Optional<Book> findBook(Long id);

    Book addBook(Book book);
}