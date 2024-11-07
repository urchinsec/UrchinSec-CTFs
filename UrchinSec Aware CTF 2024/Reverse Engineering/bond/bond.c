#include <stdio.h>
#include <string.h>

void xor_string(const char *input, char *output, char key) {
    size_t length = strlen(input);
    for (size_t i = 0; i < length; i++) {
        output[i] = input[i] ^ key; // XOR operation
    }
    output[length] = '\0'; // Null-terminate the output string
}

int main() {
    const char *target = "gu\\{yn\\zont\\v3j0f0j\\n3g"; // The string to compare with
    char input[256];

    printf("Enter A Key To Bond : ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0; // Remove the newline character

    char key = 'K'; // Example key for XOR operation
    char xor_result[256];

    // Perform XOR on the input string
    xor_string(input, xor_result, key);

    // Check if the result matches the target
    if (strcmp(xor_result, target) == 0) {
        printf("Looks like a match to me!\n");
    } else {
        printf("NO NO! BEGONE!!!!\n");
    }

    return 0;
}