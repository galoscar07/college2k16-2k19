#include "DynamicArray.h"
#include<stdlib.h>
#include<assert.h>
DynamicVector* createVector(int capacity)
{
	DynamicVector* vector = (DynamicVector*)malloc(sizeof(DynamicVector)*capacity);
	vector->capacity = capacity;
	vector->elems = (Telement*)malloc(sizeof(Telement)*capacity);
	vector->size = 0;
	return vector;
}

void destroyVector(DynamicVector * vector)
{
	if (vector == NULL)
		return;
	free(vector->elems);
	free(vector);
}

void addElem(DynamicVector * vector, Telement el)
{
	if (vector != NULL) {
		vector->elems[vector->size++] = el;

		if (vector->size == vector->capacity)
			increaseCapacity(vector);
	}
}

void increaseCapacity(DynamicVector* vector) {
	if (vector != NULL) {
		vector->capacity *= 2;
		vector->elems = (Telement*)realloc(vector->elems, vector->capacity * sizeof(Telement));

	}
}
void TestArray()
{
	DynamicVector *vector = createVector(1);
	Planet *planet = createPlanet("12251251", "Earth", "SOL", 0);
	Planet *planet2 = createPlanet("25568988", "Mars", "SOL", 15);
	addElem(vector, planet);
	assert(vector->size == 1);
	assert(vector->capacity == 2);

	addElem(vector, planet2);
	assert(vector->size == 2);
	assert(vector->capacity == 4);

	destroyPlanet(planet);
	destroyPlanet(planet2);
	destroyVector(vector);
}