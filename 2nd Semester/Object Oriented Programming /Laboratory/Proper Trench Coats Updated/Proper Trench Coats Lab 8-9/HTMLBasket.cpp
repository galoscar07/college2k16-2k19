//
//  HTMLBasket.cpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 15/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#include "CSVBasket.hpp"
#include "FileBasket.hpp"
#include <fstream>
#include "RepositoryExceptions.hpp"
#include "HTMLBasket.hpp"
#include <iostream>

HTMLBasket::HTMLBasket() : FileBasket(){
    
}

void HTMLBasket::writeToFile(){
    ofstream f(this->fileName);
    f << "<!DOCTYPE html>" << endl;
    f << "<html>" << endl;
    f << "<head>" << endl;
    f << "<title>Basket</title>" << endl;
    f << "</head>" << endl;
    f << "<body>" << endl;
    f << "<table border = \"1\">" << endl;
    f << "<tr>" << endl;
    f << "<td>Id</td>" << endl;
    f << "<td>Size</td>" << endl;
    f << "<td>Color</td>" << endl;
    f << "<td>Price</td>" << endl;
    f << "<td>Quatity</td>" << endl;
    f << "<td>Photo Link</td>" << endl;
    f << "<td>Length</td>" << endl;
    f << "</tr>" << endl;
    for (auto i : this->coats){
        f << "<tr>" << endl;
        f << "<td>" <<i.getId() << "</td>" << endl;
        f << "<td>" <<i.getSize() << "</td>" << endl;
        f << "<td>" <<i.getColor() << "</td>" << endl;
        f << "<td>" <<i.getPrice() << "</td>" << endl;
        f << "<td>" <<i.getQuantity() << "</td>" << endl;
        f << "<td><a href = \"" <<i.getPhoto() << "\"Link</a></td>" << endl;
        f << "<td>" <<i.getPrice() << "</td>" << endl;
        f << "</tr>" << endl;
    }
    f << "</table>" << endl;
    f << "</body>" << endl;
    f << "</html>" << endl;
    f.close();
}

void HTMLBasket::displayBasket(){
    
}
