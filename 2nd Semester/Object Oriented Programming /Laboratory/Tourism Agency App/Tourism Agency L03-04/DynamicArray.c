//
//  DynamicArray.c
//  Tourism Agency L03-04
//
//  Created by Gal Oscar on 02/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#include "DynamicArray.h"
#include <stdlib.h>
#include <assert.h>

DynamicArray* createDynamicArray(int capacity){
    DynamicArray* yes = (DynamicArray*)malloc(sizeof(DynamicArray));
    if (yes == NULL)
        return NULL;
    yes->capacity = capacity;
    yes->length = 0;
    yes->elems = (Element*)malloc(capacity * sizeof(Element));
    if (yes->elems == NULL)
        return NULL;
    return yes;
}

void destroyDynamicArray(DynamicArray* dArray){
    if (dArray == NULL)
        return;
    if (dArray->elems == NULL)
        return;
    free(dArray->elems);
    dArray->elems = NULL;
    
    free(dArray);
    dArray = NULL;
}

void resize(DynamicArray* dArray){
    if (dArray == NULL)
        return;
    
    dArray->capacity *= 2;
    dArray->elems = (Element*)realloc(dArray->elems, dArray->capacity * sizeof(Element));
}

void addDynamic(DynamicArray* dArray, Element t){
    if (dArray == NULL)
        return;
    if (dArray->elems == NULL)
        return;
    if (dArray->length == dArray->capacity)
        resize(dArray);
    dArray->elems[dArray->length++] = t;
}

void deleteDynamic(DynamicArray* dArray, int pos){
    if (dArray == NULL)
        return;
    if (dArray->elems == NULL)
        return;
    for (int i = pos; i < dArray->length - 1; i++)
        dArray->elems[i] = dArray->elems[i + 1];
    dArray->length--;
}

int getLengthDynamic(DynamicArray* dArray){
    if (dArray == NULL)
        return -1;
    return dArray->length;
}

Element get(DynamicArray* dArray, int pos){
    return dArray->elems[pos];
}

void testAllDynamic(){
    DynamicArray* some = createDynamicArray(1);
    calendar Calendar;
    Calendar.day = 1;
    Calendar.month = 1;
    Calendar.year = 2018;
    Offer * offer = createOffer("Mountain", "Everest", Calendar, 1000);
    assert(some->length == 0);
    assert(some->capacity == 1);
    addDynamic(some, offer);
    assert(some->length == 1);
    assert(some->capacity == 1);
    addDynamic(some, offer);
    addDynamic(some, offer);
    assert(some->length == 3);
    assert(some->capacity == 4);
    assert(getLengthDynamic(some) == 3);
    deleteDynamic(some, 1);
    assert(some->length == 2);
    assert(some->capacity == 4);
    destroyDynamicArray(some);
}
