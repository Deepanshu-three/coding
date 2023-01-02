#include <stdio.h>

char main()
{
    char a;
    printf("enter subject which u have passed \n");


    scanf("%d" , &a);
    if (a="maths and science and computer ")
    {   
        printf("you have got a bumper price \n");
        
    }
    else if (a="maths and science")
    {
        printf("you got a book \n");
    }
    else if (a="maths and computer")
    {
        printf("you got a abescus\n");

    }
    else if (a="science and computer ")
    {
        printf("you got a research paper \n");
    }
    else if (a="maths"){
        printf("you got a geometery box \n");
    }
    else if (a="science"){
        printf("you got a telescope \n");
    }
    else if (a="computer"){
        printf("you got a mouse \n");
    }
    
    else {
        printf("WRONG SUB ENTERED \n");
    }
        return 0;
    
    
}



