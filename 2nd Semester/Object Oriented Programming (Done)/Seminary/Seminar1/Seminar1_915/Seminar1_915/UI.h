#pragma once
#include "Controller.h"

typedef struct
{
	Controller* ctrl;
} UI;

void run(UI* ui);