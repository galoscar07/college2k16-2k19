#include "Song.h"
#include <string>

using namespace std;

Song::Song(): title(""), artist(""), duration(Duration()), source("") {}

Song::Song(const string& artist, const string& title, const Duration& duration, const string& source)
{
	this->artist = artist;
	this->title = title;
	this->duration = duration;
	this->source = source;
}

string Song::toString() const
{
	string result = this->artist + " " + std::to_string(this->duration.getMinutes()) + " " + std::to_string(this->duration.getSeconds()) + " " + this->title + " " + this->source;
	return result;
}
