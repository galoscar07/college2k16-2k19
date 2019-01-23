#pragma once
#include <string>
class Song {
private:
	std::string artist;
	std::string title;
	int duration;
	std::string link;
public:
	Song();
	Song(const std::string& artist, const std::string& title, int duration, const std::string& link);
	std::string getArtist() const;
	std::string getTitle() const { return this->title; };
};


