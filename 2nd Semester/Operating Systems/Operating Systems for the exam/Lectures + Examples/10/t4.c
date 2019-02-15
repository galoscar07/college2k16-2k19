#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define N 10

void* show_order_number(void* arg) {
    int p = (int)arg;

    printf("%d\n", p);
    return NULL;
}

int main() {
    int i;
    pthread_t thr[N];

    for(i=0; i<N; i++) {
        pthread_create(&thr[i], NULL, show_order_number, (int*)i);
    }

    for(i=0; i<N; i++) {
        pthread_join(thr[i], NULL);
    }

    return 0;
}
