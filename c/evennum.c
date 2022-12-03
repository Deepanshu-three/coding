#include <stdio.h>

void main(){

    int a,b=0;
    printf("enter the number u want to count even number to:");
    scanf("%d",&a);

    do
    {
        printf("%d\n",b);
        b=b+2;
    } while (b<=a);
    
    
}