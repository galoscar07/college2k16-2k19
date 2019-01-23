#pragma once
#include "Planet.h"
#include <assert.h>

typedef struct
{
	Planet v[100];
	int len;
}PlanetRepo;

PlanetRepo createRepo();

//Function for adding a planet to the repository
//Input: r - a pointer to the planet repository
//		 p - a planet
//Output:planet 'p' will be added to the repository
void addPlanet(PlanetRepo *r, Planet p);

void testAdd();