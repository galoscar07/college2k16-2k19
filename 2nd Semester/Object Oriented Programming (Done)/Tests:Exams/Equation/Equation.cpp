//
// Created by Gal Oscar on 18/06/2017.
//

#include "Equation.h"
using namespace std;

Equation::Equation() {

}

Equation::Equation(int a, int b, int c) {
    this->a = a;
    this->b = b;
    this->c = c;
}

Equation::~Equation() {
}

std::string Equation::toString() {
    string something = to_string(this->a) + "*x^2" + to_string(this->b) + "*x" + to_string(this->c);
    return something;
}

std::string Equation::toStringA() {
    string something = to_string(this->a);
    return something;
}

std::string Equation::toStringB() {
    string something = to_string(this->b);
    return something;
}

std::string Equation::toStringC() {
    string something = to_string(this->c);
    return something;
}
