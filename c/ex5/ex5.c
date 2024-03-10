#include <stdio.h>

/* comment 1 */
int main (int argc, char *argv[])
{
    int distance = 100;

    // comment 2
    printf("You are %d miles away.\n", distance);
    printf("argc = %d .\n", argc);
    printf("argv[0] = %s .\n", argv[0]);
    printf("argv[1] = %s .\n", argv[1]);
    printf("argv[2] = %s .\n", argv[2]);

    return 0;
}
