//Author: Kaustubh Barve
//Contains a function that returns True if input is a prime number, and False otherwise
#include <stdio.h>
#include <stdbool.h>
bool prime(int n);


int main() {
	int input;
	scanf("%d",&input);
	if (prime(input))
	{
		printf("Yes");
	}
	else
	{
		printf("No");
	}
	return 0;
}

bool prime(int n) {
	bool result=false;
	if (n>1 && n%2!=0 && n%3!=0 || n==3)
	{
		result = true;
	}
	return result;
	
}