#include "Controller.h"

Controller createController(Planets * repo)
{
	Controller new_controller;
	new_controller.repo = repo;
	return new_controller;
}

void addPlanetController(Controller *myController, char symbol[], char solar_syst[], char name[], int distance)
{
	planet new_planet = create_planet(symbol, solar_syst, name, distance);
	addPlanet(myController->repo, new_planet);
}
