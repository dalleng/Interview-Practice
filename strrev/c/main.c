#include <stdio.h>
#include <string.h>

/* Reverse the given string in-place */

void strrev(char *string);

int main(int argc, char *argv[]) {
    char some_string[] = "hola";
    strrev(some_string);
    printf("%s\n", some_string);
}

void strrev(char *string) {
    char aux;
    int length = strlen(string);
    int front = 0;
    int back = length - 1;

    while (front < back) {
        aux = string[front];
        string[front] = string[back];
        string[back] = aux;
        front++;
        back--;
    }
}
