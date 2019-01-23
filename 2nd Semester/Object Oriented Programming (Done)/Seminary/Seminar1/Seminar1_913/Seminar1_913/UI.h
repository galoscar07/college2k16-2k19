#pragma once
#include "Controller.h"

typedef struct
{
	Controller *cont;
}UI;

UI createUI(Controller *cont);

void run(UI* ui);