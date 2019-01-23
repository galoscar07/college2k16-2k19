#include <stdio.h>
#include <string.h>
#include "Planet.h"

Planet create_planet(char * symbol, char * name, char * solarSystem, double distance)
{
	Planet x;
	strcpy(x.symbol, symbol);
	strcpy(x.name, name);
	strcpy(x.solarSystem, solarSystem);
	x.distance = distance;
	return x;
}


