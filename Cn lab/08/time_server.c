#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <unistd.h> 
#include <time.h> 
#include <sys/socket.h> 
#include <arpa/inet.h> 
 
#define PORT 5050 
#define BUFFER_SIZE 128 
 
int main() { 
    int sockfd; 
    struct sockaddr_in servaddr, cliaddr; 
    socklen_t len; 
    char buffer[BUFFER_SIZE]; 
    time_t now; 
 
    // Create UDP socket 
    sockfd = socket(AF_INET, SOCK_DGRAM, 0); 
    if (sockfd < 0) { 
        perror("socket error"); 
        exit(1); 
    } 
 
    memset(&servaddr, 0, sizeof(servaddr)); 
    servaddr.sin_family = AF_INET; 
    servaddr.sin_addr.s_addr = INADDR_ANY; 
    servaddr.sin_port = htons(PORT); 
 
    if (bind(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) { 
        perror("bind error"); 
        exit(1); 
    } 
 
    printf("UDP Time Server running on port %d...\n", PORT); 
 
    while (1) { 
        len = sizeof(cliaddr); 
        // Wait for request from client 
        if (recvfrom(sockfd, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&cliaddr, &len) < 0) { 
            perror("recvfrom error"); 
            continue; 
        } 
 
        // Get current time 
        now = time(NULL); 
        snprintf(buffer, sizeof(buffer), "%s", ctime(&now)); 
 
        // Send time to client 
        sendto(sockfd, buffer, strlen(buffer), 0, (struct sockaddr *)&cliaddr, len); 
        printf("Sent time to client: %s", buffer); 
    } 
    close(sockfd); 
    return 0; 
}