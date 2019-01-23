#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define N 2

int a[4] = {1, 2, 3, 4};

void* add_to_previous(void* arg) {
    int p = (int)arg;

    /* p==0 -> a[0] += a[1]*/
    /* p==1 -> a[2] += a[3]*/
    a[2*p] += a[2*p+1];
    return NULL;
}

int main() {
    int i;
    pthread_t thr[N];

    for(i=0; i<N; i++) {
        pthread_create(&thr[i], NULL, add_to_previous, (int*)i);
    }

    for(i=0; i<N; i++) {
        pthread_join(thr[i], NULL);
    }

    a[0] += a[2];

    printf("%d\n", a[0]);

    return 0;
}
