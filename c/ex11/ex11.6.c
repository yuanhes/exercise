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
    //char buffer[50];
    //snprintf(buffer, 15, "%p\n", &states[i-1]);
    //printf("buffer = %s\n", buffer);
    char *ptr = (char *)&states[i-1]; //the addr you wish to access the contents of
    int j = 0;
    for (i=-1000; i<0; i++) {
        for (j=0; j<16; j++) {
            printf("%c", *(ptr + i * 10 + j )); //this will give you the first byte, you can add any more bytes you need to the ptr itself, like so: *(ptr + nbyte).
        }
        printf("\n");
    }
    return 0;
}
