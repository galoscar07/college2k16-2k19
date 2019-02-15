#include "Controller.h"
#include "YoutubeSong.h"
#include "LocalSong.h"
#include <algorithm>
#include <iterator>

using namespace std;

void Controller::addSongToRepository(const string& type, const string& artist, const string& title, double minutes, double seconds, const string& source, double size)
{
	// create a new song, with the given type and information
	Song* s = nullptr;
	if (type == "youtubeSong")
		s = new YoutubeSong(artist, title, Duration(minutes, seconds), source);
	else
		s = new LocalSong(artist, title, Duration(minutes, seconds), source, size);
	this->repo.addSong(s);

	// after the song was added to the repository, it can be deleted
	delete s;
}

void Controller::addSongToPlaylist(Song* song)
{
	this->playList.add(song);
}

void Controller::addAllSongsByArtistToPlaylist(const std::string& artist)
{
	// get all the songs from the repository
	vector<Song*> v = this->repo.getSongs();
	vector<Song*> songsByArtist;
	copy_if(v.begin(), v.end(), back_inserter(songsByArtist), [artist](Song* s) { return s->getArtist() == artist; });
	for (auto s : songsByArtist)
		this->playList.add(s);
}

void Controller::startPlaylist()
{
	this->playList.play();
}

void Controller::nextSongPlaylist()
{
	this->playList.next();
}