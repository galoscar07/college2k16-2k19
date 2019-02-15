//
//  Repository.c
//  Tourism Agency L03-04
//
//  Created by Gal Oscar on 07/03/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#include "Repository.h"
#include "Entities.h"
#include <string.h>
#include <strings.h>
#include <assert.h>
#include <stdlib.h>


OfferRepository* createRepo(){
    OfferRepository* of = (OfferRepository*)malloc(sizeof(OfferRepository));
    of->dynamic = createDynamicArray(1);
    return of;
}

void destroyRepo(OfferRepository* of){
    if (of == NULL)
        return;
    for (int i = 0; i< getLengthDynamic(of->dynamic); i++){
        Offer* o = get(of->dynamic, i);
        destroyOffer(o);
    }
    destroyDynamicArray(of->dynamic);
}

int findDestDepartureRepo(OfferRepository of,char *destination, calendar departureDate){
    int i;
    for (i = 0; i < getLengthDynamic(of.dynamic); i++){
        Offer* o = get(of.dynamic, i);
        if ((strcmp(o->destination, destination) == 0) && (o->departureDate.day = departureDate.day) && (o->departureDate.month = departureDate.month) && (o->departureDate.year = departureDate.year))
            return i;
    }
    return -1;
}

int addRepo(OfferRepository* of, Offer* o){
    if (findDestDepartureRepo(*of, o->destination, o->departureDate) != -1)
        return 0;
    Offer* copy = copyOffer(o);
    addDynamic(of->dynamic, copy);
    return 1;
}

int getLengthRepo(OfferRepository* of){
    if (of->dynamic == NULL)
        return -1;
    return getLengthDynamic(of->dynamic);
}

Offer* getOfferOnPositionRepo(OfferRepository* of, int position){
    calendar nullCalendar; nullCalendar.day = 0; nullCalendar.month = 0; nullCalendar.year = 0;
    if (position < 0 || position >= getLengthDynamic(of->dynamic))
        return createOffer("", "", nullCalendar, 0);
    return get(of->dynamic, position);
}

int delRepo(OfferRepository* of, Offer* o){
    int something = findDestDepartureRepo(*of, o->destination, o->departureDate);
    if (something == -1)
        return 0;
    Offer* some = get(of->dynamic, something);
    destroyOffer(some);
    deleteDynamic(of->dynamic, something);
    return 1;
}

int updateRepo(OfferRepository *of, Offer* o){
    int something = findDestDepartureRepo(*of, o->destination, o->departureDate);
    if (something == -1)
        return 0;
    else{
        if (getType(o)[0] != '-')
            strcpy(of->dynamic->elems[something]->type, o->type);
        if (o->price != 0)
            of->dynamic->elems[something]->price = o->price;
        return 1;
    }
}

void testAllRepository(){
    OfferRepository *repo = createRepo();
    calendar Calendar; Calendar.day = 20; Calendar.month = 11; Calendar.year = 2018;
    Offer* o = createOffer("Mountain", "Everest", Calendar, 1000);
    assert(getLengthRepo(repo) == 0);
    addRepo(repo, o);
    assert(getLengthRepo(repo) == 1);
    calendar Calendar1; Calendar1.day = 15; Calendar1.month = 10; Calendar1.year = 2017;
    Offer* o1 = createOffer("Break", "Hong Kong", Calendar1, 700);
    addRepo(repo, o1);
    assert(getLengthRepo(repo) == 2);
    assert(getLengthDynamic(repo->dynamic) == 2);
    
    assert(delRepo(repo, o) == 1);
    assert(getLengthRepo(repo) == 1);
    assert(delRepo(repo, o) == 0);
    assert(getLengthRepo(repo) == 1);
    
    Calendar1.day = 15; Calendar1.month = 10; Calendar1.year = 2017;
    o1 = createOffer("Breakasda", "Hong Kong", Calendar1, 7000);
    assert(updateRepo(repo,o1) == 1);
    Calendar1.day = 1005; Calendar1.month = 90; Calendar1.year = 2019;
    o1 = createOffer("Breakasda", "Ho Ko", Calendar1, 7000);
    assert(updateRepo(repo,o1) == 0);
    
}
