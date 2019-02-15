//
//  Coats.hpp
//  Proper Trench Coats Lab 5-6
//
//  Created by Gal Oscar on 09/04/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include <iostream>

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
    Coat();
    Coat(const int& id,const int& size,const std::string& color, const float& price, const int& quantity, const std::string& picture, const float& length);
    bool operator==(const int& value) const;
    bool operator<(const int& value) const;
    void setPrice(const float& price);
    void setQuantity(const int& quatity);
    int getId() const { return id; }
    int getSize() const { return size; }
    std::string getColor() const { return color; }
    float getPrice() const { return price; }
    int getQuantity() const { return quantity; }
    std::string getPhoto() const { return photo; }
    float getLength() const { return length; }
};
