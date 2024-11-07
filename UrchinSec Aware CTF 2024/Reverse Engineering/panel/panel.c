#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>

int check_secret(char *password) {
    char *endptr;
    errno = 0;
    long num = strtol(password, &endptr, 10);
    printf("\nPassword Input : %s\n", password);

    if (errno == ERANGE) {
        printf("None Found In Range\n");
        return 1;
    }

    if (endptr == password) {
        printf("No Secret Code Was Found\n");
        return 1;
    }

    if (*endptr != '\0') {
        printf("Secret Code Found And Extracted! Found Characters\n");
    }

    printf("Fetched Secret Code : %ld\n", num);

    if (num == 133739) {
        printf("\nYou Access The Secret Tunnel! There is no need for me to give you the flag! Fetch it your self as a true Secret Agent!\n");
        int len = strlen(password);
//        printf("\n%ld", len);
        int flag = num * len; // 2006085 *expected
        int flagb = flag - num; // 1872346 *expected
        int output = flagb / 7; // 267478 *expected
        if (output == 267478) {
            printf("urchinsec{%ld}\n", flagb + 2006085); // 3878431 *expected
        } else {
            printf("You got it! Wrong!\n");
        }
    } else {
        printf("Let's Do this One More Time\n");
    }

    return 0;
}

int main() {
    char username[10];
    char password[20];

    printf("[+]===============================[+]\n");
    printf("[+]         Secure Agency         [+]\n");
    printf("[+]===============================[+]\n");
    printf("[*]-------------------------------[*]\n");
    printf("[*]    Login Now To Join Comms    [*]\n");
    printf("[*]-------------------------------[*]\n\n");

    printf(">> Enter Your Username >> ");
    scanf("%s", &username);

    if (strcmp(username, "urchinadmin") == 0) {
        printf("[+] Correct Username \n");
        printf(">> Enter Your Password >> ");
        scanf("%s", &password);
        printf("\n[!] Confirming Password");
        check_secret(password);
    } else {
        printf("[!] Wrong Username!");
    }

    return 0;
}