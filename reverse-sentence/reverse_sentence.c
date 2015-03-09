#include <stdio.h>

void reverse_sentence(char *text);
void reverse_word(char *left, char *right);

int main(int argc, char *argv[]) {
    char s1[] = "";
    reverse_sentence(s1);
    printf("%s\n", s1);
}

void reverse_sentence(char *text) {
    char *left = text;
    char *right = text;

    while (*left != '\0') {
        // skip whitespace
        if (*left == ' ') { 
            left++;
            continue;
        }
        
        right = left;

        while (*(right + 1) != '\0') {
            // found the word boundary
            if (*(right + 1) == ' ') break;
            right++;
        }

        reverse_word(left, right);
        left = right;
        left++;
    }
}

void reverse_word(char *left, char *right) {
    char aux;
    if (left == right) return;

    while (left < right) {
        aux = *left;
        *left = *right;
        *right = aux;
        left++; right--;
    }
}
