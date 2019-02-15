package ro.ubb.PracticalSample.core.service;

import ro.ubb.PracticalSample.core.model.Person;

import java.util.List;

public interface PersonService {
    List<Person> getAllByKeyword(String keyword);
}
