#include <stdio.h>
#include <string.h>
#include <Windows.h>

typedef struct
{
	int array[100];
	int length;
} vector;

//Reads a vector of integer elements different from 0
vector read()
{
	vector a;
	a.length = 0;
	int element = 1;
	printf("Give the elements: ");
	while (element != 0)
	{
		scanf("%d", &element);
		if (element) {
			a.array[a.length++] = element;
		}
	}
	return a;
}

// Computes the sum of all the elements in a given vector.
// Input: v - vector of integers;
// Output: The sum of all the elements
int sum(vector v)
{
	int sum = 0;
	for (int i = 0; i < v.length; i++)
		sum += v.array[i];

	return sum;
}

// Returns the options of the menu
char* menu()
{
	return "1. Read a vector\n2. Compute the sum of numbers of a vector\n 3.Find the logest subsequence of equal numbers \n0. Exit\n";
}

//function to determine the longest subsequence of equal elements
void determine_subsequence(vector v, int* pos1, int* pos2) {
	*pos1 = 0;
	*pos2 = 0;
	int max_difference = 0;
	int i;
	for (i = 0; i < v.length-1; i++) {
		int j = i + 1;
		while (j < v.length && v.array[j] == v.array[j - 1]) {
			j++;
		}
		if (j - i > max_difference) {
			max_difference = j - i;
			*pos1 = i;
			*pos2 = j - 1;
		}

	}

}

void print_subsequence(int pos1, int pos2, vector v) {
	printf("The subsequence is: \n|");
	int i;
	for (i = pos1; i<= pos2; i++) printf("%d  ", v.array[i]);

}


int main()
{
	system("color f4");

	float d = 1.2;
	printf("%d", d);


	/*char surname[40];
	char firstname[20];

	printf("Surname: ");
	scanf("%s", surname);
	printf("First name: ");
	scanf("%s", firstname);
	strcat(surname, firstname);
	printf("Hello, %s!\n", surname);
	printf("The length is: %d\n", strlen(surname));*/
	char* m = menu();
	int cmd;
	vector v;
	int s;
	/*
	vector a = read();

	int s = sum(a);

	printf("Sum: %d\n", s);
	*/

	do
	{
		printf(m);
		printf("Input a command\n");
		scanf("%i", &cmd);

		if (cmd == 1)
		{
			v = read();
		}
		else if (cmd == 2)
		{
			s = sum(v);
			printf("Sum: %i\n", s);
		}
		else if (cmd == 3) {
			int pos1, pos2;
			
			determine_subsequence(v, &pos1, &pos2);
			print_subsequence(pos1, pos2, v);
		}
	} while (cmd != 0);

	system("pause");
	return 0;
}