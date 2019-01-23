#include"Planet.h"
#include "Repository.h"
#include <assert.h>
Repository createRepository()
{
	Repository repo;
	repo.planetNumber = 0;
	return repo;
}

void addPlanet(Repository * repo, Planet p)
{
	repo->planetList[repo->planetNumber++] = p;
}

void Test_addPlanet()
{
	Repository repo;
	Planet p,q;
	repo = createRepository();
	p = CreatePlanet("Planet1", "abcdefg", "Solar System", 29);
	q = CreatePlanet("Earth", "symbol1", "Sol", 0);
	addPlanet(&repo, p);
	addPlanet(&repo, q);
	assert(repo.planetNumber == 2);
}