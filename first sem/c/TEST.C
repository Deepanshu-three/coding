#include <stdio.h>
int main(int argc, char const *argv[])
{
    int rownum;
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
    return 0;
}
