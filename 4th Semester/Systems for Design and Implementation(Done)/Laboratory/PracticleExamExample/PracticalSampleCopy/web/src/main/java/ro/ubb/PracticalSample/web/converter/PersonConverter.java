package ro.ubb.PracticalSample.web.converter;

import org.springframework.stereotype.Component;
import ro.ubb.PracticalSample.core.model.Person;
import ro.ubb.PracticalSample.web.dto.PersonDto;

@Component
public class PersonConverter implements Converter<Person, PersonDto> {

    @Override
    public Person convertDtoToModel(PersonDto personDto) {
        Person person = new Person(personDto.getId(), personDto.getSsn(), personDto.getName());
        return person;
    }

    @Override
    public PersonDto convertModelToDto(Person person) {
        PersonDto personDto = new PersonDto(person.getId(), person.getSsn(), person.getName());
        return personDto;
    }
}
