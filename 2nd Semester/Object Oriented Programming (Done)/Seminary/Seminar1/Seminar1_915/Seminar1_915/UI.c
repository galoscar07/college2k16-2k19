#include "UI.h"
#include "Controller.h"

void printMenu()
{
	printf("\n**********************************************************\n");
	printf("1 - add a planet.\n");
	printf("2 - list all planets.\n");
	printf("0 - to exit.\n");
	printf("\**********************************************************\n");
}

int addPlanetUI(UI* ui)
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

	controller_add_planet(ui->ctrl, symbols, name, solarSystem, distanceToEarth);
}

int readIntegerNumber(const char* message)
{
	char s[16];
	int res = 0;
	int flag = 0;
	int r = 0;

	while (flag == 0)
	{
		printf(message);
		scanf("%s", s);

		r = sscanf(s, "%d", &res);	// reads data from s and stores them as integer, if possible; returns 1 if successful
		flag = (r == 1);
		if (flag == 0)
			printf("Error reading number!\n");
	}
	return res;
}

void run(UI* ui)
{
	while (1)
	{
		printMenu();
		int command = 0;
		printf("Enter a command: ");
		scanf("%d", &command);

		if (command == 0)
			break;
		switch (command)
		{
		case 1:
		{
			int res = addPlanetUI(ui);
			printf("Planet successfully added.\n");
			break;
		}
		case 2:
		{
			//listAllPlanets(ui);
			break;
		}
		case 3:
		{
			//listPlanetsWithCombination(ui);
			break;
		}
		}
	}

}
