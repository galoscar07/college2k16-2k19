#include "DynArr.h"
#include <stdlib.h>
#include <assert.h>

DynamicArray * create_array(int capacity)
{
	DynamicArray *p = (DynamicArray*)malloc(sizeof(DynamicArray));
	p->capacity = capacity;
	p->size = 0;
	p->elems = (TElement*)malloc(sizeof(TElement)*capacity);
	return p;
}


void destroy_array(DynamicArray * arr)
{
	if (arr == NULL)
		return;

	free(arr->elems);
	free(arr);
}

void resize(DynamicArray* arr)
{
	arr->capacity *= 2;
	arr->elems = (TElement*)realloc(arr->elems, arr->capacity * sizeof(TElement));
}

void add_to_array(DynamicArray* arr, TElement e)
{
	if (arr->size == arr->capacity)
		resize(arr);

	arr->elems[arr->size++] = e;
}

TElement get_from_array(DynamicArray * arr, int id)
{
	return arr->elems[id];
}

void testsDynamicArray()
{
	DynamicArray* da = create_array(2);
	if (da == NULL)
		assert(0);

	assert(da->capacity == 2);
	assert(da->size == 0);

	Planet* p1 = createPlanet("UV$O*~1", "Gallifrey", "Kasterborous", 250000);
	add_to_array(da, p1);
	assert(da->size == 1);

	Planet* p2 = createPlanet("V^E$9L@", "Abydos", "Sol", 583);
	add_to_array(da, p2);
	assert(da->size == 2);

	// capacity must double
	Planet* p3 = createPlanet("A&V$9+Q", "Cimmeria", "Asgard", 1058);
	add_to_array(da, p3);
	assert(da->size == 3);
	assert(da->capacity == 4);

	//// delete planet on position 0
	//delete(da, 0);
	//Planet* p = get(da, 0);
	//assert(strcmp(getName(p), "Abydos") == 0);
	//assert(da->length == 2);

	// destroy the dynamic array
	destroy_array(da);

	// destroy the planets
	destroyPlanet(p1);
	destroyPlanet(p2);
	destroyPlanet(p3);
}