#pragma once
#include<string>

class Song
{
private:
	std::string artist;
	std::string title;
	int  duration;
	std::string link;
public:
	Song(const std::string& artist, const std::string& title,int duration, const std::string& link);
	Song();
	std::string get_artist()const { return this->artist; }
	std::string get_title()const { return this->title; }

	void play();
};