#include "Repository.h"
#include <string>
#include <algorithm>
#include "Utils.h"
#include "YoutubeSong.h"
#include "LocalSong.h"

using namespace std;

Repository::Repository(const Repository& r)
{
	for (auto s : r.songs)
		this->songs.push_back(s->clone());
}

Repository::~Repository()
{
	for (auto s : this->songs)
		delete s;
}

void Repository::addSong(Song* s)
{
	// create a clone of the song (allocate memory and copy the song) and add this to the repository
	Song* song = s->clone();
	this->songs.push_back(song);
}

Song* Repository::findByArtistAndTitle(const std::string& artist, const std::string& title)
{
	auto it = find_if(this->songs.begin(), this->songs.end(), [artist, title](Song* s) {return (s->getArtist() == artist && s->getTitle() == title); });
	if (it != songs.end())
		return *it;
	return nullptr;
}