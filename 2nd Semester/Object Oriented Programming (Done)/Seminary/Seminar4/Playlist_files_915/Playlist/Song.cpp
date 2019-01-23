#include "Song.h"
#include <Windows.h>
#include <shellapi.h>
#include "Utils.h"
#include <iostream>
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

	vector<string> result = tokenize(line, ',');
	if (result.size() != 4)
		return is;

	s.artist = result[0];
	s.title = result[1];
	vector<string> res = tokenize(result[2], ':');
	s.duration.setMinutes(std::stod(res[0]));
	s.duration.setSeconds(std::stod(res[1]));

	s.source = result[3];
	return is;
}

ostream& operator<<(ostream & os, const Song & s)
{
	os << s.artist << "," << s.title << "," << s.duration.getMinutes() << ":" << s.duration.getSeconds() << "," << s.source << "\n";
	return os;
}
