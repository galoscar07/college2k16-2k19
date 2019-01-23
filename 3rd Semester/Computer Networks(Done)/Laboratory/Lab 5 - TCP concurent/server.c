#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>

void clientserving(int c){
	char str[100];
	int length = 0;
	recv(c, &str, 100, MSG_WAITALL);

	if(access(&str, R_OK) == -1){
		length = -1;
		send(c, &length, sizeof(length), 0);
		close(c);
		exit(0);
	}
	else{
		FILE* fd;
		fd = fopen(&str, "r");
		
		fseek(fd, 0, SEEK_END);
		length = ftell(fd);
		fseek(fd, 0, SEEK_SET);
		
		send(c, &length, sizeof(length), 0);
		
		char content[length+1];
		fread(content, length, 1, fd);
		
		send(c, content, length, 0);
		
		fclose(fd);
		close(c);
		exit(0);
	}
}

int main() {
	int s;
	struct sockaddr_in server, client;
	int c, l; 

	s = socket(AF_INET, SOCK_STREAM, 0);
	if (s < 0) {
		printf("Eroare la crearea socketului server\n");
		return 1;
	}
 
	memset(&server, 0, sizeof(server));
	server.sin_port = htons(1234);
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = INADDR_ANY;
 
	if (bind(s, (struct sockaddr *) &server, sizeof(server)) < 0) {
		printf("Eroare la bind\n");
		return 1;
	}
 
	listen(s, 5);
 
	l = sizeof(client);
	memset(&client, 0, sizeof(client));
 
	while (1) {
		c = accept(s, (struct sockaddr *) &client, &l);
		printf("A client connected.\n");
 
		if(fork() == 0){
			clientserving(c);
			return 0;			
		}
	}
}
 

