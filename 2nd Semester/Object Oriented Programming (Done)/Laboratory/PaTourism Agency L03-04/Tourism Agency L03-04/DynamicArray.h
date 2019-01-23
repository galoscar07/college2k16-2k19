//
//  DynamicArray.h
//  Tourism Agency L03-04
//
//  Created by Gal Oscar on 02/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#pragma once
#include <stdio.h>
#include "Entities.h"
#define CAPACITY 10
typedef Offer* Element;

typedef struct
{
    Element* elems;
    int length;
    int capacity;
} DynamicArray;

DynamicArray* createDynamicArray(int capacity);
    /*
     The function will create a dynamic array of generic elements, with a given capacity
     Input: capacity which represents an integer, maximum capacity for the dynamic array
     Output: The function will return a pointer to the created dynamic array
    */

void destroyDynamicArray(DynamicArray* dArray);
    /*
     The function will free the memory and distroy the dynamic array
     Input: dArray which represents a dynamic array to be deleted
    */

void addDynamic(DynamicArray* dArray, Element t);
    /*
     The function will add a generic element to the dynamic array
     Input: dArray which is a dynamic array type and is also the array in which we will add the element, and t which type Element which actualy is an offer.
    */

void deleteDynamic(DynamicArray* dArray, int pos);
    /*
     The function will delete an element from the dynamic array on a specific position
     Input: dArray which is a dynamic array type and is also the array from which we will delete an element and pos which is an int and represent the position of the element that we want to delete
    */

int getLengthDynamic(DynamicArray* arr);
    /*
     The function will return the length of a dynamic array.
     Input: dArray which is type DynamicArray and represent the array from which we will get the length
    */

Element get(DynamicArray* arr, int pos);
    /*
     The function will return the element on a given position
     Input:dArray which is type DynamicArray and represent the array from which we will get the element and pos which is an int representing the position of the element that we want to return
     Output: The function will return an Element that is on a given position
    */

void testAllDynamic();
    /*
     The function is a test function and it will handle some cases in adding deleteing items out ot the vector array
    */
    
