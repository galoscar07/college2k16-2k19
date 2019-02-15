import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import {RouterModule} from "@angular/router";
import { AuthorsComponent } from './authors/authors.component';
import { BooksComponent } from './books/books.component';
import {BooksService} from "./books/books.service";
import {AuthorsService} from "./authors/authors.service";
import {HttpClientModule} from "@angular/common/http";
import {FormsModule} from "@angular/forms";


@NgModule({
  declarations: [
    AppComponent,
    AuthorsComponent,
    BooksComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot([
        {
          path: 'books',
          component: BooksComponent
        },
        {
          path: 'authors',
          component: BooksComponent
        }
    ]),
    HttpClientModule,
    FormsModule
  ],
  providers: [BooksService, AuthorsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
