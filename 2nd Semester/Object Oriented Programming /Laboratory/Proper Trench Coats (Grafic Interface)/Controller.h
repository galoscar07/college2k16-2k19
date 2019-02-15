//
// Created by Gal Oscar on 23/05/2017.
//

#pragma once
#include "Repository.h"
#include "FileBasket.h"
#include <assert.h>
#include <vector>
#include "Validators.h"

class Controller{
private:
    Repository repo;
    CoatValidator validators;
public:
    FileBasket* basketList;
public:

    Controller(const Repository& r, CoatValidator v,FileBasket* file) : repo{ r }, validators{ v },basketList(file) {}

    Controller(const Repository& r) : repo(r) {}

    ~Controller();

    Repository getRepo() const { return repo; }

    void addCoatToRepo(const int& id, const int& size,const std::string& color,const float& price, const int& quantity, const std::string& photo, const float& length);

    void addCoatToBasket(Coat& coat);

    void removeCoatFromRepo(const int& id);

    void updateCoatInRepo(const int& id, const float& price, const int& quantity);

    std::vector<Coat> filterBySize(const int& size);

    std::vector<Coat> getAllCoats() const { return this->repo.getCoats(); }

    std::vector<Coat> getCoatsFromBasket() const {return this->basketList->getAll();}

    string getMoney();

    std::vector<Coat> filterCoatsByLength(const float& length);
};
