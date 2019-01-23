//
// Created by Gal Oscar on 26/05/2017.
//

#pragma once
#include "Coat.h"
#include <vector>

class Repository{
private:
    std::vector<Coat> coats;
    std::string filename;

public:
    //Constructor and deconstructors
    Repository();

    Repository(const std::string& filename);
    /*
     Default constructor for the repository.
     Initializes an object of type repository.
     */

    //Functions

    void addCoat(const Coat& coat);
    /*
     Adds a coat to the repository.
     Input: c which is type coat.
     Exception: The function will raise an exception if the element that we want to add already exists in the list
     */

    void removeCoat(const Coat& coat);
    /*
     Removes a Coat by id from the database.
     Input: id id which is an int.
     Exception: The function will raise an exception if the element that we want to remove is not in the list
     */

    Coat findById(const int& id) const;
    /*
     Finds a Coat by id and return the coat if the id was found and an empty coat if the coat wasn't found.
     Input: id which is an int.
     Output: the Coat that was found
     Exception: The function will raise an exception if the element that we searsh is not in the list
     */

    void updateCoat(const Coat& coat);
    /*
     Updates a Coat's price and (or) quantity.
     Input: id which is an int, price id which is a float, quantity id which is an int
     Exception: the function will raise an exception if the element that we are searching to update doesn't exist in the data base
     */

    std::vector<Coat> getCoats() const { return coats; }
    /*
     Returns a Vector containing all the coats.
     Output: coats - Vector.
     */
private:
    void readFromFile();
    /*
     The function will read from a file the entire database of coats
     */
    void writeToFile();
    /*
     The function will write into a file the entire database of coats
     */

};
