#include "Tests.h"
#include <assert.h>
#include "DynamicVector.h"
#include "Repository.h"
#include "WatchList.h"
#include "Controller.h"

void Tests::testMovie()
{
	Movie m{ "Due Date", "Comedy",100,2015,99, "https://www.youtube.com/watch?v=2fngvQS_PmQ" };
	assert(m.getTitle() == "DueDate");
	assert(m.getGenre() == "Comedy");
	assert(m.getTrailer() == "https://www.youtube.com/watch?v=2fngvQS_PmQ");
	assert(m.getDuration() == 100);
	
}

void Tests::testDynamicVector()
{
	DynamicVector<int> v1{ 2 };
	v1.add(10);
	v1.add(20);
	assert(v1.getSize() == 2);
	assert(v1[1] == 20);
	v1.add(30);
	assert(v1.getSize() == 3);

	DynamicVector<int> v2 = v1;
	assert(v2.getSize() == 3);

	DynamicVector<int> v3;
	v3 = v1;
	assert(v3[0] == 10);

	// test iterator
	DynamicVector<int>::iterator it = v1.begin();
	assert(*it == 10);
	assert(it != v1.end());
	it++;
	assert(*it == 20);
}

void Tests::testAll()
{
	testMovie();
	testDynamicVector();
}
