#pragma once
typedef struct
{
	char name[20];
	char symbol[8];
	char system[20];
	int dist;
}Planet;
Planet CreatePlanet(char name[], char symbol[], char system[], int dist);

void toString(Planet p, char* str);
