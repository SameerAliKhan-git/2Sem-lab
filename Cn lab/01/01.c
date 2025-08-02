#include <stdio.h>
#include <stdlib.h>

int main() {

int octet1, octet2, octet3, octet4;
printf("Enter an IPv4 address (e.g., 192.168.1.1): ");
if(scanf("%d.%d.%d.%d", &octet1, &octet2, &octet3, &octet4) != 4) {
    printf("Invalid input format.\n");
    return 1;
}

if (octet1 == 127) {
        printf("Loopback address (127.x.x.x)\n");
}else if (octet1 >= 1 && octet1 <= 126) {
    printf("Class A\n");
} else if (octet1 >= 128 && octet1 <= 191) {
    printf("Class B\n");
} else if (octet1 >= 192 && octet1 <= 223) {
    printf("Class C\n");
} else if (octet1 >= 224 && octet1 <= 239) {
    printf("Class D\n");
} else if (octet1 >= 240 && octet1 <= 255) {
    printf("Class E\n");
} else {
    printf("Invalid IP address.\n");
}

return 0;

}