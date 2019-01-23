package ro.ubb.PracticalSample.core.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Entity
@NoArgsConstructor
@AllArgsConstructor
@Data
public class Person {
    @Id
    @GeneratedValue
    private Long id;

    @Column(unique = true)
    private String ssn;

    private String name;
}
