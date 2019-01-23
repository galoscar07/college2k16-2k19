#pragma once
#include "Repository.h"

typedef struct {
	Repository* my_repository;

}Controller;

void add_planet_controller(Controller* my_controller, char* symbol, char* name, char*solar_syst, double distance_to_E);