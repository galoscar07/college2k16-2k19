#include "SongValidator.h"






void SongValidator::validate(const Song & s)
{
	std::vector<std::string> errors{};
	if (s.getArtist().size() < 2)
		errors.push_back("Artist invalid");
	if (s.getTitle().size() < 2)
		errors.push_back("Title invalid");

	if (errors.size() > 0)
		throw SongException(errors);
}
