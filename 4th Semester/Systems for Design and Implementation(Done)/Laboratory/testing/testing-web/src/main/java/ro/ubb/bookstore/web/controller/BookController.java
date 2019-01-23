package ro.ubb.bookstore.web.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import ro.ubb.bookstore.core.model.Book;
import ro.ubb.bookstore.core.service.BookService;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

@RestController
public class BookController {

    private static final Logger log = LoggerFactory.getLogger(BookController.class);

    @Autowired
    private BookService bookService;

    @Autowired
    private BookConverter bookConverter;

    @RequestMapping(value = "/books", method = RequestMethod.GET)
    public Iterable getBooks() {
        log.trace("getBooks");
        List<Book> books = bookService.getAll();
        log.trace("getBooks: books={}", books);
        return bookConverter.convertModelsToDtos(books);
    }

    @RequestMapping(value = "/books/{bookId}", method = RequestMethod.GET)
    public BookDto getBook(@PathVariable final Long bookId) {
        log.trace("getBooks");
        Optional<Book> book = bookService.findBook(bookId);
        log.trace("getBook: book={}", book);
        return bookConverter.convertModelToDto(book.get());
    }

    @RequestMapping(value = "/books/{bookId}", method = RequestMethod.PUT)
    public BookDto updateBook(@PathVariable final Long bookId, @RequestBody final BookDto bookDto) {
        log.trace("updateBook: bookId={}, bookDtoMap={}", bookId, bookDto);
        Book book = bookConverter.convertDtoToModel(bookDto);
        book.setId(bookId);
        Optional<Book> bookOptional = bookService.updateBook(book);
        Map<String, BookDto> result = new HashMap<>();
        if (bookOptional.isPresent()) {
            result.put("book", bookConverter.convertModelToDto(bookOptional.get()));
        } else {
            result.put("book", bookConverter.convertModelToDto(new Book()));
        }
        log.trace("updateBook: result={}", result);
        return result.get("book");
    }

    @RequestMapping(value = "/books", method = RequestMethod.POST)
    public BookDto createBook(@RequestBody final BookDto bookDto) {
        log.trace("createBook: bookDtoMap={}", bookDto);
        Book book = bookService.addBook(bookConverter.convertDtoToModel(bookDto));
        BookDto result = bookConverter.convertModelToDto(book);
        log.trace("createBook: result={}", result);
        return result;
    }

    @RequestMapping(value = "books/{bookId}", method = RequestMethod.DELETE)
    public ResponseEntity deleteBook(@PathVariable final Long bookId) {
        log.trace("deleteBook: bookId={}", bookId);
        bookService.deleteBook(bookId);
        log.trace("deleteBook - method end");
        return new ResponseEntity(new EmptyJsonResponse(), HttpStatus.OK);
    }
}
