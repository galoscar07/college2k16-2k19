#pragma once
#include "Song.h"

class YoutubeSong: public Song
{
public:
	YoutubeSong(const std::string& artist, const std::string& title, const Duration& duration, const std::string& source);

	/*
		Overrides the "play" function in the base class.
		Input: -
		Output: plays a youtube song, using chrome.
	*/
	void play() const override;

	/*
		Overrides the "clone" function in the base class. This function will know how to clone a youtube song. 
		Input: -
		Output: returns a new Youtube song, containing the same information as the current song.
	*/
	Song* clone() const override;
};

