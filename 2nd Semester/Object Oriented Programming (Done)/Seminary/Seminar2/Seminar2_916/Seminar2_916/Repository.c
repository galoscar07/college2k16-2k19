#include "Repository.h"
#include <stdlib.h>
Repository * repositoryCreate()
{
	Repository *rep = (Repository*)malloc(sizeof(Repository));
	if (rep == NULL) {
		return NULL;
	}

	rep->arr = create_array(CAPACITY);

	return rep;
}

void repositoryDestroy(Repository * rep)
{
	for (int i = 0; i < rep->arr->size; i++) {
		destroyPlanet(get_from_array(rep->arr, i));
	}

	destroy_array(rep->arr);

	free(rep);
}

void repositoryAdd(Repository * rep, Planet * p)
{
	add_to_array(rep->arr, p);
}
