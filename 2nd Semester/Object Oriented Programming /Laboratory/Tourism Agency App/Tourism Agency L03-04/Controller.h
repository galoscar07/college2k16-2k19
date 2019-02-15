//
//  Controller.h
//  Tourism Agency L03-04
//
//  Created by Gal Oscar on 07/03/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include "Repository.h"

typedef struct{
    
    OfferRepository* repo;
    DynamicArray* before;
    DynamicArray* after;
    int undoIndex;
    
}OfferController;

OfferController createController(OfferRepository* of);
    /*
     The function will create the controller
    */

int addOfferController(OfferController* of, char* type, char* destination, calendar departureDate, int price);
    /*
     The function will add an offer to the repository
     Input: of which is a pointer to the offerController, type which is a char, destination which is a char, departureDate which is a calendar structure and price which is an int
     Output: the function will return 1 if the offer was sucessfully added and 0 otherwise.
    */

OfferRepository* getRepository(OfferController* of);
    /*
     The function will return the repository
     Input: of which is a pointer to the controller
    */

int deleteOfferController(OfferController* of, char* destination, calendar departureDate);
/*
 The function will delete an offer from the repository
 Input: of which is a pointer to the controller, destination and departureDate which are the 2 keys with the help of whom we will search the structure that need to be deleted from the repo
 Outpu: the function will return 1 if the delete was sucessfull or 0 otherwise.
 */

int updateOfferController(OfferController* of, char* type, char* destination, calendar departureDate, int price);
/*
 The function will update a structure from the repository.
 Input: of which is a pointer to the controllerm destination, type, departureDate, price are the fields that will complete an offer structure
 Output: The function will return 1 if the update was done and 0 otherwise.
 */

OfferRepository* filterByDestinationCombinationController(OfferController* of, char* destination);
/*
 The function searched for the offers that contain a given symbol combination found in the variable destination
 Input: of which is a pointer to the controller, and destination is a string, if it is null we will return all offers
 Output: the function will return a list.
 */

OfferRepository* filterByPriceController(OfferController*of, char* price, int pri);

OfferRepository* filterByPriceDateController(OfferController* of, char *type, calendar date);

OfferRepository* filterOfferWithTypeDestinationController(OfferController* of, char* type);

void addOperationController(OfferController *cont, Offer* before, Offer* after);

int undoController(OfferController *of);

int redoController(OfferController* of);

void startUp(OfferController* ctrl);

void destroyController(OfferController* cont);

void testAllController();



