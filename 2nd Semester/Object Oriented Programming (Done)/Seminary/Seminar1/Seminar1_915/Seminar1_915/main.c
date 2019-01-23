#include "PlanetRepository.h"
#include <Windows.h>
#include "Controller.h"
#include "UI.h"

int main()
{
	testAdd();

	PlanetRepo repo = createRepo();
	Controller ctrl = create_controller(&repo);
	UI ui;
	ui.ctrl = &ctrl;

	run(&ui);

	system("pause");
	return 0;
}