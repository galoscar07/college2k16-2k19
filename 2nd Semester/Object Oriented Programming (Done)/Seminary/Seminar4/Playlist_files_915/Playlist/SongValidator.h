#pragma once
#include <vector>
#include "Song.h"

class SongException
{
private:
	std::vector<std::string> errors;

public:
	SongException(std::vector<std::string> err) : errors{ err } {}
	std::vector<std::string> getErrors() const { return errors; }
};

class MyException : public std::exception
{
private:
	std::string message;
public:
	const char* what() { return message.c_str(); }
};

class SongValidator
{
public:
	static void validate(const Song& s);
};

