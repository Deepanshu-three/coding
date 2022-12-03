#include <stdio.h>

int sum(int a, int b)
{
    return a + b;
}

void main()
{
    int a, b, num3;
    printf("ernter number 1 ", a);
    scanf("%d", &a);
    printf("enter number 2 ", b);
    scanf("%d", &b);
    num3 = sum(a, b);
    printf("the sume is %d", num3);
}
