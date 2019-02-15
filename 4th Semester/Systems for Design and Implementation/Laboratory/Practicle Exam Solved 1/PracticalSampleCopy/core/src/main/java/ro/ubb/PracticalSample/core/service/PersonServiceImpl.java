package ro.ubb.PracticalSample.core.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ro.ubb.PracticalSample.core.model.Person;
import ro.ubb.PracticalSample.core.repository.PersonJpaRepository;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class PersonServiceImpl implements PersonService {
    private static final Logger LOG = LoggerFactory.getLogger(PersonServiceImpl.class);

    @Autowired
    private PersonJpaRepository personRepository;

    @Override
    public List<Person> getAllByKeyword(String keyword) {

        LOG.trace("getAllByKeyword --- method entered");

        List<Person> persons = personRepository.findAll();

//        for (Person p : persons){
//            if (!p.getName().contains(keyword))
//                persons.remove(p);
//        }
        persons = persons.stream()
            .filter(p -> p.getName().contains(keyword))
            .collect(Collectors.toList());

        LOG.trace("getAllByKeyword: persons={}", persons);
        return persons;
    }


}
