#include "Repository.h"
#include <string>
#include <fstream>
#include "Utils.h"

using namespace std;

Repository::Repository(const std::string& filename)
{
}

void Repository::addSong(const Song& s)
{
	this->songs.push_back(s);
}

Song Repository::findByArtistAndTitle(const std::string& artist, const std::string& title) const
{
	for (auto s: this->songs)
	{
		if (s.getArtist() == artist && s.getTitle() == title)
			return s;
	}

	return Song{};
}

FileRepository::FileRepository(const std::string & fn) : filename { fn }
{
	this->readFromFile();
}

void FileRepository::writeToFile()
{
	ofstream f{ this->filename };

	if (!f.is_open())
		return;

	for (auto s : this->songs)
		f << s;

	f.close();
}

void FileRepository::readFromFile()
{
	Song s;
	ifstream g{ this->filename };
	if (!g.is_open())
		return;
	while (g >> s)
	{
		this->songs.push_back(s);
	}
	g.close();
}
