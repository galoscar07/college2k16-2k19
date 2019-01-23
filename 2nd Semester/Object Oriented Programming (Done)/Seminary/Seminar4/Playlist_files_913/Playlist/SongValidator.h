#pragma once
#include <vector>
#include "Song.h"
class SongException
{
private:
	std::vector<std::string> errors;

public:
	SongException(std::vector<std::string> v) { this->errors = v; };
	
	std::vector<std::string> get_errors() const { return errors; }
};

class SongValidator
{
public:
	static void validate(const Song& s);
};

