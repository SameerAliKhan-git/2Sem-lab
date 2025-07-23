#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <unistd.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <arpa/inet.h> 
#include <netinet/ip_icmp.h> 
#include <netdb.h> 
#include <sys/time.h> 
 
#define PACKET_SIZE     64 
 
// Compute checksum for the ICMP header 
unsigned short checksum(void *b, int len) { 
    unsigned short *buf = b; 
    unsigned int sum=0; 
    unsigned short result; 
 
    for ( sum = 0; len > 1; len -= 2 ) 
        sum += *buf++; 
    if ( len == 1 ) 
        sum += *(unsigned char*)buf; 
    sum = (sum >> 16) + (sum & 0xFFFF); 
    sum += (sum >> 16); 
    result = ~sum; 
    return result; 
} 
 
int main(int argc, char *argv[]) { 
    int sockfd; 
    struct sockaddr_in addr_con; 
    char packet[PACKET_SIZE]; 
    struct icmp *icmp_hdr = (struct icmp *) packet; 
    struct timeval start, end; 
    struct hostent *host; 
    int addrlen, n; 
    char recvbuf[PACKET_SIZE + sizeof(struct ip)]; 
 
    if (argc != 2) { 
        printf("Usage: %s <hostname/IP>\n", argv[0]); 
        return 1; 
    } 
 
    sockfd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP); 
    if (sockfd < 0) { 
        perror("Socket error"); 
        return 1; 
    } 
 
    memset(&addr_con, 0, sizeof(addr_con)); 
    addr_con.sin_family = AF_INET; 
    if ((host = gethostbyname(argv[1])) == NULL) { 
        printf("Host not found!\n"); 
        return 1; 
    } 
    addr_con.sin_addr = *(struct in_addr*)host->h_addr; 
 
    // Prepare ICMP header 
    memset(packet, 0, PACKET_SIZE); 
    icmp_hdr->icmp_type = ICMP_ECHO; 
    icmp_hdr->icmp_code = 0; 
    icmp_hdr->icmp_id = getpid(); 
    icmp_hdr->icmp_seq = 1; 
    memset(icmp_hdr->icmp_data, 0xa5, PACKET_SIZE - sizeof(struct icmp)); 
    icmp_hdr->icmp_cksum = 0; 
    icmp_hdr->icmp_cksum = checksum(icmp_hdr, PACKET_SIZE); 
 
    gettimeofday(&start, NULL); 
    // Send ICMP Echo Request 
    if (sendto(sockfd, packet, PACKET_SIZE, 0, (struct sockaddr *)&addr_con, sizeof(addr_con)) <= 0) { 
        perror("Sendto error"); 
        return 1; 
    } 
 
    addrlen = sizeof(addr_con); 
    // Receive ICMP Echo Reply 
    if ((n = recvfrom(sockfd, recvbuf, sizeof(recvbuf), 0, (struct sockaddr *)&addr_con, &addrlen)) <= 0) { 
        perror("Recvfrom error"); 
        return 1; 
    } 
    gettimeofday(&end, NULL); 
 
    // Calculate round trip time 
    double timeElapsed = (end.tv_sec - start.tv_sec) * 1000.0; 
    timeElapsed += (end.tv_usec - start.tv_usec) / 1000.0; 
 
    struct ip *ip_hdr = (struct ip *) recvbuf; 
    struct icmp *icmphdr_recv = (struct icmp *)(recvbuf + (ip_hdr->ip_hl << 2)); 
 
    if (icmphdr_recv->icmp_type == ICMP_ECHOREPLY) { 
        printf("Reply from %s: bytes=%d icmp_seq=%d ttl=%d time=%.2f ms\n", 
            argv[1], n, icmphdr_recv->icmp_seq, ip_hdr->ip_ttl, timeElapsed); 
    } else { 
        printf("No ICMP_ECHOREPLY received.\n"); 
    } 
 
    close(sockfd); 
    return 0;
}



