#include "UI.h"
#include <Windows.h>
#include "LocalSong.h"

using namespace std;

int main()
{
	system("color f4");

	// _CrtDumpMemoryLeaks is frequently called at the end of program execution to verify that all memory allocated by the application has been freed. 
	// The function can be called automatically at program termination by turning on the _CRTDBG_LEAK_CHECK_DF bit field of the _crtDbgFlag flag using the _CrtSetDbgFlag function.
	// (https://msdn.microsoft.com/en-us/library/d41t22sb.aspx)
	int flag = _CrtSetDbgFlag(_CRTDBG_REPORT_FLAG);
	flag |= _CRTDBG_LEAK_CHECK_DF;
	_CrtSetDbgFlag(flag);

	Repository repo;
	Controller ctrl(repo);
	ctrl.addSongToRepository("youtubeSong", "Ed Sheeran", "I see fire", 4, 54, "https://www.youtube.com/watch?v=2fngvQS_PmQ");
	ctrl.addSongToRepository("youtubeSong", "The Proclaimers", "I would walk 500 miles", 3, 37, "https://www.youtube.com/watch?v=otXGqU4LBEI");
	ctrl.addSongToRepository("localSong", "Doctor Who", "I am the Doctor", 3, 55, "\"C:\\Users\\Iuliana\\Desktop\\I am The Doctor.mp3\"", 3.62);

	UI ui(ctrl);
	ui.run();
	
	return 0;
}