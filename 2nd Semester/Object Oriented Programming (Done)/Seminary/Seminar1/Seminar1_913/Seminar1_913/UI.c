#include "UI.h"
#include <stdio.h>
UI createUI(Controller * cont)
{
	UI newUI;
	newUI.cont = cont;
	return newUI;
}

/*
Prints the available menu for the problem
Input: -
Output: the menu is printed at the console
*/
void printMenu()
{
	printf("\n**********************************************************\n");
	printf("1 - add a planet.\n");
	printf("2 - list all planets.\n");
	//printf("3 - list planets with a given symbol combination.\n");
	printf("0 - to exit.\n");
	printf("\**********************************************************\n");
}

/*
Verifies if the given command is valid (is either 1, 2 or 0)
Input: command - integer
Output: 1 - if the command is valid
0 - otherwise
*/
int validCommand(int command)
{
	if (command >= 0 && command <= 2)
		return 1;
	return 0;
}

/*
Reads an integer number from the keyboard. Asks for number while read errors encoutered.
Input: the message to be displayed when asking the user for input.
Returns the number.
*/
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

	//return addPlanet(ui->ctrl, symbols, name, solarSystem, distanceToEarth);
	addPlanetController(ui->cont, symbols, solarSystem, name, distanceToEarth);
}

void run(UI * ui)
{
	while (1)
	{
		printMenu();
		int command = readIntegerNumber("Input command: ");
		while (validCommand(command) == 0)
		{
			printf("Please input a valid command!\n");
			command = readIntegerNumber("Input command: ");
		}
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
		}
	}
}
