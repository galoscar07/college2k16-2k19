#include "Song.h"
#include <sstream>

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
	stringstream s;
	s << this->artist << " - " << this->title << ", " << this->duration.getMinutes() << ":" << this->duration.getSeconds() << endl;
	s << "Source: " << this->source << endl;
	return s.str();
}
