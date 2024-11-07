#include <stdio.h>
#include <string.h>
#include <openssl/md5.h>

#define HASH_LENGTH MD5_DIGEST_LENGTH

// Predefined hash for the password "vanessa"
const unsigned char predefined_hash[HASH_LENGTH] = {
    0x28,0x2B,0xBB,0xFB,0x69,0xDA,0x08,0xD0,0x3F,
    0xF4,0xBC,0xF3,0x4A,0x94,0xBC,0x53
};

// Function to hash the password using MD5
void hash_password(const char *password, unsigned char *hash) {
    MD5((unsigned char *)password, strlen(password), hash);
}

// Function to compare the hashes
int compare_hashes(const unsigned char *hash1, const unsigned char *hash2) {
    return memcmp(hash1, hash2, HASH_LENGTH) == 0;
}

int main() {
    char username[50];
    char password[50];
    unsigned char hashed_password[HASH_LENGTH];

    // Input username and password
    printf("Enter username: ");
    fgets(username, sizeof(username), stdin);
    username[strcspn(username, "\n")] = 0; // Remove newline

    printf("Enter password: ");
    fgets(password, sizeof(password), stdin);
    password[strcspn(password, "\n")] = 0; // Remove newline

    // Hash the entered password
    hash_password(password, hashed_password);

    char flag1[] = "urchinsec{";
    strcat(flag1, username);
    strcat(flag1, "_");
    strcat(flag1, password);

    // Compare with the predefined hash
    if (compare_hashes(hashed_password, predefined_hash)) {
        printf("Welcome, Please Use This To Access Other Dimensions: %s\n", flag1);
    } else {
        printf("Access denied for user: %s\n", username);
    }

    return 0;
}