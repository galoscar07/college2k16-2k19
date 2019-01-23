#include "Controller.h"

Controller CreateController(Repository * reposit)
{

		Controller c;
		c.repo = reposit;
	
}

void AddPlanetToTheController(Controller * contr, char name[20], char solar[], char *symb, int distance)
{
	Planet p;
	p = CreatePlanet(name, symb, solar, distance);
	addPlanet(contr->repo, p);
}
