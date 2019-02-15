#pragma once
#include <vector>
#include "Song.h"

class PlayList
{
private:
	std::vector<Song*> songs;
	int current;

public:
	PlayList();

	// Adds a song to the playlist.
	void add(Song* song);

	// Returns the song that is currently playing.
	Song* PlayList::getCurrentSong();

	// Starts the playlist - plays the first song.
	void play();

	// Plays the next song in the playlist.
	void next();

	// Checks if the playlist is empty.
	bool isEmpty();
};

