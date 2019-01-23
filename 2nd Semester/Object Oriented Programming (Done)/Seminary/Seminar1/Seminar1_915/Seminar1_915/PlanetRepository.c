#include "PlanetRepository.h"

PlanetRepo createRepo()
{
	PlanetRepo r;
	r.len = 0;
	return r;
}

void addPlanet(PlanetRepo * r, Planet p)
{
	r->v[r->len] = p;
	r->len++;
}

void testAdd()
{
	PlanetRepo repo = createRepo();
	Planet p1 = create_planet("UV$O*~1", "Gallifrey", "Kasterborous", 250000);
	Planet p2 = create_planet("V^E$9L@", "Abydos", "Sol", 583);

	addPlanet(&repo, p1);
	assert(repo.len == 1);

	addPlanet(&repo, p2);
	assert(repo.len == 2);
}
