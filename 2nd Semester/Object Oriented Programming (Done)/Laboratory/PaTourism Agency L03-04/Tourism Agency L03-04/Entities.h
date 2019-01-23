//
//  Entities.h
//  Tourism Agency L03-04
//
//  Created by Gal Oscar on 07/03/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#pragma once

typedef struct{
    int day;
    int month;
    int year;
}calendar;
    /*
     The thing above will create a structure that has 3 fields (all of them are int values): day, month, year. The scructure will be called calendar
    */

typedef struct{
    char *type;
    char *destination;
    calendar departureDate;
    int price;
}Offer;
    /*
     The thing above will create a structure that will be called offer. The offer structure has 4 components: type which will be a char max 20 characters, destination also char with max 25 characters, departureDate which is an calendar and price which is an int.
    */



Offer *createOffer(char type[], char destination[], calendar departureDate, int price);
    /*
     The function will create an offer. As input data the functions has all the elements needed to create an offer structure.
     Output: The function will return an offer structure.
    */

void destroyOffer(Offer *o);
    /*
     The function will free the memory and destroys the given offer.
     Input: The function will recive an offer
    */

char* getType(Offer* o);
    /*
     The funtion will return the value which in this case is a char that is in the structure o on the field type
     Input: o which is a pointer to a structure Offer.
     Output: a value char
    */

char* getDestination(Offer* o);
    /*
     The funtion will return the value which in this case is a char that is in the structure o on the field destination
     Input: o which is a pointer to a structure Offer.
     Output: a value char
    */

calendar getDepartureDate(Offer* o);
    /* 
     The funtion will return the value which in this case is a structure claendar that is in the structure o on the field departureDate
     Input: o which is a pointer to a structure Offer.
     Output: a value that is a structure char
    */

int getPrice(Offer* o);
    /*
     The funtion will return the value which in this case is a int that is in the structure o on the field price
     Input: o which is a pointer to a structure Offer.
     Output: a value int
    */

void toString(Offer o, char str[]);
    /*
     This function will composes a string with the same text that would be printed if format was used on printf, but instead of being printed, the content is stored as a C string in the buffer pointed by str.
     Input: o which is a structure offer having 4 fields and str which is the string in which we will put a string
    */

Offer* copyOffer(Offer* o);

