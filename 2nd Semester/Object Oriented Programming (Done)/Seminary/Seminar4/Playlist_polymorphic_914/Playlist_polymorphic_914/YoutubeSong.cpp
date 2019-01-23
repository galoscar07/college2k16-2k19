#include "YoutubeSong.h"
#include <Windows.h>

YoutubeSong::YoutubeSong(const std::string& artist, const std::string& title, const Duration& duration, const std::string& source) : Song{artist, title, duration, source}
{
}

void YoutubeSong::play() const
{
	ShellExecuteA(NULL, NULL, "chrome.exe", this->source.c_str(), NULL, SW_SHOWMAXIMIZED);
}
