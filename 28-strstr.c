#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//NOTE: Both strStr implementations are functional and pass.
//      First is done without using strstr in C, second is done with strstr in C.



int strStrAlt(char * haystack, char * needle){
    if (needle[0] == '\0') {
        return 0;
    }

    int i = 0;
    int counter = 0;
    while (haystack[i] != '\0') {
        while (true) {
            if (needle[counter] == '\0') {
                //Reached end of needle. Word matched.
                return i;
            }
            if (haystack[i + counter] == '\0')  {
                //Didn't match word. Reached end of haystack.
                return -1;
            }
            
            if (haystack[i + counter] == needle[counter]) {
                //Matches. 
                counter++;
            } else {
                counter = 0;
                break;
            }
        }
        i++;
    }
    
    return -1;
}

int strStr(char * haystack, char * needle) {
    char * matchStart = strstr(haystack, needle);
    if (matchStart == NULL) {
        return -1;
    }

    //Pointer arithmetic
    int location = matchStart - haystack;
    return location;
}

int main(void) {
    int value = strStr("hello", "lo");
    printf("%d", value);
    return 0;
}