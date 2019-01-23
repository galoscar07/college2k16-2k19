#include "Validator.h"

using namespace std;

void SongValidator::Validate(const Song& s)
{
	vector <string> errors;
	if (s.getArtist().size() < 2)
	{
		errors.push_back("Artist invalid");
	}
	if (s.getTitle().size() < 2)
	{
		errors.push_back("Invalid Title");
	}
	if (errors.size() > 0)
	{
		throw SongException{ errors };
	}
}