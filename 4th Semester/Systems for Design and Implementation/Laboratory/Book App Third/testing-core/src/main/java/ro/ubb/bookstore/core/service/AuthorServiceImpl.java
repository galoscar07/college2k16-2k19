package ro.ubb.bookstore.core.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ro.ubb.bookstore.core.model.Author;
import ro.ubb.bookstore.core.repository.AuthorRepository;
import ro.ubb.bookstore.core.repository.BookRepository;

import java.util.List;
import java.util.Optional;

@Service
public class AuthorServiceImpl implements AuthorService {

    @Autowired
    private AuthorRepository authorRepository;

    @Autowired
    private BookRepository bookRepository;

    @Override
    public List<Author> getAll() {
        List<Author> result = authorRepository.findAllWithPurchasesAndBooksJPQL();
        return result;
    }

    @Override
    public Optional<Author> findAuthor(Long id) {
        Optional<Author> author = authorRepository.findById(id);
        return author;
    }

    @Override
    public Author addAuthor(Author author) {
        authorRepository.save(author);
        return author;
    }
}