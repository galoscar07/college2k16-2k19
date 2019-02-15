#include "Repository.h"


Repository::Repository(std::string path)
{
	this->filename = path;
}

void Repository::load()
{
	std::ifstream f(this->filename);
	double a, b, c;
	while (f >> a) {
		f >> b;
		f >> c;
		this->equations.push_back(Quadratic{ a,b,c });
	}
	f.close();
}

void Repository::add(double a, double b, double c)
{
	this->equations.push_back(Quadratic(a, b, c));
}

Quadratic & Repository::get(int index)
{
	return this->equations[index];
}

std::vector<Quadratic> Repository::getAll()
{
	return this->equations;
}

Repository::~Repository()
{
}


