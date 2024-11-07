#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

const int SAMPLE_RATE = 44100;
#define DURATION 2 // Duration of the gibberish sound in seconds

void generate_magic(const char *output) {
    FILE *file = fopen(output, "wb");
    if (!file) {
        perror("Failed to open output file");
        return;
    }

    int sample_count = SAMPLE_RATE * DURATION;
    uint32_t data_size = sample_count * sizeof(int16_t);

    // Write WAV header
    fwrite("RIFF", 1, 4, file);
    uint32_t chunk_size = 36 + data_size;
    fwrite(&chunk_size, sizeof(chunk_size), 1, file);
    fwrite("WAVE", 1, 4, file);
    fwrite("fmt ", 1, 4, file);
    uint32_t subchunk1_size = 16;
    fwrite(&subchunk1_size, sizeof(subchunk1_size), 1, file);
    uint16_t audio_format = 1;
    fwrite(&audio_format, sizeof(audio_format), 1, file);
    uint16_t num_channels = 1;
    fwrite(&num_channels, sizeof(num_channels), 1, file);
    fwrite(&SAMPLE_RATE, sizeof(SAMPLE_RATE), 1, file); // Using the variable here
    uint32_t byte_rate = SAMPLE_RATE * num_channels * sizeof(int16_t);
    fwrite(&byte_rate, sizeof(byte_rate), 1, file);
    uint16_t block_align = num_channels * sizeof(int16_t);
    fwrite(&block_align, sizeof(block_align), 1, file);
    uint16_t bits_per_sample = 16;
    fwrite(&bits_per_sample, sizeof(bits_per_sample), 1, file);
    fwrite("data", 1, 4, file);
    fwrite(&data_size, sizeof(data_size), 1, file);

    // Write gibberish samples
    for (int i = 0; i < sample_count; i++) {
        int16_t sample = (int16_t)(rand() % 32768) - 16384; // Random noise
        fwrite(&sample, sizeof(sample), 1, file);
    }

    fclose(file);
}

void exclusive_or(const char *input, char *output, char key) {
    size_t length = strlen(input);
    for (size_t i = 0; i < length; i++) {
        output[i] = input[i] ^ key; // XOR operation
    }
    output[length] = '\0'; // Null-terminate the output string
}

int main() {
    const char *correct_xor = "l~WadpxWl~WadggWqnoWl~W`pa~rfW{z|{"; // Replace with actual expected XOR result
    char input[256];

    printf("Enter Your Song Name: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0; // Remove the newline character

    // Key for XOR operation
    char key = 0x8; // Example key, you can choose any character

    // XOR and reverse the input
    char xor_result[256];
    exclusive_or(input, xor_result, key);

    // Reverse the XOR result
    char reversed[256];
    size_t length = strlen(xor_result);
    for (size_t i = 0; i < length; i++) {
        reversed[i] = xor_result[length - 1 - i];
    }
    reversed[length] = '\0'; // Null-terminate the reversed string

    // Check if the reversed XOR result matches the correct string
    if (strcmp(reversed, correct_xor) == 0) {
        printf("You have it!\n");
    } else {
        printf("Let's Try This Again!\n");
        generate_magic("lovely.wav");
    }

    return 0;
}