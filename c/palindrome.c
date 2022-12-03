#include <stdio.h>
#include <string.h>

int ispal(int num)
{
    int reversed=0;
    int original = num;
    while (num!=0){
        reversed = reversed * 10 + num % 10;
        num = num/10;
    }
    printf("the reversed number is %d and ",reversed);

    if(reversed == original)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main()
{
    int number;
    printf("Enter a number u want to check if it is palindrome or not: ");
    scanf("%d",&number);
    if(ispal(number)){
        printf("the number is palindrome");
    }
    else{
        printf("the number is  not a plaindorme");
    }
    return 0;
}