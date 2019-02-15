package ro.ubb.bookstore.core.repository;


import org.springframework.data.jpa.repository.EntityGraph;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import ro.ubb.bookstore.core.model.Book;

import java.util.List;
import java.util.Optional;

public interface BookRepository extends Repository<Book, Long> {
    @Query("select distinct b from Book b")
    @EntityGraph(value = "bookWithPurchases", type = EntityGraph.EntityGraphType.LOAD)
    List<Book> findAllWithPurchases();

    @Query("select distinct b from Book b")
    @EntityGraph(value = "bookWithPurchasesAndClients", type = EntityGraph.EntityGraphType.LOAD)
    List<Book> findAllWithPurchasesAndClients();

    @Query("select b from Book b where b.id = :id")
    @EntityGraph(value = "bookWithPurchasesAndClients", type = EntityGraph.EntityGraphType.LOAD)
    Optional<Book> findOneWithPurchasesAndClients(@Param("id") Long id);
}
