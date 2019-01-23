#pragma once
#include<string>

class Song
{
private:
	std::string title;
	std::string artist;
	int duration;
	std::string source;
public:
	Song();
	Song(const std::string &title,const std::string &artist, int duration,const std::string &source);
	
	std::string getTitle()const { return this->title; };
	std::string getArtist()const { return this->artist; };
	
	void play();
};

