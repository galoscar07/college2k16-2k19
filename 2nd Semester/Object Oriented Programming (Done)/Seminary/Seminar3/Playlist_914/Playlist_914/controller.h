#pragma once
#include "repository.h"
class Controller {
private:
	Repository& repo;
public:
	Controller(Repository& r);
	int getSize() { return this->repo.getSize(); }
	void addSong(const Song& s);
};