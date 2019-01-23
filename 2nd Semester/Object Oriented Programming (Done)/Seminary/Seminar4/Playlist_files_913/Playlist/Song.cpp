#include "Song.h"
#include <Windows.h>
#include <shellapi.h>
#include "Utils.h"
#include <vector>

using namespace std;

Song::Song(): title(""), artist(""), duration(Duration()), source("") {}

Song::Song(const std::string& artist, const std::string& title, const Duration& duration, const std::string& source)
{
	this->artist = artist;
	this->title = title;
	this->duration = duration;
	this->source = source;
}

void Song::play()
{
	ShellExecuteA(NULL, NULL, "chrome.exe", this->getSource().c_str(), NULL, SW_SHOWMAXIMIZED);
}

istream & operator>>(istream & is, Song & s)
{
	string line;
	getline(is, line);
	vector<string> tokens = tokenize(line, ',');
	if (tokens.size() != 4)
		return is;
	s.title = tokens[0];
	s.artist = tokens[1];
	vector<string> dur = tokenize(tokens[2], ':');
	s.duration = Duration{stod(dur[0]),stod(dur[1])};
	s.source = tokens[3];
	return is;
}

ostream & operator<<(ostream & os,const Song & s)
{
	os << s.title << "," << s.artist << "," << s.duration.getMinutes() << ":" << s.duration.getSeconds() << "," << s.source << endl;
	return os;
}
