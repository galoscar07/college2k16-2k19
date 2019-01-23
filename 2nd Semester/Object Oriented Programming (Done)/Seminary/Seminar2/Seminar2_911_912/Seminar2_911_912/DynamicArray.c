#include "DynamicArray.h"
#include <assert.h>
#include<stdlib.h>

DynamicArray* createArray(int capacity)
{
	DynamicArray* vector = (DynamicArray*)malloc(sizeof(DynamicArray));
	vector->length = 0;
	vector->capacity = capacity;
	vector->elems = (TElement*)malloc(capacity* sizeof(TElement));
	return vector;
}

void destroyArray(DynamicArray* vector)
{
	if (vector != NULL)
	{
		free(vector->elems);
		free(vector);
	}
}

void realocate(DynamicArray* a) {
	a->capacity *= 2;
	a->elems = (TElement*)realloc(a->elems, sizeof(a->elems) * a->capacity);
}

void addElement(DynamicArray* a, TElement* e) {
	
	if (a->length == a->capacity)
		realocate(a);
	a->elems[a->length] = e;
	a->length++;
}

void testAdd()
{
	DynamicArray* arr = createArray(1);

	Planet* p1 = createPlanet("UV$O*~1", "Gallifrey", "Kasterborous", 250000);
	Planet* p2 = createPlanet("V^E$9L@", "Abydos", "Sol", 583);
	
	addElement(arr, p1);
	assert(arr->length == 1);

	addElement(arr, p2);
	assert(arr->length == 2);
	assert(arr->capacity == 2);

	destroyPlanet(p1);
	destroyPlanet(p2);

	destroyArray(arr);
}