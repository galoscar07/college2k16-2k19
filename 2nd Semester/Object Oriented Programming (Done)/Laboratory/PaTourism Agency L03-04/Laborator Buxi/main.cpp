#include "Movie.h"
#include "UI.h"
//#include <Windows.h>

using namespace std;

int main(){
	//system("color 2");

	Repository repo{};
	Controller ctrl{ repo };

	ctrl.addMovieToRepository( "The Circle", "Drama", 121, 2017, 83,"http://www.imdb.com/video/imdb/vi3222058521?playlistId=tt4287320&ref_=tt_ov_vi" );
	ctrl.addMovieToRepository( "How to Be a Latin Lover", "Comedy", 114, 2017, 100, "http://www.imdb.com/video/imdb/vi3479680537?playlistId=tt4795124&ref_=tt_ov_vi" );
	ctrl.addMovieToRepository( "The Promise","Drama", 133, 2016, 93, "http://www.imdb.com/video/imdb/vi4201100825?playlistId=tt4776998&ref_=tt_ov_vi" );
	ctrl.addMovieToRepository( "The Accountant","Crime", 125, 2016, 100, "http://www.imdb.com/title/tt2140479/videoplayer/vi2433726233?ref_=tt_ov_vi" );
	ctrl.addMovieToRepository( "The Cube","Thriller", 90, 1997, 100, "https://www.youtube.com/watch?v=Esjc0rPj3K4" );
	ctrl.addMovieToRepository( "We're the Millers","Comedy", 98, 2014, 80, "http://www.imdb.com/video/imdb/vi544319001?playlistId=tt1723121&ref_=tt_ov_vi" );
	ctrl.addMovieToRepository( "The Notebook","Drama", 105, 2004, 96, "https://www.youtube.com/watch?v=FC6biTjEyZw" );
	ctrl.addMovieToRepository( "Life of Pi","Adventure", 87, 2011, 65, "http://www.imdb.com/video/imdb/vi2646320921?playlistId=tt0454876&ref_=tt_ov_vi" );
	ctrl.addMovieToRepository( "The Revenant","Adventure", 95, 2015, 95, "http://www.imdb.com/title/tt1663202/videoplayer/vi3857035801?ref_=tt_ov_vi" );
	ctrl.addMovieToRepository( "Inside Out","Animation", 101, 2015, 78, "http://www.imdb.com/video/imdb/vi203730969?playlistId=tt2096673&ref_=tt_ov_vi" );
	UI ui{ ctrl };
	ui.run();
	
	return 0;
}
