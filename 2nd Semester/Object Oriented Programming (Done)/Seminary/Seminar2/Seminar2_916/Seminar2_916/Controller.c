#include "Controller.h"
#include "Planet.h"

void add_planet_controller(Controller * my_controller, char * symbol, char * name, char * solar_syst, double distance_to_E)
{
	Planet* new_planet = createPlanet(symbol, name, solar_syst, distance_to_E);
	repositoryAdd(my_controller->my_repository, new_planet);
}
