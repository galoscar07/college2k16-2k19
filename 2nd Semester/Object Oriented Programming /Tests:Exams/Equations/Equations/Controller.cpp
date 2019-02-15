#include "Controller.h"


Controller::Controller(Repository r)
{
	this->repo = r;
	this->repo.load();
}

Controller::~Controller()
{
}

void Controller::update(int index, double a, double b, double c)
{
	Quadratic &e = this->repo.get(index);
	e.setA(a);
	e.setB(b);
	e.setC(c);
}

std::vector<Quadratic> Controller::getAll()
{
	return this->repo.getAll();
}

std::vector<Quadratic> Controller::filter(std::string type)
{
	if (type == "All") {
		return this->getAll();
	}

	std::vector<Quadratic> v = this->getAll();
	std::vector<Quadratic> results;

	if (type == "Real") {
		for (auto e : v)
			if (e.real())
				results.push_back(e);
	}

	else {
		for (auto e : v)
			if (!e.real())
				results.push_back(e);
	}
	return results;
}
