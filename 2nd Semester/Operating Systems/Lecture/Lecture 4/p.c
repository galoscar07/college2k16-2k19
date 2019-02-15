#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

int main() {
    int i, j;

    for(i=0; i<3; i++) {
        if(fork() == 0) {
            for(j=0; j<4; j++) {
                sleep(1);
                printf("%d.%d: sunt %d fiu al lui %d\n", i, j, 
                                                      getpid(),
                                                      getppid());
            }
            exit(0);
        }
    }
    for(i=0; i<3; i++) {
        wait(0);
    }
    return 0;
}
