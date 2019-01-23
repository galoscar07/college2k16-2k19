package ro.ubb.PracticalSample.web.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import ro.ubb.PracticalSample.core.model.Person;
import ro.ubb.PracticalSample.core.service.PersonService;
import ro.ubb.PracticalSample.web.converter.PersonConverter;
import ro.ubb.PracticalSample.web.dto.PersonDto;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

@RestController
public class PersonController {
    private static final Logger LOG = LoggerFactory.getLogger(PersonController.class);

    @Autowired
    private PersonService personService;

    @Autowired
    private PersonConverter personConverter;

    @RequestMapping(value = "/persons/{keyword}", method = RequestMethod.GET)
    public Set<PersonDto> getPersonsByKeyword(@PathVariable String keyword){
        LOG.trace("getPersonsByKeyword --- method entered");
        List<Person> persons = personService.getAllByKeyword(keyword);
        Set<PersonDto> result = new HashSet<>();
        for (Person p : persons)
            result.add(personConverter.convertModelToDto(p));

        LOG.trace("getPersonsByKeyword: result={}", result);
        return result;
    }
}
