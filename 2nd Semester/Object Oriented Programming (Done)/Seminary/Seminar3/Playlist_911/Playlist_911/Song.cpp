#include"Song.h"
#include <Windows.h>

Song::Song(const std::string &title, const std::string &artist, int duration, const std::string &source)
{
	this->title = title;
	this->artist = artist;
	this->duration = duration;
	this->source = source;
}

void Song::play()
{
	ShellExecuteA(NULL, NULL, "chrome.exe", this->source.c_str(), NULL, SW_SHOWMAXIMIZED);
}

Song::Song()
{
	this->title = "";
	this->artist = "";
	this->duration = 0;
	this->source = "";
}
