
#pragma once
#include"Planet.h"
typedef struct
{
	Planet planetList[100];
	int planetNumber;
}Repository;
Repository createRepository();
void addPlanet(Repository *repo, Planet p);
void Test_addPlanet();