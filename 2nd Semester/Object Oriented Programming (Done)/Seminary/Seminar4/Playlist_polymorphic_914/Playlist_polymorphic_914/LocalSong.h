#pragma once
#include "Song.h"
#include <string>
using namespace std;

class LocalSong : public Song {
private:
	unsigned int fileSize;
public:
	LocalSong(const string& artist, const string& title, const Duration& duration, const string& source, unsigned int fileSize);
	string toString() const override;

	void play() const override;

	~LocalSong() {}
};

