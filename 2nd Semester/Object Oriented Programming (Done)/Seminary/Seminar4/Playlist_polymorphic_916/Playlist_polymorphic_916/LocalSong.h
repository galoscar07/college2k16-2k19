#pragma once
#include "Song.h"
class LocalSong : public Song
{
private:
	double fileSize;

public:
	LocalSong(const std::string& artist, const std::string& title, const Duration& duration, const std::string& source, double size);
	std::string toString() const override;

	void play() const override;

	~LocalSong() {}
};

