#include "Controller.h"
#include <algorithm>

using namespace std;

void Controller::addSongToRepository(const std::string& artist, const std::string& title, double minutes, double seconds, const std::string& source)
{
	Song s{ artist, title, Duration{minutes, seconds}, source };
	this->repo.addSong(s);
}

void Controller::addSongToPlaylist(const Song& song)
{
	this->playList.add(song);
}

void Controller::addAllSongsByArtistToPlaylist(const std::string& artist)
{
	vector<Song> songs = this->repo.getSongs();
	int nSongs = count_if(songs.begin(), songs.end(),
		[artist](const Song& s)
		{
			return s.getArtist() == artist;
		});

	vector<Song> songsByArtist(nSongs);
	copy_if(songs.begin(), songs.end(), songsByArtist.begin(),
		[artist](const Song& s)
		{
			return s.getArtist() == artist;
		});

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

void Controller::savePlaylist(const std::string& filename)
{
}

void Controller::openPlaylist() const
{
}
