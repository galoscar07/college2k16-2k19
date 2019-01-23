#pragma once
#include "PlanetRepository.h"
#include<stdio.h>

typedef struct {
	PlanetRepo *repo;

}Controller;

Controller create_controller(PlanetRepo *r);

void controller_add_planet(Controller *c, char * symbol, char * name, char * solarSystem, double distance);