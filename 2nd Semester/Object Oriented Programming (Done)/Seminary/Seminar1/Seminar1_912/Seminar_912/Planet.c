#include "Planet.h"
#include<string.h>

Planet CreatePlanet(char name[], char symbol[], char system[], int dist)
{
	Planet p;
	strcpy(p.name, name);
	strcpy(p.symbol, symbol);
	strcpy(p.system, system);
	p.dist = dist;
	return p;
}
