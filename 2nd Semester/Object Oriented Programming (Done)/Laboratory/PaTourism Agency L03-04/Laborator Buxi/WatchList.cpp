#include "WatchList.h"

using namespace std;

void WatchList::addToList(const Movie& m)
{
	this->movies.add(m);
}

void WatchList::removeFromList(const string& title)
{
	int pos = this->posOfMovie(title);
	if (pos != -1)
		this->movies.remove(pos);
}

int WatchList::posOfMovie(const string& title)
{
	Movie* moviesInList = this->movies.getAllElems();
	for (int i = 0; i < this->movies.getSize(); i++)
	{
		Movie m = moviesInList[i];
		if (m.getTitle() == title)
			return i;
	}

	return -1;
}

Movie WatchList::getByTitle(const string& title)
{
	Movie* movies = this->movies.getAllElems();
	if (movies == NULL)
		return Movie{};
	for (int i = 0; i < this->movies.getSize(); i++)
	{
		Movie m = movies[i];
		if (m == title)
			return m;
	}

	return Movie{};
}