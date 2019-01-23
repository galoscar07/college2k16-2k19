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
	string str;

	str = "Title: " + title + "\n";
	str += "Artist: " + artist + "\n";
	str += "Duration: " + to_string(duration.getMinutes()) + " minutes and " + to_string(duration.getSeconds()) + " seconds\n";
	str += "Source: " + source + "\n";

	return str;
}
