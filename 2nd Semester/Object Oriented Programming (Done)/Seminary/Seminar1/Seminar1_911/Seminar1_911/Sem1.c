#include<stdio.h>
#include<Windows.h>
#include <string.h>
typedef struct
{
	int arr[100];
	int len;
} vector;

//reads a vector of integer numbers untill it encounters 0
vector read()
{
	vector newarr;
	newarr.len = 0;
	int add;
	printf("Please give an array of integers (end it with 0)\n");
	scanf("%d", &add);

	while (add)
	{
		newarr.arr[newarr.len++] = add;
		scanf("%d", &add);
	}
	return newarr;
}

int sum(vector a) {

	int s = 0; 
	for (int i = 0; i < a.len; i++) {
		s += a.arr[i];
	}

	return s;
}

/* The function determines the longest contiguous sequence of equal numbers in a vector.
	Input: x as type vector of integers,
	Output: first_p and len pointers to an integer representing the position where the subseq
	starts, respectively the length of the subseq;
*/
void determine_seq(vector x, int *first_p, int *len)
{	
	int aux = 1;
	int i;
	for (i = 1; i < x.len; i++)
	{
		if (x.arr[i] == x.arr[i - 1])
			aux++;
		else
		{
			if (*len <= aux)
			{
				*len = aux;
				*first_p = i - aux;
				aux = 1;
			}
		}
	}
	if (*len <= aux)
	{
		*len = aux;
		*first_p = i - aux;
		aux = 1;
	}
}



int main()
{
	system("color f4");
	/*int a=0, b=0;
	printf("Give the value of a:");
	scanf("%d",&a);
	printf("Give the value of b:");
	scanf("%d", &b);
	printf("Here you have the sum %d \n",a+b);
	char name[256], surname[256];
	printf("Give me the name:");
	scanf("%s", name);
	printf("Give me the surname:");
	scanf("%s", surname);
	strcat(name, " ");
	strcat(name, surname);
	printf("Hello %s \n", name);*/

	vector x;
	
	int opt = 0, s = 0;


	while (1){

		printf("\n MENU \n");
		printf("1). Read Array \n");
		printf("2). Display Sum \n");
		printf("3). The longest subsequence of equal numbers \n");
		printf("Enter Command \n"); 
		scanf("%d", &opt);

		if (opt == 1)
			x = read();

		else if (opt == 2) 
		{
			s = sum(x);
			printf("The sum is: %d \n" , s);
		}
		else if (opt == 3)
		{
			int first_p = 0;
			int len = 0;
			determine_seq(x, &first_p, &len);
			for (int i = first_p; i < first_p + len;i++)
				printf("%d \n", x.arr[i]);
		}
		if (opt == 0)
			break;

		


	}
	
	

	system("pause");
	return 0;
}

