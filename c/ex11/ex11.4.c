#include <stdio.h>

int main(int argc, char *argv[])
{
    // go through each string in argv

    int i = 0;
    while(i < argc) {
        printf("arg %d: %s\n", i, argv[i]);
        i++;
    }

    i = argc;
    while(i > 0) {
        printf("arg %d: %s\n", i-1, argv[i-1]);
        i--;
    }

    // let's make our own array of strings
    char *states[] = {
        "California", "Oregon",
        "Washington", "Texas"
    };

    int num_states = 4;
    i = 0;  // watch for this
    while(i < num_states) {
        printf("state %d: %s\n", i, states[i]);
        i++;
    }

    i = 0;  // watch for this
    while(i < num_states) {
        printf("BEFORE COPY: Memory addresses - states[%d]: %p , argv[%d]: %p \n", i, &states[i], i, &argv[i]);
        if ( i < argc) {
            states[i] = argv[i];
        }
        printf("state %d: %s\n", i, states[i]);
        printf("AFTER COPY: Memory addresses - states[%d]: %p , argv[%d]: %p \n", i, &states[i], i, &argv[i]);
        i++;
    }

    return 0;
}
