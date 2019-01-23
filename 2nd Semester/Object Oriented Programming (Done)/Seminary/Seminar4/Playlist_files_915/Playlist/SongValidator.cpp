#include "SongValidator.h"


void SongValidator::validate(const Song & s)
{
	std::vector<std::string> errors;

	if (s.getArtist().size() < 2)
		errors.push_back("Artist length must be > 2!");
	if (s.getTitle().size() < 2)
		errors.push_back("Title length must be > 2!");

	if (errors.size() > 0)
		throw SongException{ errors };
}
