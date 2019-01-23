#pragma once
#include "Repository.h"
typedef struct
{
	Repository *repo;
}Controller;

Controller CreateController(Repository *reposit);
void AddPlanetToTheController(Controller*, char name[20], char solar[], char *symb, int distance);



