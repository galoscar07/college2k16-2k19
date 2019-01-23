/*
	Implement a program that creates two threads.
	The threads will print their ID (pthread_self) 10 times and then stop.
	Insure that the printed IDs alternate always (ie A, B, A, B, ...)
*/

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define NUM_TH 2

int counter = 0;
long tid = 0;
pthread_mutex_t mtx;
int x;

void *PrintM (void *threadid){
	while (counter!=20){
		if (counter % 2 == 0) x=0;
		else x=1;	
		if (x == (long) threadid){
			pthread_mutex_lock(&mtx);
			tid = (long) threadid;
  			printf ("Thread Id:  #%ld!\n", tid);
			counter++;
		}
  	}
  pthread_mutex_unlock(&mtx);
}

int main (int argc, char *argv[]){
	pthread_t threads[NUM_TH];
	int rc;
	long t;
	for (t = 0; t < NUM_TH; t++){
		x = t;
    		rc = pthread_create (&threads[t], NULL, PrintM, (void *) t);
    		if (rc){
    		printf ("ERROR; the error code for pthread_create() is %d\n",rc);
    		exit (-1);
     		}
  	}
 	for (t=0; t < NUM_TH; t++){
		pthread_join(threads[t], NULL);
  	}
  	pthread_exit (NULL);
	return 0;
}	


