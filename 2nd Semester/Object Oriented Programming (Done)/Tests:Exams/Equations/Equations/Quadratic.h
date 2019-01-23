#pragma once
#include <string>

class Quadratic
{
private:
	double a, b, c;
public:
	/*
	Computes the solutions to the equation.
	Input: - 
	Output: string containing the solutions to the quadratic equation
	*/
	std::string solutions();
	std::string equation();
	bool real();
	double getA() { return a; };
	double getB() { return b; };
	double getC() { return c; };
	void setA(double x) { a = x; };
	void setB(double x) { b = x; };
	void setC(double x) { c = x; };

	Quadratic();
	Quadratic(double a, double b, double c);
	~Quadratic();
};

