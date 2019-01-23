#pragma once
#include <iostream>
#include <string>

class Duration
{
private:
	double minutes;
	double seconds;
public:
	Duration() : minutes(0), seconds(0) {}
	Duration(double min, double sec) : minutes(min), seconds(sec) {}

	double getMinutes() const { return minutes; }
	double getSeconds() const { return seconds; }
	void setMinutes(double min) { minutes = min; }
	void getSeconds(double sec) { seconds = sec; }
};

class Song
{
protected:
	std::string title;
	std::string artist;
	Duration duration;
	std::string source;		// might be a youtube link or a local file

public:
	// default constructor for a song
	Song();

	// constructor with parameters
	Song(const std::string& artist, const std::string& title, const Duration& duration, const std::string& source);

	std::string getTitle() const { return title; }
	std::string getArtist() const { return artist; }
	Duration getDuration() const { return duration; }
	std::string getSource() const { return source; }

	// converts a Song to its string representation
	std::string toString() const;

	virtual void play() const = 0;

	virtual ~Song() {}
};

