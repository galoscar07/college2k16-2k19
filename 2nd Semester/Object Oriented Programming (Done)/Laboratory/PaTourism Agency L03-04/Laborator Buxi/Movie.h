#pragma once
#include <iostream>

class Movie
{
private:
	std::string title;
	std::string genre;
	int duration;
	int year;
	int likes;
	std::string trailer; //link

public:
	//default constructor
	Movie();

	//copy constructor
	Movie(const Movie& m);

	//construtor with parameters
	Movie(const std::string& title, const std::string& genre, int duration, int year, int likes, const std::string trailer);

	std::string getTitle()const { return title; }
	std::string getGenre()const { return genre; }
	int getDuration() { return duration; }
	int getYear() { return year; }
	int getLikes() { return likes; }
	std::string getTrailer()const { return trailer; }

	void setGenre(std::string& newg) { genre = newg; }

	bool operator==(const std::string& title) { return this->title == title; }
	//plays the current trailer
	void play();
};