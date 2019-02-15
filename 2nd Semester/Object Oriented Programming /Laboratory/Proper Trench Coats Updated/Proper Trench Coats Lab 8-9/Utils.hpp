//
//  Utils.hpp
//  Proper Trench Coats Lab 8-9
//
//  Created by Gal Oscar on 15/05/2017.
//  Copyright © 2017 Gal Oscar. All rights reserved.
//

#pragma once
#include <string>
#include <vector>

/*
	Trims leading and trailing spaces from a string.
	Input: s - string
	Output: a string, with no leading and trailing spaces.
 */
std::string trim(const std::string& s);

/*
	Tokenizes a string.
	Input:	str - the string to be tokenized.
	delimiter - char - the delimiter used for tokenization
	Output: a vector of strings, containing the tokens
 */
std::vector<std::string> tokenize(const std::string& str, char delimiter);
