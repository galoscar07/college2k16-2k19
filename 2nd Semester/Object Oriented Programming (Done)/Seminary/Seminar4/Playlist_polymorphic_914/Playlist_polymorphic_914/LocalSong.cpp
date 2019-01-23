#include "LocalSong.h"
#include <Windows.h>

LocalSong::LocalSong(const string& artist, const string& title, const Duration& duration, const string& source, unsigned int fileSize) : Song{artist, title, duration, source}
{
	this->fileSize = fileSize;
}

string LocalSong::toString() const {
	string str;

	str = Song::toString();
	str += "Filesize: " + to_string(fileSize) + " bytes\n";

	return str;
}

void LocalSong::play() const
{
	ShellExecuteA(NULL, NULL, "C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe", this->source.c_str(), NULL, SW_SHOWMAXIMIZED);
}
