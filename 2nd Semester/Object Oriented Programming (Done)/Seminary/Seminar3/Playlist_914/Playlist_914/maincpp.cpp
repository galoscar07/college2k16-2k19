#include "song.h"
#include "DynamcVector.h"
#include <assert.h>
#include "controller.h"
void testSong() {
	Song s{ "Ed Sheeran","I see fire",300,"link" };
	assert(s.getArtist() == "Ed Sheeran");
	
}

void testDynamicVector() {
	DynamicVector<Song> songs{};
	songs.add(Song{ "Ed Sheeran", "I see fire", 300, "link" });
	songs.add(Song{ "Rihanna", "Love on the brain", 320, "link" });
	assert(songs.length() == 2);

	DynamicVector<Song> v{};
	v = songs;
}
void testController()
{
	Repository r;
	//r.addSong(Song{ "Ed Sheeran", "I see fire", 300, "link" });
	//r.addSong(Song{ "Rihanna", "Love on the brain", 320, "link" });
	Controller control{ r };
	control.addSong(Song{ "Ed Sheeran", "I see fire", 300, "link" });
	control.addSong(Song{ "Rihanna", "Love on the brain", 320, "link" });
	assert(r.getSize() == 2);
}

int main() {
	testSong();
	testDynamicVector();
	testController();
	return 0;
}