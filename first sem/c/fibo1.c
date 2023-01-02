#include <stdio.h>
int main()
{
    int a=0,b=1;
    for (int i = 0; i <=10; i++)
    {
        int temp=a+b;
        printf("%d\n",temp);
        if(i%2==0){
            a=temp;
        }else{
            b=temp;
        }
    }
    
    return 0;
}