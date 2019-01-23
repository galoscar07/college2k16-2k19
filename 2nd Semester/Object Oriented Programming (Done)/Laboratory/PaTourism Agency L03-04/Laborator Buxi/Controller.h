#pragma once
#include "Repository.h"
#include "WatchList.h"

class Controller
{
private:
	Repository repo;
	WatchList list;

public:
	Controller(const Repository& r) : repo(r) {}

	Repository getRepo() const { return repo; }
	WatchList getWatchlist() const { return list; }

	//adds a movie with the given data to the movie repo
	void addMovieToRepository(const std::string& title, const std::string& genre, int duration, int year, int likes, const std::string& trailer);

	//removes a movie with the given title from the repo
	void deleteMovieFromRepository(const std::string& title);

	//updates movie info
	void updateGenre(int pos, const std::string& title, const std::string& newG);
	void updateYear(int pos, const std::string& title, int newY);
	void updateLikes(int pos, const std::string& title, int newL);
	void updateTrailer(int pos, const std::string& title, const std::string& newT);

	Repository returnByGenre(const std::string& genre);
	void playTrailers(const std::string& genre);
	void nextMovieTrailer(const std::string& genre);

	void addToWatchlist(const Movie& m);
	void deleteFromWatchlist(const std::string& title);

}; 
