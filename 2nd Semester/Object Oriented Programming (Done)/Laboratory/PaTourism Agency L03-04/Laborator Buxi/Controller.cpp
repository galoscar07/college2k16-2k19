#include "Controller.h"

void Controller::addMovieToRepository(const std::string& title, const std::string& genre, int duration, int year, int likes, const std::string& trailer)
{
	Movie m = Movie(title, genre, duration, year, likes, trailer);
	this->repo.addMovie(m);
}

void Controller::deleteMovieFromRepository(const std::string& title)
{
	this->repo.deleteMovie(title);
}

void Controller::updateGenre(int pos, const std::string& title, const std::string& newG)
{
	this->repo.updateGenre(pos, title, newG);
}

void Controller::updateYear(int pos, const std::string& title, int newy)
{
	this->repo.updateYear(pos, title, newy);
}

void Controller::updateLikes(int pos, const std::string& title, int newl)
{
	this->repo.updateLikes(pos, title, newl);
}

void Controller::updateTrailer(int pos, const std::string& title, const std::string& newt)
{
	this->repo.updateTrailer(pos, title, newt);
}

Repository Controller::returnByGenre(const std::string& genre)
{
	return this->repo.getByGenre(genre);
}

void Controller::playTrailers(const std::string& genre)
{
	this->repo.play(genre);
}

void Controller::nextMovieTrailer(const std::string& genre)
{
	this->repo.next(genre);
}

void Controller::addToWatchlist(const Movie& m)
{
	this->list.addToList(m);
}

void Controller::deleteFromWatchlist(const std::string& title)
{
	this->list.removeFromList(title);
}