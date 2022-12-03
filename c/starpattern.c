#include <stdio.h>
void star(int rows)
{
    for (int i = 0; i < rows; i++)
    {
        for (int k = 0; k >=  (rows-i ); k++)
        {
            printf("  ");
        }
         
        for (int j = 0; j <=i ; j++)
        {
            printf("*");
        }
        printf("\n");
      
    }
    
    
    
    
}
void reversestar(int rows)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j <= rows-i-1 ; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    
}
int main()
{
    int rows, num;
    printf("enter 0 for triangular and 1 for reverse or q to quit\n",num);
    scanf("%d", &num);
    printf("enter the number u want star pattern of \n");
    scanf("%d", &rows);

    switch (num)
    {
    case 0:
       star(rows);

        break;
    case 1:

        reversestar(rows);

    default:
        printf('YOU HAVE ENTERED INVALID CHOICE');
        break;
    }
    return 0;
}