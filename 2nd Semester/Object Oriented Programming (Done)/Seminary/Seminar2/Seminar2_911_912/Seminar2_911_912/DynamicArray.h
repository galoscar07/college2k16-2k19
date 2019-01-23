#pragma once
#include "Planet.h"
#define CAPACITY 10

typedef Planet* TElement;

typedef struct
{
	TElement* elems;
	int length;			
	int capacity;		
}DynamicArray;

DynamicArray* createArray(int);
void destroyArray(DynamicArray*);
void addElement(DynamicArray*, TElement);

void testAdd();