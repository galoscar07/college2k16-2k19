#include "Controller.h"
#include "Planet.h"
#include <stdlib.h>

void createController(PlanetsRepo * r)
{
	Controller* c = (Controller*)malloc(sizeof(Controller));
	c->repo = r;

	return c;
}

void addPlanetCtrl(Controller * c, char * sym, char * name, char * system, double dist)
{
	Planet* p = createPlanet(sym, name, system, dist);
	addRepo(c->repo, p);
}
