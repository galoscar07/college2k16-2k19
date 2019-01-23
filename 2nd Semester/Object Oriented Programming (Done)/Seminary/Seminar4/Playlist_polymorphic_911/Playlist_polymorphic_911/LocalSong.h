#pragma once
#include "Song.h"
class LocalSong :
	public Song
{
private:
	int file_size;
public:
	LocalSong();
	LocalSong(const std::string& artist, const std::string& title, const Duration& duration, const std::string& source, const int file_size);
	std::string toString() const;

	void play() const override;

	~LocalSong() {}
};

