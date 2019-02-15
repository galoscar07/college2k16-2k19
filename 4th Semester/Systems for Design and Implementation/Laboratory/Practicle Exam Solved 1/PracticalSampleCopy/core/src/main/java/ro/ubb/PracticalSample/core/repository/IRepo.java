package ro.ubb.PracticalSample.core.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.NoRepositoryBean;
import org.springframework.transaction.annotation.Transactional;

import java.io.Serializable;

@NoRepositoryBean
@Transactional
public interface IRepo<T, ID extends Serializable>
    extends JpaRepository<T, ID> {
}
