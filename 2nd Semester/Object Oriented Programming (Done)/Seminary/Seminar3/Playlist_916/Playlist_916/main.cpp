#include"dynamic_array.h"
#include"Song.h"
#include<assert.h>

void test_vector()
{
	DynamicVector<Song> v{ 1 };
	Song s1{ "ed sheeran","I see fire",120,"www.google.com" };
	Song s2{ "Pink","Fire",300,"www.youtube.com" };
	v.add_to_array(s1);
	assert(v.get_size() == 1);
	v.add_to_array(s2);
	assert(v.get_size() == 2);
	DynamicVector<Song> v1;
	v1 = v;
}

int main()
{
	test_vector();
	return 0;
}