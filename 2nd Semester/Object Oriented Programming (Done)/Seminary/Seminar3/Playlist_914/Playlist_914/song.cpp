#include "song.h"
Song::Song(const std::string& artist, const std::string& title, int duration, const std::string& link) {
	this->artist = artist;
	this->title = title;
	this->duration = duration;
	this->link = link;
}

std::string Song::getArtist() const
{
	return this->artist;
}

Song::Song() {
	artist = "";
	title = "";
	duration = 0;
	link = "";
}