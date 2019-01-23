package oscar.core.model;

import lombok.*;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

@NamedEntityGraphs({
        @NamedEntityGraph(name = "authorWithBooks",
                attributeNodes = @NamedAttributeNode(value = "books")),
})
@Entity
@NoArgsConstructor
@AllArgsConstructor
@Getter
@ToString(exclude = "books")
@Data
@Setter
@Builder
public class Author extends BaseEntity<Long> {
    @Column(name = "name", nullable = false)
    private String name;

    @OneToMany(mappedBy = "author", fetch = FetchType.LAZY)
    private Set<Book> books = new HashSet<>();

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Author that = (Author) o;

        return name.equals(that.name);
    }

    @Override
    public int hashCode() {
        return name.hashCode();
    }
}
