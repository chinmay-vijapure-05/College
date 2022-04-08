// word and line count
#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp;
    char ch;
    fp = fopen("counting.txt","r");
    ch=getc(fp);
    int words=0, lines=0;
    while(ch!=EOF){
        if(ch==' ' || ch=='\n')
            words++;
        if(ch=='\n')
            lines++;
        ch=getc(fp);
    }
    printf("words: %d\nlines: %d\n",words+1,lines+1);
    fclose(fp);
    return 0;
}
