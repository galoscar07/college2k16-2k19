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
public class Book {

    @Column(name = "title", nullable = false)
    private String title;

    @Column(name = "year", nullable = false)
    private String year;

    @OneToMany(mappedBy = "book", cascade = CascadeType.ALL, fetch = FetchType.LAZY, orphanRemoval = true)
    private Set<Author> authors = new HashSet<>();

    public Set<Author> getAuthor() {
        return this.authors.stream().
                map(Author::getAuthor).
                collect(Collectors.toSet());
    }

    @Override
    public int hashCode() {
        return title.hashCode();
    }

    public void addClients(Set<Author> clients) {
        clients.forEach(this::addAuthor);
    }
}
