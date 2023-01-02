#include <stdio.h>
#include <string.h>
int main()
{
    int rownum;
    printf("enter the number  :");
    scanf("%d",&rownum);
    
    for (int i = 0; i < rownum; i++)
    {
        for (int space1 = 0; space1 < rownum - (rownum-i); space1++)
        {
            printf("  ");
        }
        for (int j = 0; j <= rownum-i-1 ; j++)
        {
            printf("* ");
        }
        printf("\n");
    }
    for (int rows = 0; rows <= rownum; rows++)
    {

               //space
        for (int space = 0; space < (rownum - rows); space++)
        {
            printf("  ");
        }
        //pattern

        for (int pattern = 0; pattern < rows; pattern++)
        {
            printf("* ");
        }
        printf("\n");
        
    }
    

    return 0;
}