#pragma once
#include "Repository.h"

class Controller
{
private:
	Repository repo;
public:
	Controller() {};
	Controller(Repository r);
	~Controller();

	void update(int index, double a, double b, double c);
	std::vector<Quadratic> getAll();
	/*
	Filters the equations by solution type.
	The allowed types are "All", "Real" and "Imaginary".
	Input: string containing the type
	Output: vector containing the filtered equations
	*/
	std::vector<Quadratic> filter(std::string type);
};

