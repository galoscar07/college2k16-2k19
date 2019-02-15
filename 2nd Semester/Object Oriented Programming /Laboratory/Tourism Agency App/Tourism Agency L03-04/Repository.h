//
//  Repository.h
//  Tourism Agency L03-04
//
//  Created by Gal Oscar on 07/03/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#pragma once
#include "Entities.h"
#include "DynamicArray.h"

typedef struct{
    DynamicArray* dynamic;
}OfferRepository;

OfferRepository* createRepo();
    /*
     The function will create the offer Repository
     */

void destroyRepo(OfferRepository* of);
    /*
     The function will destroy a given offer repository
    */

int findDestDepartureRepo(OfferRepository of, char *destination, calendar daprtureDate);
    /*
     The function will search through the repository for an offer with the given destination and departure date.
     Input Data: of is a pointer to the OfferRepository*, destination and departure date are a string and respectively a calendar structure with which we will search for.
     Output: the function will return the position of the offer in the OfferRepository* or -1 if it doesn't exist in the repo.
     */

int addRepo(OfferRepository* of, Offer* o);
    /*
     The function will add into the repository of offers an offer.
     Input: of which is a pointer to the offer repository and o which is an offer.
     Output: 1 if the offer was added sucessfully and 0 if the offer wasn't added.
     */

int getLengthRepo(OfferRepository* of);
    /*
     The function will return the length of the offers repository
     Input: as input will be the of which is a pointer to the offer repository
     Output: an integer which represents the length of the offer repository
     */

Offer* getOfferOnPositionRepo(OfferRepository* of, int position);
    /*
     The function will return the offer that is on the given position
     Input: of which is a pointer to the OfferRepository** and position which is a position in the repository
     Output: The offer that is on the given position, or an "empty" offer.
     */

int delRepo(OfferRepository* of, Offer* o);
    /*
     The function will delete an offer from the repository. The offer must have the departureDate and destination the same as o
     Input: of which is a pointer to the OfferRepository* and o which is an offer but we care only about destination and departureDate fields
     Output: 1 if the offer was deleted from the repository and 0 otherwise.
    */

int updateRepo(OfferRepository* of, Offer* o);
    /*
     The function will update 2 fields of the offer structure, to be exact the type field and price.
     Input: of which is a pointer to the repository and o which is the structure from which we will update the structure in the repo
     Output: 1 if the update was managed and 0 otherwise
    */

void testAllRepository();
/*
 The function will have test for the repository.
 */



     
     
     
     
     
     
     
     
     
     
     
     
     
     
