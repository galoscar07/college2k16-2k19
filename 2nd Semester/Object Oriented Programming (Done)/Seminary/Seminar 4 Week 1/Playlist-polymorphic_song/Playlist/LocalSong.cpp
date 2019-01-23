#include "LocalSong.h"
#include <Windows.h>
#include <sstream>

using namespace std;

LocalSong::LocalSong(const std::string& artist, const std::string& title, const Duration& duration, const std::string& source, double fileSize) : Song(artist, title, duration, source)
{
	this->fileSize = fileSize;
}

void LocalSong::play() const
{
	ShellExecuteA(NULL, NULL, "C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe", this->getSource().c_str(), NULL, SW_SHOWMAXIMIZED);
}

string LocalSong::toString() const
{
	stringstream s;
	s << "Size: " << this->fileSize << " MB." << endl;
	return Song::toString() + s.str();
}

Song* LocalSong::clone() const
{
	return new LocalSong(*this);
}
