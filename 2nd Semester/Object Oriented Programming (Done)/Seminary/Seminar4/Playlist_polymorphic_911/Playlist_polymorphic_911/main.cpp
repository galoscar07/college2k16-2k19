#include <iostream>
#include "Song.h"
#include "LocalSong.h"
#include <Windows.h>
#include <vector>
#include "YoutubeSong.h"

using namespace std;

int main()
{
	system("color f4");

	Song* s1 = new YoutubeSong{ "Ed Sheeran", "I see fire", Duration{3, 40}, "www.youtube.com" };
	cout << s1->toString()<< "\n";
	Song* s2 = new LocalSong{ "Doctor Who Theme Song", "Doctor Who", Duration{ 4, 20 }, "C:\\Users\\song.mp3", 100 };
	cout << s2->toString();
	
	vector<Song*> songs{s1, s2};
	/*for (vector<Song*>::iterator it = songs.begin(); it != songs.end(); it++)
		(*it)->play();*/
		
	delete s1;
	delete s2;

	system("pause");

	return 0;
}