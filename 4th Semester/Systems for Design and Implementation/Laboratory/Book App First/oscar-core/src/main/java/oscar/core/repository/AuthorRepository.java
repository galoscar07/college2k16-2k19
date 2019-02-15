package oscar.core.repository;

import org.springframework.data.jpa.repository.EntityGraph;
import org.springframework.data.jpa.repository.Query;
import oscar.core.model.Author;

import java.util.List;

public interface AuthorRepository extends Repository<Author, Long> {
    @Query("select distinct a from Author a")
    @EntityGraph(value = "authorWithBooks", type = EntityGraph.EntityGraphType.LOAD)
    List<Author> findAllWithBooks();
}
