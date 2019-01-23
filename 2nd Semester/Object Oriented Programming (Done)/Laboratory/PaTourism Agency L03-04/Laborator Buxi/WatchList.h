#pragma once
#include "DynamicVector.h"
#include "Movie.h"

class WatchList
{
private:
	DynamicVector<Movie> movies;

public:
	WatchList() {};

	//adds a movie to the watchlist
	void addToList(const Movie& m);

	//removes a movie from the watchlist
	void removeFromList(const std::string& title);

	//returns the movie with the given title
	Movie getByTitle(const std::string& title);

	int posOfMovie(const std::string& title);

	//returns all the movies from the watchlist
	DynamicVector<Movie> getList() { return movies; }

};