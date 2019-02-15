#pragma once
#include "Song.h"

class LocalSong: public Song
{
private:
	double fileSize;
public:
	LocalSong(const std::string& artist, const std::string& title, const Duration& duration, const std::string& source, double fileSize);

	/*
		Overrides the "play" function in the base class.
		Input: -
		Output: plays a locally stored song, using Windows Media Player.
	*/
	void play() const override;

	std::string toString() const override;
	
	/*
		Overrides the "clone" function in the base class. This function will know how to clone a youtube song.
		Input: -
		Output: returns a new local song, containing the same information as the current song.
	*/
	Song* clone() const override;
};

