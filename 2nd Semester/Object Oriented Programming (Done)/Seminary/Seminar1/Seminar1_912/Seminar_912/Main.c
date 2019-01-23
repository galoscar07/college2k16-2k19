#include<stdio.h>
#include "UI.h"
#include <Windows.h>

int main()
{
	system("color f4");

	Test_addPlanet();

	Repository repo = createRepository();
	Controller ctrl = CreateController(&repo);
	UI ui = createUI(&ctrl);
	run(&ui);

	system("pause");
	return 0;
}