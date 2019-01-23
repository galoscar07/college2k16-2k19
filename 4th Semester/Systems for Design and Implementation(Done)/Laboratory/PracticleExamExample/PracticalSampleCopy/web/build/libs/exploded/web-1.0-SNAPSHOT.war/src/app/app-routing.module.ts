import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { PersonsComponent } from './persons/persons.component';

const routes: Routes = [
  { path: 'registry', component: PersonsComponent },
  { path: '', redirectTo: '/registry', pathMatch: 'full' }
]

@NgModule({
  exports: [ RouterModule ],
  imports: [ RouterModule.forRoot(routes) ]
})
export class AppRoutingModule { }
