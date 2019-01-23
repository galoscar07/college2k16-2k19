#pragma once
#include "Planet.h"
#define CAPACITY 10
typedef Planet* TElement;

typedef struct {
	TElement* elems;
	int size;
	int capacity;
}DynamicArray;


DynamicArray* create_array(int capacity);
void destroy_array(DynamicArray* arr);
void add_to_array(DynamicArray*, TElement);
TElement get_from_array(DynamicArray * arr, int id);
void testsDynamicArray();