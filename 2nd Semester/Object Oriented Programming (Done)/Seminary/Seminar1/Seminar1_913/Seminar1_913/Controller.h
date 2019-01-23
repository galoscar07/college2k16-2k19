#pragma once
#include "Repository.h"
#include "Planet.h"
typedef struct {
	Planets *repo;
}Controller;

Controller createController(Planets *repo);

void addPlanetController(char symbol[], char solar_syst[], char name[], int distance);

