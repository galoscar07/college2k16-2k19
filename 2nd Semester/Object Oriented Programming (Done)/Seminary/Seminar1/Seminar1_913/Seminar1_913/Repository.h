#pragma once
#include  "planet.h"
typedef struct {
	planet planets[100];
	int length;
}Planets;

Planets createRepository();

void addPlanet(Planets*, planet);
void test_add();