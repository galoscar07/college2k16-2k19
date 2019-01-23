import { Component, OnInit } from '@angular/core';
import { PersonService } from '../person.service'
import { Person } from '../person';

@Component({
  selector: 'app-persons',
  templateUrl: './persons.component.html',
  styleUrls: ['./persons.component.css']
})
export class PersonsComponent implements OnInit {

  persons: Person[] = [];

  constructor(private personService: PersonService) { }

  ngOnInit() {
  }

  loadAll(keyword: string): void{
    this.personService.getPersons(keyword)
      .subscribe(persons => this.persons = persons);
  }

}
