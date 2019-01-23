package ro.ubb.bookstore.core.repository;

import ro.ubb.bookstore.core.model.Author;

import javax.persistence.EntityManager;
import javax.persistence.Query;
import java.util.List;

public class AuthorRepositoryImpl extends JPQLRepositorySupport implements AuthorRepositoryJPQL {
    @Override
    public List<Author> findAllWithPurchasesAndBooksJPQL() {
        EntityManager entityManager = getEntityManager();
        Query query = entityManager.createQuery("select distinct c from Author c " +
                "left join fetch c.purchases p " +
                "left join fetch p.book");

        return (List<Author>) query.getResultList();
    }

}
