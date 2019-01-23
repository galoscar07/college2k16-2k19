#include "Song.h"
#include "LocalSong.h"
#include "YoutubeSong.h"
#include <iostream>
#include <Windows.h>
#include <crtdbg.h>
#include <vector>

using namespace std;

int main()
{
	system("color f4");

	{
	Song *s1 = new YoutubeSong{ "Pink Martini","Splendor in the grass",Duration{3,40},"http://www.youtube.com" };
	Song *s2 = new LocalSong{ "Ed Sheeran", "I see fire",Duration{3,40},"\"C:\\Users\\Iuliana\\Desktop\\I am The Doctor.mp3\"",3 };

	vector<Song*> songs{ s1, s2 };

	Song* s3 = new YoutubeSong{ "La la land","La la land",Duration{ 3,40 },"http://www.youtube.com" };
	songs.push_back(s3);

	/*for (Song* s : songs)
		s->play();*/

		/*for (auto it = songs.begin(); it != songs.end(); it++)
			(*it)->play();*/

	delete s1;
	delete s2;
	delete s3;
	}

	system("pause");

	_CrtDumpMemoryLeaks();

	return 0;
}