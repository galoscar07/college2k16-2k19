#pragma once
#include "DynamicArray.h"

typedef struct
{
	DynamicVector* planets;
} Repository;

Repository* createRepo();
void destroyRepo(Repository*);
void addPlanet(Repository*, Planet*);