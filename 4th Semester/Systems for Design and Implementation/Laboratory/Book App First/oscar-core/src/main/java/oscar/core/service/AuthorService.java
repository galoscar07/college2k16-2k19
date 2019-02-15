package oscar.core.service;

import oscar.core.model.Author;

import java.util.List;
import java.util.Optional;

public interface AuthorService {
    List<Author> getAll();

    Optional<Author> findAuthor(Long id);

    Author addAuthor(Author author);
}
