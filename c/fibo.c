#include <stdio.h>

int main(){
    int n,a=0,b=1,sum,i;
    printf("input the number u want the series of \n");
    scanf("%d",&n);
   
    for (int i = 0; i < n; i++)
    {
        if (i<=1)
        
            sum=i;
        
        else{
            sum=a+b;
            a=b;
            b=sum;
           
        }
        printf("%d \n",sum);
    }
    
    return 0;    
}