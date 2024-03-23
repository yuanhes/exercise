#include <stdio.h>
#include <string.h>

int main (int argc, char *argv[])
{
    int areas[] = {10, 12, 13, 14, 20};
    char name[] = "Zed";
    char full_name[] = {
        'Z', 'e', 'd', 
        ' ', 'A', '.', ' ', 
        'S', 'h', 'a', 'w', '\0', 'a', 'b'
    };
    char full_name_st[] = "Zed A. Shaw";

   // WARNIGN: On some systems you may have to change the 
   // %ld in this code to a %u since it will use unsigned ints.
   printf("The size of an int: %ld\n", sizeof(int));
   printf("The size of areas (int[]): %ld\n", sizeof(areas));
   printf("The number of ints in areas: %ld\n", sizeof(areas) / sizeof(int));
   printf("The first area is %d, the 2nd %d.\n", areas[0], areas[1]);

   printf("The size of a char: %ld\n", sizeof(char));
   printf("The size of name (char[]): %ld\n", sizeof(name));
   printf("The number of chars: %ld\n", sizeof(name) / sizeof(char));
   
   printf("The size of full_name (char[]): %ld\n", sizeof(full_name));
   printf("The number of chars: %ld\n", sizeof(full_name) / sizeof(char));
   printf("The strlen of full_name (char[]): %ld\n", strlen(full_name));

   printf("name=\"%s\" and full_name=\"%s\"\n", name, full_name);

   printf("The size of full_name_st (char[]): %ld\n", sizeof(full_name_st));
   printf("The number of chars: %ld\n", sizeof(full_name_st) / sizeof(char));
   printf("The strlen of full_name_st (char[]): %ld\n", strlen(full_name_st));

   printf("full_name_st=\"%s\"\n", full_name_st);

   int i;
   for (i = -1; i < 5; i++) {
       printf("name[%d]=\"%c\"\n", i, name[i]);
   }
   for (i = -1; i < 14; i++) {
       printf("full_name[%d]=\"%c\"\n", i, full_name[i]);
   }
   // for (i = -100; i < 100; i++) {
   //     printf("areas[%d]=\"%d\"\n", i, areas[i]);
   // }

   return 0;
}
