#pragma once
#include "Song.h"
#include <vector>

class Repository
{
protected:
	std::vector<Song> songs;

public:
	Repository() {}

	/*
		Constructor with parameters. 
		Initializes an object of type repository, by reading data from the given file.
		Throws: FileException - if the file cannot be opened.
	*/
	Repository(const std::string& filename);

	virtual ~Repository() {};

	/*
		Adds a song to the repository.
		Input: s - Song.
		Output: the song is added to the repository.
		Throws: FileException - if the file cannot be opened.
	*/
	virtual void addSong(const Song& s);

	/*
		Finds a song, by artist and title.
		Input: artist, title - string
		Output: the song that was found, or an "empty" song (all fields empty and duration 0), if nothing was found.
	*/
	Song findByArtistAndTitle(const std::string& artist, const std::string& title) const;

	std::vector<Song> getSongs() const { return songs; }
};

class FileRepository : public Repository {
private: 
	std::string file_name;

	void load_from_file();
public:
	FileRepository(const std::string&);

	void write_to_file();

	void addSong(const Song& s) override;

};

class RepositoryException : public std::exception
{
private:
	std::string message;

public:
	const char* what() { return message.c_str(); }
};