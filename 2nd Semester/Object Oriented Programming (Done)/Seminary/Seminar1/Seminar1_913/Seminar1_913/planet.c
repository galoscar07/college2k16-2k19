#include "Planet.h"
#include<string.h>


planet create_planet(char symbol[], char solar_syst[], char name[], int distance)
{
	planet p1;
	strcpy(p1.name, name);
	strcpy(p1.symbol, symbol);
	strcpy(p1.solar_syst, solar_syst);
	p1.distance = distance;
	return p1;
}
