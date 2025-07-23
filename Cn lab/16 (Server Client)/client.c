#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <unistd.h>

#define PORT 5353
#define MAXBUFLEN 256

int main() {
    int sockfd;
    struct sockaddr_in servaddr;
    char buffer[MAXBUFLEN], domain[MAXBUFLEN];

    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(PORT);
    inet_pton(AF_INET, "127.0.0.1", &servaddr.sin_addr);

    printf("Enter domain name: ");
    fgets(domain, MAXBUFLEN, stdin);
    domain[strcspn(domain, "\n")] = 0;

    sendto(sockfd, domain, strlen(domain), 0, (struct sockaddr *)&servaddr, sizeof(servaddr));
    socklen_t len = sizeof(servaddr);
    int n = recvfrom(sockfd, buffer, MAXBUFLEN, 0, (struct sockaddr *)&servaddr, &len);
    buffer[n] = 0;

    printf("Server response: %s\n", buffer);
    close(sockfd);
    return 0;
}