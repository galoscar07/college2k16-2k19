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

FileRepository::FileRepository(const std::string & filename) :Repository{}
{
	this->filename = filename;
	this->ReadFromfile();
}

void FileRepository::WriteToFile()
{
	ofstream of{ this->filename };
	if (!of.is_open()) return;

	for (Song s : this->songs)
		of << s;
}

void FileRepository::ReadFromfile()
{
	ifstream ifs{ this->filename };
	if (!ifs.is_open()) return;
	Song s;
	while (ifs >> s)
	{
		this->addSong(s);
	}
	ifs.close();
}

void FileRepository::addSong(const Song & s)
{
	Repository::addSong(s);
	WriteToFile();
}
