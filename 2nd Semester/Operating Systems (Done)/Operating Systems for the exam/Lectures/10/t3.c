#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define N 10

struct pair {
    int a;
    int b;
};

void* add(void* arg) {
    struct pair* p = (struct pair*)arg;

    printf("ID=%u SUM=%d\n", (unsigned int)pthread_self(), p->a + p->b);
    free(arg);
    return NULL;
}

int main() {
    int i;
    pthread_t thr[N];
    struct pair* arg;

    for(i=0; i<N; i++) {
        arg = (struct pair*) malloc(sizeof(struct pair));
        arg->a = i;
        arg->b = i;
        pthread_create(&thr[i], NULL, add, arg);
    }

    for(i=0; i<N; i++) {
        pthread_join(thr[i], NULL);
    }

    return 0;
}
