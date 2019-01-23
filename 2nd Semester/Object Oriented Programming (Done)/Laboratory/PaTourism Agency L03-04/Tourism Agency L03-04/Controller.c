//
//  Controller.c
//  Tourism Agency L03-04
//
//  Created by Gal Oscar on 07/03/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Controller.h"
#include <string.h>
#include <stdlib.h>

OfferController createController(OfferRepository* of){
    OfferController cont;
    cont.repo = of;
    cont.after = createDynamicArray(2);
    cont.before = createDynamicArray(2);
    cont.undoIndex = -1;
    return cont;
}

void destroyController(OfferController* cont){
    for (int i = 0; i < getLengthDynamic(cont->after); i++){
        destroyOffer(cont->after->elems[i]);
    }
    for (int i = 0; i < getLengthDynamic(cont->before); i++){
        destroyOffer(cont->before->elems[i]);
    }
    destroyDynamicArray(cont->after);
    destroyDynamicArray(cont->before);
    destroyRepo(cont->repo);
    
}

OfferRepository* getRepository(OfferController* of){
    return of->repo;
}

int addOfferController(OfferController* of, char* type, char* destination, calendar departureDate, int price){
    Offer* o = createOffer(type, destination, departureDate, price);
    int something = addRepo(of->repo, o);
    if (something == 1)
        addOperationController(of, NULL, o);
    return something;
    
}

int deleteOfferController(OfferController* of, char destination[], calendar departureDate){
    Offer* o = createOffer("", destination, departureDate, 0);
    int pos = findDestDepartureRepo(*of->repo, destination, departureDate);
    
    Offer* o1 = getOfferOnPositionRepo(of->repo, pos);
    int something = delRepo(of ->repo, o);
    
    if (something == 1)
        addOperationController(of, o1, NULL);
    return something;
}

int updateOfferController(OfferController* of, char type[], char destination[], calendar departureDate, int price){
    int pos = findDestDepartureRepo(*of->repo, destination, departureDate);
    Offer* o1 = getOfferOnPositionRepo(of->repo, pos);
    
    Offer* o = createOffer(type, destination, departureDate, price);
    int something = updateRepo(of->repo, o);
    
    int pos2 = findDestDepartureRepo(*of->repo, destination, departureDate);
    Offer* o3 = getOfferOnPositionRepo(of->repo, pos2);
    
    if (something == 1)
        addOperationController(of, o1, o3);
    return something;
}

int checkDate(calendar date1, calendar date2){
    // 1 is date1 > date 2 , o otherwise
    if (date1.year > date2.year){
        return 1;
    }
    if (date1.month > date2.month){
        return 1;
    }
    if (date1.day > date2.day){
        return 1;
    }
    return 0;
}

OfferRepository* filterByDestinationCombinationController(OfferController* of, char destination[]){
    OfferRepository* something = createRepo();
    if (strcmp(destination, "null") == 0){
        for (int i=0; i< getLengthRepo(of->repo); i++){
            Offer *o = getOfferOnPositionRepo(of->repo, i);
            addRepo(something, o);
        }
    }
    else{
        for (int i=0; i< getLengthRepo(of->repo); i++){
            Offer *o = getOfferOnPositionRepo(of->repo, i);
            if (strstr(getDestination(o), destination) != NULL)
                addRepo(something, o);
        }
    }
    int sorted=0;
    while(!sorted){
        sorted=1;
        for (int i=0; i<getLengthRepo(something)-1; i++){
            if (something->dynamic->elems[i]->price < something->dynamic->elems[i+1]->price){
                sorted=0;
                Offer *aux = something->dynamic->elems[i];
                something->dynamic->elems[i] = something->dynamic->elems[i+1];
                something->dynamic->elems[i+1] = aux;
            }
        }
    }
    return something;
}

OfferRepository* filterByPriceController(OfferController* of, char *type, int pri){
    OfferRepository* something = createRepo();
    for (int i=0; i< getLengthRepo(of->repo); i++){
        Offer *o = getOfferOnPositionRepo(of->repo, i);
        if ((strstr(getType(o), type) != NULL) && (getPrice(o)<pri))
            addRepo(something,o);
        }
    int sorted=0;
    while(!sorted){
        sorted=1;
        for (int i=0; i<getLengthRepo(something)-1; i++){
            if (something->dynamic->elems[i]->price > something->dynamic->elems[i+1]->price){
                sorted=0;
                Offer *aux = something->dynamic->elems[i];
                something->dynamic->elems[i] = something->dynamic->elems[i+1];
                something->dynamic->elems[i+1] = aux;
            }
        }
    }
    return something;
}

OfferRepository* filterByPriceDateController(OfferController* of, char *type, calendar date){
    OfferRepository* something = createRepo();
    for (int i = 0; i < getLengthRepo(of -> repo); i++){
        Offer* o = getOfferOnPositionRepo(of->repo, i);
        if ((strstr(getType(o), type) != NULL) && (checkDate(o->departureDate, date) == 1) ){
            addRepo(something, o);
        }
    }
    return something;
}

OfferRepository* filterOfferWithTypeDestinationController(OfferController* of, char* type){
    
    OfferRepository* something = createRepo();
    for (int i = 0; i < getLengthRepo( of -> repo); i++){
        Offer* o = getOfferOnPositionRepo(of->repo, i);
        if (strstr(getType(o), type)){
            addRepo(something, o);
        }
    }
    int sorted=0;
    while(!sorted){
        sorted=1;
        for (int i=0; i<getLengthRepo(something)-1; i++){
            if (strcmp(something->dynamic->elems[i]->destination , something->dynamic->elems[i+1]->destination)>0){
                sorted=0;
                Offer *aux = something->dynamic->elems[i];
                something->dynamic->elems[i] = something->dynamic->elems[i+1];
                something->dynamic->elems[i+1] = aux;
            }
        }
    }
    return something;
}

void addOperationController(OfferController *cont, Offer* before, Offer* after) {
    while (cont->undoIndex < cont->after->length - 1)
    {
        destroyOffer(cont->after->elems[cont->after->length-1]);
        destroyOffer(cont->before->elems[cont->before->length - 1]);
        deleteDynamic(cont->after, cont->after->length - 1);
        deleteDynamic(cont->before, cont->before->length - 1);
    }
    addDynamic(cont->after, after);
    addDynamic(cont->before, before);
    cont->undoIndex ++;
}

int undoController(OfferController *cont){
    if (cont->undoIndex < 0)
        return 0;
    if(cont->after->elems[cont->undoIndex]!=NULL){
        Offer* o = createOffer("", cont->after->elems[cont->undoIndex]->destination, cont->after->elems[cont->undoIndex]->departureDate, 0);
        delRepo(cont->repo, o);
    }
    if(cont->before->elems[cont->undoIndex]!=NULL){
        Offer* o = createOffer(cont->after->elems[cont->undoIndex]->type , cont->after->elems[cont->undoIndex]->destination, cont->after->elems[cont->undoIndex]->departureDate, cont->after->elems[cont->undoIndex]->price);
        addRepo(cont->repo, o);
    }
    cont->undoIndex--;
    return 1;
}

int redoController(OfferController *cont){
    if (cont->undoIndex+1 == cont->after->length)
        return 0;
    if (cont->before->elems[cont->undoIndex+1] != NULL){
        Offer* o = createOffer("", cont->after->elems[cont->undoIndex+1]->destination, cont->after->elems[cont->undoIndex+1]->departureDate, 0);
        delRepo(cont->repo, o);
    }
    if (cont->after->elems[cont->undoIndex + 1] != NULL){
        Offer* o = createOffer(cont->after->elems[cont->undoIndex+1]->type , cont->after->elems[cont->undoIndex+1]->destination, cont->after->elems[cont->undoIndex+1]->departureDate, cont->after->elems[cont->undoIndex+1]->price);
        addRepo(cont->repo, o);
    }
    cont->undoIndex ++;
    return 1;
}


void startUp(OfferController* ctrl){
    calendar Calendar;
    Calendar.day = 1;
    Calendar.month = 1;
    Calendar.year = 2018;
    addOfferController(ctrl, "Mountain", "Everest", Calendar, 1000);
    
    Calendar.day = 10;
    Calendar.month = 2;
    Calendar.year = 2018;
    addOfferController(ctrl,"City", "Budapest", Calendar, 700);
    
    Calendar.day = 15;
    Calendar.month = 3;
    Calendar.year = 2018;
    addOfferController(ctrl,"Seaside", "Vama", Calendar, 400);
    
    Calendar.day = 20;
    Calendar.month = 4;
    Calendar.year = 2018;
    addOfferController(ctrl,"Mountain", "Bucegi", Calendar, 350);
    
    Calendar.day = 29;
    Calendar.month = 5;
    Calendar.year = 2018;
    addOfferController(ctrl,"Seaside", "Mamaia", Calendar, 1040);
    
    Calendar.day = 30;
    Calendar.month = 6;
    Calendar.year = 2018;
    addOfferController(ctrl,"City", "Bucharest", Calendar, 1500);
    
    Calendar.day = 5;
    Calendar.month = 7;
    Calendar.year = 2018;
    addOfferController(ctrl,"City", "Alba", Calendar, 20);
    
    Calendar.day = 18;
    Calendar.month = 8;
    Calendar.year = 2018;
    addOfferController(ctrl,"Seaside", "Creta", Calendar, 1000);
    
    Calendar.day = 27;
    Calendar.month = 9;
    Calendar.year = 2018;
    addOfferController(ctrl,"City", "Amsterdam", Calendar, 2000);
    
    Calendar.day = 20;
    Calendar.month = 10;
    Calendar.year = 2018;
    addOfferController(ctrl,"City", "London", Calendar, 3000);
    
    Calendar.day = 06;
    Calendar.month = 10;
    Calendar.year = 2019;
    addOfferController(ctrl,"City", "Alba", Calendar, 3000);
}


