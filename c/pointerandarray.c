#include <stdio.h>
int main()
{
    int arr[]={11,22,33,44};
    printf("%d\n",arr[0]);
    printf("%d\n", *(&arr+1));
    return 0;
}