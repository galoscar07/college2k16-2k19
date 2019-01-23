package oscar.web.converter;

import org.springframework.stereotype.Component;
import oscar.core.model.Book;
import oscar.web.dto.BookDto;

@Component
public class BookConverter extends AbstractConverterBaseEntityConverter<Book, BookDto> {
    @Override
    public Book convertDtoToModel(BookDto bookDto) {
        Book b = new Book();
        b.setTitle(bookDto.getTitle());
        b.setYear(bookDto.getYear());
        b.setId(bookDto.getId());
        return b;
    }

    @Override
    public BookDto convertModelToDto(Book book) {
        BookDto bookDto = BookDto.builder()
                .title(book.getTitle())
                .author(book.getAuthor().getName())
                .year(book.getYear())
                .build();
        bookDto.setId(book.getId());
        return bookDto;
    }
}
