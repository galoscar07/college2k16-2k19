#pragma once

#include <vector>
#include <string>
#include "Song.h"

class SongException: public std::exception
{
private:
	std::vector <std::string> errors;
public:
	SongException(std::vector <std::string> error)
	{
		this->errors = error;
	}
	std::vector <std::string> GetError()
	{
		return this->errors;
	}
};

class SongValidator
{
public:
	static void Validate(const Song& s);
};