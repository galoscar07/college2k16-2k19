#pragma once
typedef struct
{
	char symbol[8];
	char solar_syst[100];
	char name[100];
	int distance;
}planet;

planet create_planet(char symbol[], char solar_syst[], char name[], int distance);
