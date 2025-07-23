// udp_time_client.c 
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <unistd.h> 
#include <sys/socket.h> 
#include <arpa/inet.h> 
 
#define SERVER_IP "127.0.0.1" 
#define PORT 5050 
#define BUFFER_SIZE 128 
 
int main() { 
    int sockfd; 
    struct sockaddr_in servaddr; 
    socklen_t len; 
    char buffer[BUFFER_SIZE] = "GET TIME"; 
    int n; 
 
    // Create UDP socket 
    sockfd = socket(AF_INET, SOCK_DGRAM, 0); 
    if (sockfd < 0) { 
        perror("socket error"); 
        exit(1); 
    } 
 
    memset(&servaddr, 0, sizeof(servaddr)); 
    servaddr.sin_family = AF_INET; 
    servaddr.sin_port = htons(PORT); 
    inet_pton(AF_INET, SERVER_IP, &servaddr.sin_addr); 
 
    // Send request to server 
    sendto(sockfd, buffer, strlen(buffer), 0, (struct sockaddr *)&servaddr, sizeof(servaddr)); 
 
    // Receive response 
    len = sizeof(servaddr); 
    n = recvfrom(sockfd, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&servaddr, &len); 
    if (n > 0) { 
        buffer[n] = '\0'; 
        printf("Time from server: %s", buffer); 
    } 
    close(sockfd); 
    return 0; 
}
