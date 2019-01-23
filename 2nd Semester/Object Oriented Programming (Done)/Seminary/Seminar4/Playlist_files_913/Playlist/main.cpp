#include "UI.h"
#include <Windows.h>
#include "SongValidator.h"
#include <string>
using namespace std;

int main()
{
	system("color f4");

	Song s{ "aa","bb",Duration{2,10},"link" };
	cout << s;
	Song s2{};
	cin >> s2;
	cout << s2;

	Repository* repo = new FileRepository{ "Songs.txt" };
	FileRepository* fileRepo = dynamic_cast<FileRepository*>(repo);
	if (fileRepo != nullptr)
		fileRepo->write_to_file();

	Song s3{};
	cin >> s3;
	try 
	{
		SongValidator::validate(s3);
	}
	catch (SongException &e) {
		for (std::string s : e.get_errors()) {
			cout << s << "\n";
		}
	}
	system("pause");

	return 0;
}