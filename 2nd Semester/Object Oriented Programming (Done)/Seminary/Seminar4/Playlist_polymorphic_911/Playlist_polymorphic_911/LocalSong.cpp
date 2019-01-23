#include "LocalSong.h"
#include <Windows.h>

LocalSong::LocalSong()
{

}

LocalSong::LocalSong(const std::string & artist, const std::string & title, const Duration & duration, const std::string & source, const int file_size) : 
	Song{ artist, title, duration, source }, file_size{file_size} //only uses copy constructor
{
}

std::string LocalSong::toString() const
{
	return Song::toString() + " " + std::to_string(file_size);
}

void LocalSong::play() const
{
	ShellExecuteA(NULL, NULL, "C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe", this->source.c_str(), NULL, SW_SHOWMAXIMIZED);
}
