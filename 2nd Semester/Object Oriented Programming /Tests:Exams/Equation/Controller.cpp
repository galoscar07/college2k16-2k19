//
// Created by Gal Oscar on 18/06/2017.
//

#include "Controller.h"

Controller::Controller() {

}

Controller::Controller(Repository r) {
    this->repo = r;
}

Controller::~Controller() {

}

std::vector<Equation> Controller::getAll() {
    return this->repo.getAll();
}
