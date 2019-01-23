#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define NUM_TH 5

void *PrintM (void *threadid)
{
  long tid;
  tid = (long) threadid;
  printf ("Salut! Aici thread-ul #%ld!\n", tid);
  pthread_exit (NULL);
}

int main (int argc, char *argv[])
{
  pthread_t threads[NUM_TH];
  int rc;
  long t;
  for (t = 0; t < NUM_TH; t++)
    {
      printf ("In main: create thread %ld\n", t);
      rc = pthread_create (&threads[t], NULL, PrintM, (void *) t);
      if (rc)
    {
      printf ("ERROR; the error code for pthread_create() is %d\n",
          rc);
      exit (-1);
    }
    }
  pthread_exit (NULL);
}

