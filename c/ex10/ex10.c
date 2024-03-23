#include <stdio.h>

int main(int argc, char *argv[])
{
    int i = 0;

    // go through each string in argv
    // why am I skipping argv[0]?
    int j = 0;
    for(i=1, j=1; i < argc;i++, j=i+1 ) {
        printf("i, arg %d: %s\n", i, argv[i]);
        printf("j, arg %d: %s\n", j, argv[j]);
    }

    // let's make our own array of strings
    char *states[] = {
        "California", "Oregon",
        "\0", "\{null}",
        "Washington", "Texas"
    };
    int num_states = 6;

    for(i = 0; i < num_states; i++) {
        printf("state %d: %s\n", i, states[i]);
    }

    for(i = 0; i < num_states; i++) {
        argv[i]=states[i];
        printf("arg %d: %s\n", i, argv[i]);
        printf("state %d: %s\n", i, states[i]);
    }

    return 0;
}
