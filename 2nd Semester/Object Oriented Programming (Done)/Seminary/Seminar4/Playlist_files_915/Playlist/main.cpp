#include "UI.h"
#include <Windows.h>
#include "SongValidator.h"
#include <iostream>
#include <string>

using namespace std;

int main()
{
	system("color f4");

	Song s{ "Ed Sheeran", "I see fire", Duration{4, 54}, "https ://www.youtube.com/watch?v=2fngvQS_PmQ" };
	cout << s;

	Song s2{};
	cin >> s2;

	try
	{
		SongValidator::validate(s2);
	}
	catch (SongException& ex)
	{
		for (auto e: ex.getErrors())
			cout << e;
	}

	cout << s2;
	Repository *newRepo = new FileRepository{"Songs.txt"};
	newRepo->addSong(s2);
	FileRepository* fr = dynamic_cast<FileRepository*>(newRepo);
	if (fr != nullptr)
		fr->writeToFile();

	delete newRepo;

	system("pause");

	return 0;
}