//
//  Utils.cpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 15/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#include "Utils.hpp"
#include <sstream>
#include <string>
#include <vector>

using namespace std;

std::string trim(const std::string& s){
    std::string result(s);
    long pos = result.find_first_not_of(" ");
    if (pos != -1)
        result.erase(0, pos);
    pos = result.find_last_not_of(" ");
    if (pos != std::string::npos)
        result.erase(pos + 1);
    
    return result;
}

vector<string> tokenize(const string& str, char delimiter){
    vector <string> result;
    stringstream ss(str);
    string token;
    while (getline(ss, token, delimiter))
        result.push_back(token);
    
    return result;
}
