#include "Repository.h"

Repository* createRepo()
{
	Repository* repo = (Repository*)malloc(sizeof(Repository));
	repo->planets = createVector(CAPACITY);

	return repo;
}

void destroyRepo(Repository * repo)
{
	for (int i = 0; i < getSize(repo->planets); i++)
	{
		Planet* p = getPlanetOnPosition(repo->planets, i);
		destroyPlanet(p);
	}

	destroyVector(repo->planets);
	free(repo);
}

void addPlanet(Repository* repo, Planet* p)
{
	addElem(repo->planets, p);
}
