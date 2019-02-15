/* Se daun fisier ca pairametru "
utilizatori.txt", citeste din fiser utilizatori, pentru fiecare utilizator creeaza un thread nou, daca e logat afisezi numele, statia la care e legat si ora logarii */
#include <pthread.h>
#include <studio.h>
#include <stdlib.h>
#include <string.h>

void functie_thr(void *arg);

struct params{
	char[20];
}


int main(int argc, char **argv){
	FILE *f;
	int nrLinii = 0, ch;
	char *linee = NULL;
	size_t len =0;
	ssize_t read;
	int i;	

	f = fopen(argv[1],"r");
	if (f==NULL){
		perror("Eroare la deschiderea fisierului");
		exit(EXIT_FAILURE);
	}
	do{
		ch = fgetc(f);
		if(ch=='\n')
			nrLinii++;
	}while(ch != EOF);

	//pun file pointer la inceputul fisierului
	fseek(f, 0 , SEEK_SET);
	pthread_t *t = (pthread_t *)malloc(nrLinii * sizeof(pthread_t));
	printf("Sizeof(pthread_t)=%lu\n",sizeof(pthread_t));
	while((read = getline(&line, &len, f))!= -1){
		struct params *s = malloc(sizeof(struct params));
		strcopy()
		int rc = pthread_create(&t[i],NULL, functie_thr, (void *)line);
		if(rc){
			printf("Eroare la crearea threadului %d\n", t[i]);
		}
		printf("Am creat threadul %d, si i-am trimit: %s \n",t[i], line)
	}
	free(t);
	fclose(f);
	pthread_exit(NULL);
	return 0;
}

void *functie_thr(void *arg){
	struct params *p =(struct params*) arg;
	printf("Thread-ul %d, a primit %",pthread_self(),p);
	free(p);
	pthread_exit(NULL)
}
