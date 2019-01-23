	/*	Sa se scrie un program care genereaza pe 5 thread-uri distincte 1000 de numere intregi pe care le introduce intr-un vector global. 

        Fiecare numar generat va fi introdus de thread-ul care l-a generat pe pozitia corecta in vector, astfel incat la orice moment vectorul sa fie sortat.

        Threadul principal va afisa la fiecare 10 numere generate intreg continutul vectorului.*/
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

int x,counter;
int something[1000];
pthread_t t[10];
pthread_mutex_t mtx;

funtion(int i){
	while (counter != 10){
		if (x == i){
			pthread_mutex_lock(&mtx);
			counter ++;
			something[counter] = x;
			while (x == i) {
				srand(time(NULL));
				x = rand() % 10;
			}
		}
		pthread_mutex_unlock(&mtx);
		
	}
}

int main(){
	printf("Hello World!!\n");
	int i;
	srand(time(NULL));
	x = rand() % 10;
	for (i =0; i<=10; i++){
		pthread_create(&t[i],NULL,funtion,i);
	}
	for (i =0; i<=10; i++){
		pthread_join(t[i],NULL);
	}
	for (i =0;i<counter;i++){
		printf("Element on position %d, have the value %d \n",i,something[i]);
	}
	return 0;
}

