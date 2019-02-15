package ro.ubb.bookstore.core.repository;

import ro.ubb.bookstore.core.model.Author;

public interface AuthorRepository extends Repository<Author, Long>, AuthorRepositoryJPQL {
}
