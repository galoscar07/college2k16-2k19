#include "Movie.h"
#include <Windows.h>
#include <shellapi.h>

Movie::Movie() : title(""), genre(""), duration(int()), year(int()), likes(int()), trailer("") {}


Movie::Movie(const Movie& m)
{
	this->title = m.title;
	this->genre = m.genre;
	this->duration = m.duration;
	this->year = m.year;
	this->likes = m.likes;
	this->trailer = m.trailer;
}

Movie::Movie(const std::string & title, const std::string & genre, int duration, int year, int likes, const std::string trailer)
{
	this->title = title;
	this->genre = genre;
	this->duration = duration;
	this->year = year;
	this->likes = likes;
	this->trailer = trailer;
}

//void Movie::setGenre(std::string& newg)
//{
//	this->genre = newg;
//}
void Movie::play()
{
	ShellExecuteA(NULL, NULL, "chrome.exe", this->getTrailer().c_str(), NULL, SW_SHOWMAXIMIZED);
}