#include "Quadratic.h"
#include <cmath>


std::string Quadratic::solutions()
{
	double delta = this->b*this->b - 4 * this->a*this->c;
	if (delta < 0) {
		double im, base;
		base = -this->b / (2 * this->a);
		im = sqrt(-delta) / (2 * this->a);
		return "x1 = " + std::to_string(base) + " + " + std::to_string(im) + "*i" + " x2 = " + std::to_string(base)+ " - " + std::to_string(im) + "*i";
	}
	if (delta > 0) {
		return "x1 = " + std::to_string((-this->b + sqrt(delta)) / (2 * this->a)) + " x2 = " + std::to_string((-this->b - sqrt(delta)) / (2 * this->a));
	}
	return "x1 = x2 = " + std::to_string(-b / (2 * a));
}

std::string Quadratic::equation()
{
	std::string base = std::to_string(this->a) + "*x^2";
	
	if (this->b > 0.0001)
		base += " + " + std::to_string(this->b) + "*x";
	if(this->b < -0.0001)
		base += " - " + std::to_string(fabs(this->b)) + "*x";

	if (this->c > 0.0001)
		base += " + " + std::to_string(this->c);
	if (this->c < -0.0001)
		base += " - " + std::to_string(fabs(this->c));
	
	return base;
}

bool Quadratic::real()
{
	double delta = this->b*this->b - 4 * this->a*this->c;
	if (delta < 0)
		return false;
	return true;
}

Quadratic::Quadratic()
{
	this->a = this->b = this->c = -1;
}

Quadratic::Quadratic(double a, double b, double c)
{
	this->a = a;
	this->b = b;
	this->c = c;
}

Quadratic::~Quadratic()
{
}
