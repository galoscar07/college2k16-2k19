#include "UI.h"
#include <Windows.h>
#include "Validator.h"

using namespace std;


int main()
{
	system("color f4");

	Song s{ "Hozier", "Take me to church", Duration{4, 2}, "www" };
	cout << s;

	Song s2;
	cin >> s2;
	cout << s2;

	std::string str{ "AA" };
	cout << str;

	FileRepository r{ "Songs.txt" };
	r.addSong(s2);
	
	Song s3;
	cin >> s3;
	try
	{
		SongValidator::Validate(s3);
	}
	catch (SongException& ex)
	{
		for (string s : ex.GetError())
		{
			cout << s<<endl;

		}
	}

	system("pause");
	
	return 0;
}