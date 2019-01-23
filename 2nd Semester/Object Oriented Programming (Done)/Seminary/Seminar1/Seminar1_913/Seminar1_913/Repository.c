#include "Repository.h"
#include<assert.h>
Planets createRepository()
{
	Planets v;
	v.length = 0;
	return v;
}

void addPlanet(Planets *repo, planet mPlanet)
{
	repo->planets[repo->length++] = mPlanet;
	// (*repo).planets is the same thing
}

void test_add()
{
	Planets repo1 = createRepository();
	planet p1 = create_planet("1234567", "animals", "planet of the apes", 123);
	planet p2 = create_planet("0123456", "Sol", "Earth", 0);
	addPlanet(&repo1, p1);
	addPlanet(&repo1, p2);
	assert(repo1.length == 2);

}