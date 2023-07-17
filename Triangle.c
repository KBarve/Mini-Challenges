//Author: Kaustubh Barve
//Integer input creates a right triangle with a desired number of rows with *
#include <stdio.h>
#include <string.h>
int main()
{
    int count;
    char output[100];
    scanf("%d", &count);
    for (int i=0;i<count;i++)
    {
        strcat(output,"*");
        printf("%s",output);
        if (i!=(count-1))
        {
        printf("\n");
        }
    }
    
    return 0;
    
}