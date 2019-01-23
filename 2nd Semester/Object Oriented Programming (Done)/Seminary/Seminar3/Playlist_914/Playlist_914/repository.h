#pragma once
#include "DynamcVector.h"
#include "song.h"
class Repository {
private:
	DynamicVector<Song> songs;
public:
	void addSong(const Song& s);
	int getSize()const { return this->songs.length(); };

};
