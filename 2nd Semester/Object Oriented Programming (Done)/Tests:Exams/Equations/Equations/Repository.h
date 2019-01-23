#pragma once
#include <vector>
#include <fstream>
#include "Quadratic.h"

class Repository
{
private:
	std::vector<Quadratic> equations;
	std::string filename;
public:
	Repository() {};
	Repository(std::string path);
	
	void load();
	void add(double a, double b, double c);
	Quadratic& get(int index);
	std::vector<Quadratic> getAll();

	~Repository();
};

