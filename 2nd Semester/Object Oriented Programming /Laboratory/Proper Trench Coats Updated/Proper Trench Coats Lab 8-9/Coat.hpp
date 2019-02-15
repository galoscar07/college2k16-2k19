//
//  Entities.hpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 09/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//
#pragma once
#include <iostream>
#include <string>

class Coat{
private:
    int id;
    int size;
    std::string color;
    float price;
    int quantity;
    std::string photo;
    float length;
    
public:
    //Constructors and destructors
    Coat();
    Coat(const int& id,const int& size,const std::string& color, const float& price, const int& quantity, const std::string& picture, const float& length);
    virtual ~Coat() {}
    
    //Operators
    bool operator==(const int& value) const;
    bool operator<(const int& value) const;
    
    //Setter
    void setPrice(const float& price);
    void setQuantity(const int& quatity);
    
    //Getter
    int getId() const { return id; }
    int getSize() const { return size; }
    std::string getColor() const { return color; }
    float getPrice() const { return price; }
    int getQuantity() const { return quantity; }
    std::string getPhoto() const { return photo; }
    float getLength() const { return length; }
    
    //For saving in the file
    friend std::istream& operator>>(std::istream& is, Coat& c);
    friend std::ostream& operator<<(std::ostream& os, const Coat& c);
};
