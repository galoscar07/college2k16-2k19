#include "Repository.h"
#include <string>

using namespace std;

void Repository::addMovie(const Movie& m)
{
	this->movies.add(m);
}

void Repository::deleteMovie(const string& title)
{
	int pos = this->getPosOfMovie(title);
	if (pos != -1)
		//this->movies = this->movies - this->findByTitle(title);
		this->movies.remove(pos);
}

int Repository::getPosOfMovie(const string& title)
{
	Movie* moviesInDVector = this->movies.getAllElems();
	for (int i = 0; i < this->movies.getSize(); i++)
	{
		Movie m = moviesInDVector[i];
		if (m.getTitle() == title)
			return i;
	}

	return -1;
}

Movie Repository::findByTitle(const string& title)
{
	Movie* moviesInDVector = this->movies.getAllElems();
	if (moviesInDVector == NULL)
		return Movie{};
	for (int i = 0; i < this->movies.getSize(); i++)
	{
		Movie m = moviesInDVector[i];
		if (m == title)
			return m;
		/*if (m.getTitle() == title)
		return m;*/
	}

	return Movie{};
}

Repository Repository::getByGenre(const string& genre)
{
	Movie* v = this->movies.getAllElems();
	Repository movies;

	for (int i = 0; i < this->movies.getSize(); i++)
		if (v[i].getGenre() == genre)
			movies.addMovie(v[i]);
	return movies;
}

void Repository::updateGenre(int pos, const string& title, const string& newG)
{
	Movie m = this->findByTitle(title);
	Movie m1{ m.getTitle(), newG, m.getDuration(), m.getYear(), m.getLikes(), m.getTrailer() };
	this->movies.update(m1, pos);
}

void Repository::updateYear(int pos, const string& title, int newy)
{
	Movie m = this->findByTitle(title);
	Movie m1{ m.getTitle(), m.getGenre(), m.getDuration(), newy, m.getLikes(), m.getTrailer() };
	this->movies.update(m1, pos);
}

void Repository::updateLikes(int pos, const string& title, int newl)
{
	Movie m = this->findByTitle(title);
	Movie m1{ m.getTitle(), m.getGenre(), m.getDuration(), m.getYear(), newl, m.getTrailer() };
	this->movies.update(m1, pos);
}

void Repository::updateTrailer(int pos, const string& title, const string& newt)
{
	Movie m = this->findByTitle(title);
	Movie m1{ m.getTitle(), m.getGenre(), m.getDuration(), m.getYear(), m.getLikes(), newt };
	this->movies.update(m1, pos);

}

//Manage trailers------------------------------------------------

Repository::Repository()
{
	this->current = 0;
}

Movie Repository::getCurrentMovie()
{
	if (this->current == this->movies.getSize())
		this->current = 0;

	Movie* elems = this->movies.getAllElems();
	if (elems != NULL)
		return elems[this->current];
	return Movie{};
}

void Repository::play(const string& genre)
{
	if (this->movies.getSize() == 0)
		return;

	this->current = 0;
	//Movie currentMovie = this->getCurrentMovie();
	while (this->getCurrentMovie().getGenre() != genre)
		this->current++;
	Movie currentMovie = this->getCurrentMovie();
	currentMovie.play();
}

void Repository::next(const string& genre)
{
	if (this->movies.getSize() == 0)
		return;
	this->current++;
	//Movie currentMovie = this->getCurrentMovie();
	while (this->getCurrentMovie().getGenre() != genre)
		this->current++;
	Movie currentMovie = this->getCurrentMovie();
	currentMovie.play();
}

bool Repository::isEmpty()
{
	return this->movies.getSize() == 0;
}