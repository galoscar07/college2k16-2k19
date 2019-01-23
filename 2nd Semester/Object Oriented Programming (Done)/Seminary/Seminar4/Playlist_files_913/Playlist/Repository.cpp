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

void FileRepository::load_from_file()
{
	ifstream fin{ this->file_name };
	if (!fin.is_open())
		return;
	Song new_song;
	while (fin >> new_song)
		this->addSong(new_song);
	fin.close();
}

FileRepository::FileRepository(const std::string & file_name) : Repository{}
{
	this->file_name = file_name;
	this->load_from_file();
}

void FileRepository::write_to_file()
{
	ofstream fout{ this->file_name };
	for (Song& song : this->songs)
		fout << song;
}

void FileRepository::addSong(const Song & s)
{
	Repository::addSong(s);
	this->write_to_file();
}
