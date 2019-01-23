/*
The main process reads from astandard input numbers as long as the user enters positive numbers.
For each N number it will launch a new process that will double the number DN and creates a new process. The new process will establish the Fibonacci number found on the DN position. Eg. for N=4, ND=8 the Fibonacci number is 21. The Fibonacci number will be send as a response, using a pipe channel, to the main process.
In order to establish the Fibonacci number on a given place the subprocess will use a shell script launched with popen.
*/

#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
	int nr, p, pfp[2], a;
	char cmd[1000];
	char buffer[BUFSIZ];
	printf("Give a number: ");
	scanf("%d", &nr);
	while( nr > 0){
		pipe(pfp);
		if( pipe(pfp) < 0){
			perror("It couldn't create pipe");
			exit(0);
		}
		p=fork();
		wait(0);
		if (p < 0){
			perror("It couldn't create process");
			exit(0);
		}
		if (p == 0){
			nr=2*nr;
			snprintf(cmd, sizeof(cmd), "./fibo.sh %d", nr);
			FILE *fp = popen(cmd, "r");
			fgets(buffer, BUFSIZ, fp);
			a=atoi(buffer);
			pclose(fp);
			write(pfp[1], &a, sizeof(int));
			break;
		}
		wait(0);
		read(pfp[0], &a, sizeof(int));
		close(pfp[0]);
		close(pfp[1]);
		printf("The %d th number from the fibonacci series is:  %d. \n", 2*nr, a);
		printf("Give a number: ");
		scanf("%d", &nr);
	}
	return 0;
}
