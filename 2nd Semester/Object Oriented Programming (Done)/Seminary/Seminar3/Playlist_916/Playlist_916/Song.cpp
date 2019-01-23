#include"Song.h"
#include<Windows.h>
Song::Song(const std::string& artist, const std::string& title, int duration, const std::string& link)
{
	this->artist = artist;
	this->title = title;
	this->duration = duration;
	this->link = link;
}

Song::Song()
{
	this->artist = "";
	this->title = "";
	this->duration = 0;
	this->link = "";
}

void Song::play()
{
	ShellExecuteA(NULL, NULL, "chrome.exe", this->link.c_str(), NULL, SW_SHOWMAXIMIZED);
}