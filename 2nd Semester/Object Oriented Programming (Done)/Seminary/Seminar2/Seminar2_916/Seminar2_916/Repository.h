#pragma once

#include "DynArr.h"

typedef struct {
	DynamicArray *arr;
} Repository;


Repository *repositoryCreate();

void repositoryDestroy(Repository *rep);

void repositoryAdd(Repository *rep, Planet *p);