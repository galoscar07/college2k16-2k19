#include "Repository.h"

PlanetsRepo	* Create_Repo()
{
	PlanetsRepo		*p	=	(PlanetsRepo *)malloc(sizeof(PlanetsRepo));
	p->Planets = createArray(1);
	return (p);
}

void addRepo(PlanetsRepo* r, Planet* p)
{
	addElement(r->Planets, p);
}

void destroyRepo(PlanetsRepo *r)
{
	int len = r->Planets->length;

	for (int i = 0; i < len; i++)
		destroyPlanet(r->Planets->elems[i]);
	destroyArray(r->Planets);
	free(r);
}
