//Author: Kaustubh Barve
// Integer input prints a square with a desired size of rows with #
#include <stdio.h>
#include <string.h>
int main()
{
    int size;
    char output[100];
    scanf("%d", &size);
    for (int i=0;i<size;i++)
    {
        strcat(output,"*");
    }
    for (int i=0;i<size;i++)
    {
        printf("%s",output);
        if (i!=(size-1))
        {
        printf("\n");
        }

    }
    
    return 0;
}