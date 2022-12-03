#include <stdio.h>

/*void func1(int array[])
{
    for (int i = 0; i < 10; i++)
    {
        printf("the value at %d in array is %d \n",i,array[i]);
    }
    
    return 0;
}*/
/*int func2(int *ptr)
{
    for (int i = 0; i < 10; i++)
    {
        printf("the value at %d of array is %d\n",i,ptr[i]);
    }
    
    return 0;
}*/

int func3(int arr[3][3])
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("the vaule at %d i and %d j is %d\n",i,j,arr[i][j]);
        }
        
    }
    
}

int main()
{
    int arr[3][3];
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("enter the value of %d in array j:",j);
            scanf("%d",&arr[i][j]);
        }
        
        
    }
    
    func3(arr);
    
  //  func2(arr);
   // func1(arr); //
    return 0;
}

