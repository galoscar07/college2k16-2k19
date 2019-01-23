#include "Controller.h"

Controller create_controller(PlanetRepo * r){
	Controller obj;
	obj.repo = r;
	
	return obj;
}

void controller_add_planet(Controller * c, char * symbol, char * name, char * solarSystem, double distance)
{
	Planet p = create_planet(symbol, name, solarSystem,distance);
	addPlanet(c->repo, p);
}
