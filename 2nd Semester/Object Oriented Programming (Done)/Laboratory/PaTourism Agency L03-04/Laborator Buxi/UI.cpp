#include "UI.h"
#include <string>

using namespace std;

void UI::modeMenu()
{
	cout << endl;
	cout << "*************************************************************************" << endl;
	cout << "Choose mode: " << endl;
	cout << "1 - Administrator mode" << endl;
	cout << "2 - User mode" << endl;
	cout << "0 - Exit" << endl;
	cout << "*************************************************************************" << endl;
}

void UI::adminMenu()
{
	cout << endl;
	cout << "*************************************************************************" << endl;
	cout << "1- Add a movie." << endl;
	cout << "2- Delete a movie." << endl;
	cout << "3- Update a movie." << endl;
	cout << "4- See all movies." << endl;
	cout << "0- Back" << endl;
	cout << "*************************************************************************" << endl;
}
void UI::userMenu()
{
	cout << "*************************************************************************" << endl;
	cout << "1- See watchlist." << endl;
	cout << "2- Delete from watchlist." << endl;
	cout << "3- See movies by genre." << endl;
	cout << "0- Back." << endl;
	cout << "*************************************************************************" << endl;
}

void UI::watchlistMenu()
{
	cout << endl;
	cout << "1- Add to watchlist." << endl;
	cout << "2- Next movie." << endl;
	cout << "0- Back." << endl;
}

void UI::printUpdateMenu()
{
	cout << endl;
	cout << "1- Update genre." << endl;
	cout << "2- Update year." << endl;
	cout << "3- Update number of likes." << endl;
	cout << "4- Update trailer source." << endl;
	cout << "0- Back" << endl;
}

int UI::validCommand(int com)
{
	if (com >= 0 && com <= 5)
		return 1;
	return 0;
}
void UI::addMovieToRepo()
{
	cout << "Enter title: ";
	std::string title;
	getline(cin, title);
	cout << "Enter genre: ";
	std::string genre;
	getline(cin, genre);
	int duration, year, likes;
	cout << "Enter duration: ";
	cin >> duration;
	cin.ignore();
	cout << "Enter year: ";
	cin >> year;
	cin.ignore();
	cout << "Enter number of likes: ";
	cin >> likes;
	cin.ignore();
	cout << "Trailer: ";
	std::string trailer;
	getline(cin, trailer);

	Movie m = this->ctrl.getRepo().findByTitle(title);
	if (m.getTitle() != "")
		cout << "Movie already exists in repository.";
	else
	{
		this->ctrl.addMovieToRepository(title, genre, duration, year, likes, trailer);
		cout << "Movie added successfuly.";
	}


}

void UI::deleteMovieFromRepo()
{
	cout << "Enter movie title: ";
	std::string title;
	getline(cin, title);

	Movie m = this->ctrl.getRepo().findByTitle(title);
	if (m.getTitle() == "")
		cout << "Movie does not exist in repository.";
	else
	{
		this->ctrl.deleteMovieFromRepository(title);
		cout << "Movie deleted successufly.";
	}
}

void UI::updateMovieGenre()
{
	cout << "Enter movie title: ";
	std::string title;
	getline(cin, title);

	Movie m = this->ctrl.getRepo().findByTitle(title);
	if (m.getTitle() == "")
		cout << "Movie does not exist in repository.";
	else
	{
		int pos = this->ctrl.getRepo().getPosOfMovie(title);
		cout << "Enter new genre: ";
		std::string newg;
		getline(cin, newg);
		this->ctrl.updateGenre(pos, title, newg);
		cout << "Movie updated successufly.";
	}
}

void UI::updateMovieYear()
{
	cout << "Enter movie title: ";
	std::string title;
	getline(cin, title);

	Movie m = this->ctrl.getRepo().findByTitle(title);
	if (m.getTitle() == "")
		cout << "Movie does not exist in repository.";
	else
	{
		int pos = this->ctrl.getRepo().getPosOfMovie(title);
		cout << "Enter new year: ";
		int newy;
		cin >> newy;
		cin.ignore();
		this->ctrl.updateYear(pos, title, newy);
		cout << "Movie updated successufly.";
	}

}

void UI::updateMovieLikes()
{
	cout << "Enter movie title: ";
	std::string title;
	getline(cin, title);

	Movie m = this->ctrl.getRepo().findByTitle(title);
	if (m.getTitle() == "")
		cout << "Movie does not exist in repository.";
	else
	{
		int pos = this->ctrl.getRepo().getPosOfMovie(title);
		cout << "Enter new number of likes: ";
		int newl;
		cin >> newl;
		cin.ignore();
		this->ctrl.updateLikes(pos, title, newl);
		cout << "Movie updated successufly.";
	}
}

void UI::updateMovieTrailer()
{
	cout << "Enter movie title: ";
	std::string title;
	getline(cin, title);

	Movie m = this->ctrl.getRepo().findByTitle(title);
	if (m.getTitle() == "")
		cout << "Movie does not exist in repository.";
	else
	{
		int pos = this->ctrl.getRepo().getPosOfMovie(title);
		cout << "Enter new trailer source: ";
		std::string trailer;
		getline(cin, trailer);
		this->ctrl.updateTrailer(pos, title, trailer);
		cout << "Movie updated successufly.";
	}
}
void UI::displayAllMoviesRepo()
{
	DynamicVector<Movie> v = this->ctrl.getRepo().getMovies();
	Movie* movies = v.getAllElems();
	if (movies == NULL)
		return;
	if (v.getSize() == 0)
	{
		cout << "There are no movies in the repository." << endl;
		return;
	}

	cout << "*************************************************************************" << endl;
	for (int i = 0; i < v.getSize(); i++)
	{
		Movie m = movies[i];
		cout << endl << m.getTitle() << "; Genre: " << m.getGenre() << "; Duration: " << m.getDuration() << "; Year: " << m.getYear() << "; Likes: " << m.getLikes() << endl;
	}

	cout << "*************************************************************************" << endl;
}

void UI::displayWatchlist()
{
	DynamicVector<Movie> v = this->ctrl.getWatchlist().getList();
	Movie* movies = v.getAllElems();
	if (movies == NULL)
		return;
	if (v.getSize() == 0)
	{
		cout << "There are no movies in the watchlist." << endl;
		return;
	}

	cout << "**************************************************************************" << endl;
	for (int i = 0; i < v.getSize(); i++)
	{
		Movie m = movies[i];
		cout << endl << m.getTitle() << "; Genre: " << m.getGenre() << "; Duration: " << m.getDuration() << "; Year: " << m.getYear() << "; Likes: " << m.getLikes() << endl;
	}
	cout << "**************************************************************************" << endl;
}

void UI::addMovieToWatchlist()
{
	Movie m = this->ctrl.getRepo().getCurrentMovie();
	Movie m2 = this->ctrl.getWatchlist().getByTitle(m.getTitle());

	if (m2.getTitle() != "")
		cout << "Movie already added." << endl;
	else
	{
		this->ctrl.addToWatchlist(m);
		cout << "Movie added successfuly.";
	}
}

void UI::deleteMovieFromWatchlist()
{
	cout << "Enter movie title:";
	std::string title;
	getline(cin, title);
	Movie m = this->ctrl.getWatchlist().getByTitle(title);

	if (m.getTitle() == "")
		cout << "This movie is not in the watchlist.";
	else
	{
		this->ctrl.deleteFromWatchlist(title);
		cout << endl << "Movie deleted successfuly." << endl;
	}

	cout << endl << "Rate movie? y/n: ";
	std::string rate;
	getline(cin, rate);

	if (rate == "y")
	{
		int pos = this->ctrl.getRepo().getPosOfMovie(title);
		this->ctrl.updateLikes(pos, title, m.getLikes() + 1);
	}
	else
		return;
}

void UI::run()
{
	while (true)
	{
		UI::modeMenu();
		int command;
		cout << "Choose mode: ";
		cin >> command;
		cin.ignore();

		if (command == 0)
			break;

		switch (command)
		{
		case 1: // administrator
		{
			while (true)
			{
				this->adminMenu();
				int command;
				cout << "Enter command: ";
				cin >> command;
				cin.ignore();

				if (command == 0)
					break;

				switch (command)
				{
				case 1:
				{
					this->addMovieToRepo();
					break;
				}
				case 4:
				{
					this->displayAllMoviesRepo();
					break;
				}
				case 2:
				{
					this->deleteMovieFromRepo();
					break;
				}
				case 3:
				{
					while (true)
					{
						this->printUpdateMenu();
						int cmd;
						cout << "Choose option: ";
						cin >> cmd;
						cin.ignore();

						if (cmd == 0)
							break;

						switch (cmd)
						{
						case 1:
						{
							this->updateMovieGenre();
							break;
						}

						case 2:
						{
							this->updateMovieYear();
							break;
						}

						case 3:
						{
							this->updateMovieLikes();
							break;
						}

						case 4:
						{
							this->updateMovieTrailer();
							break;
						}

						break;
						}
					}

				}
				}
			}
			break;
		}
		case 2: //user 
		{
			while (true)
			{
				UI::userMenu();
				int command;
				cout << "Enter command: ";
				cin >> command;
				cin.ignore();

				if (command == 0)
					break;

				switch (command)
				{
				case 1:
				{
					this->displayWatchlist();
					break;
				}

				case 2:
				{
					this->deleteMovieFromWatchlist();
					break;
				}

				case 3:
				{
					cout << "Enter genre (Comedy/Drama/Thriller/Animation/Adventure) : ";
					std::string genre;
					getline(cin, genre);
					if (this->ctrl.getRepo().isEmpty())
					{
						cout << "Nothing to show - the movie list is empty." << endl;
						continue;
					}
					this->ctrl.playTrailers(genre);
					Movie m = this->ctrl.getRepo().getCurrentMovie();
					cout << "Now viewing: " << m.getTitle() << " - " << m.getGenre() << " - " << m.getYear() << " ; " << m.getLikes() << " Likes" << endl;

					while (true)
					{
						this->watchlistMenu();
						cout << endl << "Enter command: ";
						int cmd;
						cin >> cmd;
						cin.ignore();

						if (cmd == 0)
							break;
						else if (cmd == 1)
							this->addMovieToWatchlist();
						else if (cmd == 2)
						{
							if (this->ctrl.getRepo().isEmpty())
							{
								cout << "Nothing to show - movie list is empty." << endl;
								continue;
							}
							this->ctrl.nextMovieTrailer(genre);
							Movie m = this->ctrl.getRepo().getCurrentMovie();
							cout << "Now viewing: " << m.getTitle() << " - " << m.getGenre() << " - " << m.getYear() << " ; " << m.getLikes() << " Likes" << endl;
						}
					}

					break;
				}
				break;
				}
			}
			break;
		}
		}
	}
}