package ro.ubb.bookstore.core.repository;

import lombok.Getter;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;

@Getter
public abstract class JPQLRepositorySupport {
    @PersistenceContext
    private EntityManager entityManager;
}
