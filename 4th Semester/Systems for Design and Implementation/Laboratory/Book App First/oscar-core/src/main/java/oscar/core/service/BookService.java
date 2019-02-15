package oscar.core.service;

import oscar.core.model.Book;

import java.util.List;
import java.util.Optional;

public interface BookService {
    List<Book> getAll();

    Book addBook(Book book);
}