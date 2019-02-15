#include <stdio.h>
#include <pthread.h>

#define N 10

struct pair {
    int a;
    int b;
};

void* add(void* arg) {
    struct pair* p = (struct pair*)arg;

    printf("ID=%u SUM=%d\n", (unsigned int)pthread_self(), p->a + p->b);
    return NULL;
}

int main() {
    int i;
    pthread_t thr[N];
    struct pair arg[10];

    for(i=0; i<N; i++) {
        arg[i].a = i;
        arg[i].b = i;
        pthread_create(&thr[i], NULL, add, &arg[i]);
    }

    for(i=0; i<N; i++) {
        pthread_join(thr[i], NULL);
    }

    return 0;
}
