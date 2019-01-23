#pragma once

#include "DynamicArray.h"

typedef struct
{
	DynamicArray *Planets;
}PlanetsRepo;

PlanetsRepo		*Create_Repo();
void addRepo(PlanetsRepo*, Planet*);

void destroyRepo(PlanetsRepo*);