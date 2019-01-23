#pragma once
#include "Repository.h"

typedef struct
{
	PlanetsRepo* repo;
} Controller;

void createController(PlanetsRepo* r);
void addPlanetCtrl(Controller* c, char* sym, char* name, char* system, double dist);
void destroyController(Controller* c);