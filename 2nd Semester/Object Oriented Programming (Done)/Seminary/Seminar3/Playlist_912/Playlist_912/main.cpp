#include "DynamicVector.h"
#include <assert.h>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

void Test_DV()
{
	DynamicVector <string> v{ 10 };
	assert(v.Get_Len() == 0);
	string s = "string";
	v.Add(s);
	assert(v.Get_Len() == 1);

	DynamicVector<string> v2;
	v2 = v;
	assert(v2.Get_Len() == 1);

	/*for (string x : v)
	{
		std::cout << x;
	}*/
}

int main()
{
	Test_DV();

	std::vector<int> v{ 1, 2, 3, 4 };
	int c = 0;
	for (int x : v)
	{
		if (x % 2 == 0)
			c++;
	}

	DynamicVector<int> dv{};
	dv.Add(1);
	dv.Add(20);
	dv.Add(25);
	for (DynamicVector<int>::iterator it = dv.begin(); it != dv.end(); it++)
	{
		std::cout << *it << " ";
	}

	for (auto x : dv)
	{
		std::cout << x << " ";
	}

	c = std::count_if(dv.begin(), dv.end(), [](int x) { return x % 2 == 0; });
	
	return (0);
}