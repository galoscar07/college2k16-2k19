#include "UI.h"
#include <stdio.h>

UI createUI(Controller * c)
{
	UI ui;
	ui.ctrl = c;
	return ui;
}

void printMenu()
{
	printf("\n**********************************************************\n");
	printf("1 - add a planet.\n");
	printf("2 - list all planets.\n");
	printf("0 - to exit.\n");
	printf("\**********************************************************\n");
}

void addPlanetUI(UI* ui)
{
	// read the planet's data
	char symbols[8], name[50], solarSystem[50];
	double distanceToEarth;

	printf("Please input the symbol combination (must contain 7 symbols): ");
	scanf("%7s", symbols);
	printf("Please input the name: ");
	scanf("%49s", name);
	printf("Please input the solar system: ");
	scanf("%49s", solarSystem);
	printf("Please input the distance to Earth (in thousands of light years): ");
	scanf("%lf", &distanceToEarth);

	AddPlanetToTheController(ui->ctrl, name, solarSystem, symbols, distanceToEarth);
}

void run(UI* ui)
{
	while (1)
	{
		printMenu();
		int command = 0;
		printf("Please input the command: ");
		scanf("%d", &command);

		switch (command)
		{
		case 1:
			addPlanetUI(ui);
			break;
		case 2:
			//listAllPlanets(ui);
			break;
		case 0:
			break;
		default:
			break;
		}
	}
}
