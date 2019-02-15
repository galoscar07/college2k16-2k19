#pragma once
#include "Song.h"
#include <vector>

class Repository
{
private:
	std::vector<Song*> songs;
	std::string filename;

public:
	Repository() {}

	// Copy constructor - is needed, as the Repository contains a vector of pointers.
	Repository(const Repository& r);

	// Destructor - will deallocate the memory allocated when adding songs to the vector of pointers.
	~Repository();

	/*
		Adds a song to the repository.
		Input: s - Song.
		Output: the song is added to the repository.
	*/
	void addSong(Song* s);

	/*
		Finds a song, by artist and title.
		Input: artist, title - string
		Output: the song that was found, or null pointer, if nothing was found.
	*/
	Song* findByArtistAndTitle(const std::string& artist, const std::string& title);

	std::vector<Song*> getSongs() const { return songs; }
};