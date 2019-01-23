#include "UI.h"

int main() 
{
	test_add();

	Planets repo = createRepository();
	Controller ctrl = createController(&repo);
	UI ui = createUI(&ctrl);

	run(&ui);

	return 0;
}