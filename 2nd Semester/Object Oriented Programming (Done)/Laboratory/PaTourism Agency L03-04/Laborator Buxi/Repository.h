#pragma once
#include"Movie.h"
#include "DynamicVector.h"

class Repository
{
private:
	DynamicVector<Movie> movies;
	int current;

public:
	Repository();

	void addMovie(const Movie& m);
	void deleteMovie(const std::string& title);

	Movie findByTitle(const std::string& title);
	int getPosOfMovie(const std::string& title);
	Repository getByGenre(const std::string& genre);

	void updateGenre(int pos, const std::string& title, const std::string& newG);
	void updateYear(int pos, const std::string& title, int newy);
	void updateLikes(int pos, const std::string& title, int newl);
	void updateTrailer(int pos, const std::string& title, const std::string& newt);

	DynamicVector<Movie> getMovies() { return movies; }
	int getCurrent() { return current; }

	//Manage trailers---------------------------------------------

	Movie getCurrentMovie();

	//Plays the first trailer
	void play(const std::string& genre);

	//PLays the next trailer
	void next(const std::string& genre);

	//checks if the movie list is empty
	bool isEmpty();
};