#pragma once

typedef struct {
	char symbol[8];
	char name[100];
	char solarSystem[100];
	double distance;
}Planet;

Planet create_planet(char *symbol, char *name, char *solarSystem, double distance);


