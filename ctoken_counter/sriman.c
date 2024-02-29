#include <stdio.h>
// Sample procedure
void greetUser(char name[]) {
    printf("Hello, %s! Welcome to the program.\n", name);
}
int main() {
    char username[50];
    printf("Enter your name: ");
    scanf("%s", username);
    // Call the procedure
    greetUser(username);
    printf("This is a simple C program.\n");
    return 0;
}
