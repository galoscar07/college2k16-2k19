#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

#define N 10

pthread_mutex_t mtx;
int sum = 0;

void* add(void* arg) {
    pthread_mutex_lock(&mtx);
    sum++;
    pthread_mutex_unlock(&mtx);
    return NULL;
}

int main() {
    int i;
    pthread_t thr[N];

    pthread_mutex_init(&mtx, NULL);

    for(i=0; i<N; i++) {
        pthread_create(&thr[i], NULL, add, NULL);
    }

    for(i=0; i<N; i++) {
        pthread_join(thr[i], NULL);
    }

    pthread_mutex_destroy(&mtx);
    printf("%d\n", sum);

    return 0;
}
