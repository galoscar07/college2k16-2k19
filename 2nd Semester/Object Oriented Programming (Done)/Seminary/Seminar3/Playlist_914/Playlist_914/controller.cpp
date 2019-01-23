#include "controller.h"

Controller::Controller(Repository& r) : repo{ r }
{
}

void Controller::addSong(const Song & s)
{
	this->repo.addSong(s);
}
