#pragma once
#include "Song.h"
class YoutubeSong :
	public Song
{
public:
	YoutubeSong(const std::string& artist, const std::string& title, const Duration& duration, const std::string& source);
	void play() const override;
	
	~YoutubeSong() {}
};

