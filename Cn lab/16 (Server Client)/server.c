#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <unistd.h>

#define PORT 5353
#define MAXBUFLEN 256

struct dns_entry {
    char domain[100];
    char ip[20];
};

int main() {
    int sockfd;
    struct sockaddr_in servaddr, cliaddr;
    char buffer[MAXBUFLEN];
    socklen_t len = sizeof(cliaddr);

    // Simple DNS table
    struct dns_entry table[] = {
        {"example.com", "1.2.3.4"},
        {"test.com", "5.6.7.8"},
        {"google.com", "142.250.64.78"}
    };
    int table_size = sizeof(table) / sizeof(table[0]);

    // Create UDP socket
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);

    memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(PORT);

    // Bind socket
    bind(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr));
    printf("DNS Server running on port %d...\n", PORT);

    while (1) {
        int n = recvfrom(sockfd, buffer, MAXBUFLEN, 0, (struct sockaddr *)&cliaddr, &len);
        buffer[n] = 0;
        printf("Received query: %s\n", buffer);

        // Search for domain
        int found = 0;
        for (int i = 0; i < table_size; i++) {
            if (strcmp(buffer, table[i].domain) == 0) {
                sendto(sockfd, table[i].ip, strlen(table[i].ip), 0, (struct sockaddr *)&cliaddr, len);
                found = 1;
                break;
            }
        }
        if (!found) {
            char *msg = "Domain not found";
            sendto(sockfd, msg, strlen(msg), 0, (struct sockaddr *)&cliaddr, len);
        }
    }
    close(sockfd);
    return 0;
}