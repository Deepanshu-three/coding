#include<stdio.h>

int main()
{
    int a,b=1;
    printf("enter the number \n");
    scanf("%d",&a);
    do
    {
        printf("%d*%d=%d \n",a,b,a*b);
        b++;
        
    } while (b<=10);
    
}