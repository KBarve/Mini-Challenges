//Author: Kaustubh Barve
//This code takes in the the number of subjects a student has, and respective grades, and returns the result based on the average.
#include <stdio.h>
#include <stdbool.h>
float average(int grades[]);    //Calculates average grade
char grade(float avg);          //Calculates grade based on average

int main() {
	int subjects;
    printf("How many subjects do you have?\n");
	scanf("%d",&subjects);
    int grades[subjects];
    printf("Please enter your grades:\n");
    //Parsing in grades as a list
    for(int i=0;i<subjects;i++)
    {
        int temp;
        scanf("%d",&temp);
        grades[i]=temp;
    }
	int avg = average(grades);
    printf("Your grade is %c\n",grade(avg));
}

//Function designed to calculate average of a list
float average(int grades[])
{
    float avg = 0.0;
	int subjects = sizeof(grades) / sizeof(grades[0]);
    for(int i=0;i<subjects;i++)
    {
        avg += grades[i];
    }
    avg /= subjects;
	return avg;	
}

//Function that allocates grades based on point structure
char grade(float avg)
{
    char result;
    if (avg>90)
    {
        result = 'A';
    }
    else if (avg>80)
    {
        result = 'B';
    }
    else if (avg>70)
    {
        result = 'C';
    }
    else if (avg>60)
    {
        result = 'D';
    }
    else if (avg>=40)
    {
        result = 'E';
    }
    else if (avg<40)
    {
        result = 'F';
    }
    return result;
}