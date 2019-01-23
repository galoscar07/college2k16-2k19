#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
 
int main() {
	int c;
	struct sockaddr_in server;
	char str[100];

	c = socket(AF_INET, SOCK_STREAM, 0);
	if (c < 0) {
		printf("Eroare la crearea socketului client\n");
		return 1;
	}
 
	memset(&server, 0, sizeof(server));
	server.sin_port = htons(1234);
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = inet_addr("127.0.0.1");
 
	if (connect(c, (struct sockaddr *) &server, sizeof(server)) < 0) {
		printf("Eroare la conectarea la server\n");
		return 1;
	}
 
	printf("Enter the filename: ");
	fgets(&str, 100, stdin);
	if (str[strlen(str)-1] == '\n')
    str[strlen(str)-1] = '\0';

	send(c, &str, sizeof(str), 0);
	
	int length = 0;
	recv(c, &length, sizeof(length), MSG_WAITALL);
	
	if(length == -1){
		printf("The file does not exist.\n");
	}
	else{
		printf("Length: %d\n", length);
		
		char content[length+1];
		recv(c, content, length, MSG_WAITALL);
		
		strcat(str, "-copy");
		FILE* fd;
		fd = fopen(&str, "w");
		
		fputs(content, fd);
		
		fclose(fd);
	}
	close(c);
}
 
 

