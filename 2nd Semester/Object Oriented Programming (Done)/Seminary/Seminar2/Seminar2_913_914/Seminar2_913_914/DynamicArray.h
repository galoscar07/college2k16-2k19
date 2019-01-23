#pragma once
#include "Planet.h"

#define CAPACITY 10

typedef Planet* Telement;
typedef struct
{
	int size;
	int capacity;
	Telement*elems;
}DynamicVector;
DynamicVector* createVector(int capacity);
void destroyVector(DynamicVector* vector);
void addElem(DynamicVector* vector, Telement el);
void TestArray();