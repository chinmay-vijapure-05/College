#include<stdio.h>

int main()
{
	int x = 87;
	char s[100];
	for(int i=0; i<100; i++){
		s[i] = i+'0';
	}
	printf("%s\n", s);

	return 0;
}