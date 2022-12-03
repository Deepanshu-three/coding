#include <stdio.h>

int main()
{
    int a,b,c;

    printf("enter marks of science \n");
    scanf("%d", &a);
    printf("enter marks of maths \n");
    scanf("%d" , &b);
    printf("enter marks of computer \n");
    scanf("%d" , &c);

    if (a>=45 &&b>=45&&c>=45)
    {
        printf("you have passed in all subjects \n");   
    
    }
    else if (a>=45&&b>=45&&c<45)
    {
    
        printf("you have failed in computer \n");
    }
    else if (a>=45&&b<45&&c>=45)
    {
        printf("you have failed in maths \n");
    }
    else if (a<45&&b>=45&&c>=45)
    {
        printf("you have failed in science \n");
    }
    
    else if (a>=45&&b<45&&c<45)
    {
        printf("you have failed in maths and computer \n");
    }
    else if (a<45&&b>=45&&c<45){
        printf("you have failed in science and compter \n");
    }
    else if (a<45&&b<45&&c>=45){
        printf("you have failed in maths and science \n");
    }
    else{
        printf("you are failed in all the subjects \n");
    }

    return 0;    
    













}
