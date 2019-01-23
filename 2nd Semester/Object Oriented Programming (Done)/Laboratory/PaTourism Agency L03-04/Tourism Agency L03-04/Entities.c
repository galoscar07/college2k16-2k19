//
//  Entities.c
//  Tourism Agency L03-04
//
//  Created by Gal Oscar on 07/03/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Entities.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

Offer *createOffer(char type[], char destination[], calendar departureDate, int price){
    Offer *o = (Offer *)malloc(sizeof(Offer));
    o->type = (char*)malloc(sizeof(char)*(strlen(type) + 1));
    o->destination = (char*)malloc(sizeof(char)*(strlen(destination) + 1));
    strcpy(o -> type, type);
    strcpy(o -> destination, destination);
    o -> departureDate = departureDate;
    o -> price = price;
    return o;
}

void destroyOffer(Offer* o){
    if (o == NULL)
        return;
    if (o->type == NULL)
        return;
    if (o->destination == NULL)
        return;
    free(o -> destination);
    free(o -> type);
    free(o);
    o->type = NULL;
    o->destination = NULL;
    o = NULL;
}

char* getType(Offer* o){
    return o->type;
}

char* getDestination(Offer* o){
    return o->destination;
}

calendar getDepartureDate(Offer* o){
    return o-> departureDate;
}

int getPrice(Offer* p){
    return p->price;
}

void toString(Offer o, char str[]){
    sprintf(str, "The offer has the type '%s', in the destination %s, with the departure date: %d/%d/%d and having the price %d.", o.type, o.destination, o.departureDate.day, o.departureDate.month, o.departureDate.year, o.price);
}

Offer* copyOffer(Offer* o){
    Offer* newOffer = createOffer(getType(o), getDestination(o), getDepartureDate(o), getPrice(o));
    return newOffer;
};
