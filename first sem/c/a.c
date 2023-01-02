#include <stdio.h>
#include <string.h>

void sort(char chr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = i+1; j < size ; j++)
        {
            if (chr[i] > chr[j])
            {
                int temp = chr[i];
                chr[i] = chr[j];
                chr[j] = temp;
            }
        }
    }
}
void print(char chr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%s \n", chr[i]);
    }
}

int main()
{
    char chr[100];
    int n;
    printf("enter the number :");
    scanf("%d", &n);
    getchar();

    for (int i = 0; i < n; i++)
    {
        printf("enter the character in array:");
        scanf("%s", &chr[i]);
        getchar();
    }

    sort(chr, n);
    print(chr, n);

    return 0;
}