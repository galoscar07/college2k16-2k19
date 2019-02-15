#include <netinet/ip.h>
#include <stdio.h>

char buf[8] = "xxxxxxxx";
int sfd,r;
struct sockaddr_in soc,csoc;
int port = 2222;
char port_s[100];
int clen=sizeof(struct sockaddr_in);

void clientServing(int nonumber,int port){
    sfd = socket (AF_INET, SOCK_DGRAM, 0);
    soc.sin_family=AF_INET;
    soc.sin_port=htons(port);
    soc.sin_addr.s_addr=inet_addr("0.0.0.0");
    bind(sfd,&soc,sizeof(struct sockaddr_in));
    int i = 0;
    for(i = 0; i < nonumber; ++ i) {
        int n = recvfrom(sfd, buf, 100, 0,&csoc,&clen);
        buf[n] = 0;
        int x;
        x = atoi(buf);
        printf("%d\n",x);
        
    }
}

main (){
    sfd = socket (AF_INET, SOCK_DGRAM, 0);
  
    soc.sin_family=AF_INET;
    soc.sin_port=htons(7777);
    soc.sin_addr.s_addr=inet_addr("0.0.0.0");
  
    bind(sfd,&soc,sizeof(struct sockaddr_in));
    
    while (1) {
        int nonumber;
        r=recvfrom (sfd,buf,100,0,&csoc,&clen);
        buf[r]=0;
        nonumber = atoi(buf);
        printf("%d\n",nonumber);
        sprintf(port_s,"%d",port);
        int n = sendto(sfd, port_s, strlen(port_s), 0, (struct sockaddr*)&csoc, clen);
        if (fork() == 0){
            clientServing(nonumber,port);
            return 0;
        }
        port ++;
    }
} 