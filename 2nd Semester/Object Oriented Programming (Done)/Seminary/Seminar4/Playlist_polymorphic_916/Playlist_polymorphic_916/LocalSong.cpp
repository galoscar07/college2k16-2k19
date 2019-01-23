#include "LocalSong.h"
#include <string>
#include <sstream>
#include <Windows.h>

using namespace std;

LocalSong::LocalSong(const std::string& artist, 
	const std::string& title, const Duration& duration, 
	const std::string& source, double size): 
	Song{artist, title, duration, source}, fileSize{size}
{
}

std::string LocalSong::toString() const
{
	stringstream s;
	string old_song = Song::toString();
	s << old_song << " size: " << this->fileSize << '\n';
	return s.str();
	//s << this->artist << " - " << this->title << ", " << this->duration.getMinutes() << ":" << this->duration.getSeconds()<<" size: "<<this->file
}

void LocalSong::play() const
{
	ShellExecuteA(NULL, NULL, "C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe", this->source.c_str(), NULL, SW_SHOWMAXIMIZED);
}
