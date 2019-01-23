#include <Windows.h>
#include "Song.h"
#include "LocalSong.h"
#include "YoutubeSong.h"
#include <crtdbg.h>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

	{
		Song* s1 = new YoutubeSong{ "Ed Sheeran", "I see fire", Duration{3, 40}, "www.youtube.com" };
		Song* s2 = new LocalSong{ "Doctor Who", "Doctor Who Theme", Duration{10, 0}, "\"C:\\Users\\Iuliana\\Desktop\\I am The Doctor.mp3\"", 10 };
		Song* s3 = new YoutubeSong{ "La la Land", "La la Land", Duration{10,10}, "www.google.com" };

		vector<Song*> songs{ s1, s2 };
		songs.push_back(s3);

		/*for (vector<Song*>::iterator it = songs.begin(); it != songs.end(); it++)
			(*it)->play();*/

		string a = "Ed Sheeran";
		int res = count_if(songs.begin(), songs.end(), [a](Song* s) { return s->getArtist() == a; });

		delete s1;
		delete s2;
		delete s3;
	}

	_CrtDumpMemoryLeaks();

	system("pause");
	return 0;
}