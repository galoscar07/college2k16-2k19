import { Injectable } from '@angular/core';

import {Person} from './person';
import {PERSONS} from './mock-persons';

import {Observable} from 'rxjs/Observable';
import { of } from 'rxjs/observable/of';

import { HttpHeaders, HttpClient } from '@angular/common/http';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
}

@Injectable({
  providedIn: 'root'
})
export class PersonService {

  private personsUrl = 'http://localhost:8080/api/persons'

  constructor(private http: HttpClient) { }

  getPersons(keyword: string): Observable<Person[]>{
    const url = this.personsUrl + "/" + keyword;
    console.log(url);
    return this.http.get<Person[]>(url);
  }
}
