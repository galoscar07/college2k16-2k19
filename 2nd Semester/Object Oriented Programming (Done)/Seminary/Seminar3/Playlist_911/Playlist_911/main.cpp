#include"Song.h"
#include "DynamicVector.h"
#include<assert.h>

void testSong()
{
	Song s{ "Title","Artist",100,"www.youtube.com" };
	assert(s.getTitle() == "Title");
	//s.play();
}

void testDynamicVector()
{
	DynamicVector<Song> songs{ 1 };
	Song s1{"Title1","Artist1",10,"www.youtube.com"};
	Song s2{ "Title2","Artist2",15,"www.youtube.com" };
	songs.AddElem(s1);
	songs.AddElem(s2);
	assert(songs.getSize() == 2);

	DynamicVector<Song> v{};
	v = songs;

}

int main()
{
	testSong();
	testDynamicVector();

	return 0;
}

