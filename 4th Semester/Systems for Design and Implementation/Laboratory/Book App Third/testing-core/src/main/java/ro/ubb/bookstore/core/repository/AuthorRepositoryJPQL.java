package ro.ubb.bookstore.core.repository;

import ro.ubb.bookstore.core.model.Author;

import java.util.List;

public interface AuthorRepositoryJPQL {
    List<Author> findAllWithPurchasesAndBooksJPQL();
}
