package ro.ubb.bookstore.core.model;

import lombok.*;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

@Entity
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@Data
@ToString
@Builder
public class Author {

    @Column(name = "title", nullable = false)
    private String title;

    @Column(name = "year", nullable = false)
    private String year;

    @OneToMany(mappedBy = "book", cascade = CascadeType.ALL, fetch = FetchType.LAZY, orphanRemoval = true)
    private Set<Book> books = new HashSet<>();


    public Set<Book> getBooks() {
        return this.books.stream().
                map(Book::getBook).
                collect(Collectors.toSet());
    }
}