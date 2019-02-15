//
// Created by Gal Oscar on 18/06/2017.
//
#pragma once
#include <iostream>
#include <string>
#include <fstream>

class Equation{
private:
    int a;
    int b;
    int c;
public:
    Equation();
    Equation(int a, int b, int c);
    ~Equation();

    int getA() { return a; }
    int getB() { return b; }
    int getC() { return c; }

    void setA(const int& x) { a = x; };
    void setB(const int& x) { b = x; };
    void setC(const int& x) { c = x; };

    std::string toString();
    std::string toStringA();
    std::string toStringB();
    std::string toStringC();
};