#pragma once
#include "Controller.h"

class UI
{
private:
	Controller ctrl;

public:
	UI(Controller& c) : ctrl(c) {}

	void run();

private:
	static void adminMenu();
	static void printUpdateMenu();
	static void modeMenu();
	static void userMenu();
	static void watchlistMenu();
	int validCommand(int com);

	void addMovieToRepo();
	void deleteMovieFromRepo();
	void displayAllMoviesRepo();

	void updateMovieGenre();
	void updateMovieYear();
	void updateMovieLikes();
	void updateMovieTrailer();

	void displayWatchlist();
	void addMovieToWatchlist();
	void deleteMovieFromWatchlist();
	void rateMovie();
};