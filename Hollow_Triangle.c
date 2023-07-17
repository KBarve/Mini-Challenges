//Author: Kaustubh Barve
//Integer input creates a HOLLOW right triangle with a desired number of rows with *
#include <stdio.h>
#include <string.h>
int main()
{
    int count;
    char output[100];
    char temp[100];
    scanf("%d", &count);
    for (int i=0;i<count;i++)
    {
        strcat(output,"*");
        if (i==0 || i==1 || i==count-1)
        {
            printf("%s",output);
        }
        else
        {
            strcat(temp," ");
            printf("*%s*",temp);
        }
        if (i!=(count-1))
        {
            printf("\n");
        }
    }
    return 0;
}