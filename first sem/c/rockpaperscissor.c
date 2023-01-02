#include <stdio.h>
#include <string.h>
#include <time.h>

int generaterandomnumber(int n)
{
    srand(time(NULL));
    return srand() % n;
}
int greater(char c1, char c2)
{

    if (c1 == c2)
    {
        return -1;
    }
    else if ((c1 == 'r') && (c2 == 's'))
    {
        return 1;
    }
    else if ((c2 == 'r') && (c1 == 's'))
    {
        return 0;
    }
    else if ((c1 == 'p') && (c2 == 'r'))
    {
        return 1;
    }
    else if ((c2 == 'p') && (c1 == 'r'))
    {
        return 0;
    }
    else if ((c1 == 's') && (c2 == 'p'))
    {
        return 1;
    }
    else if ((c2 == 's') && (c1 == 'p'))
    {
        return 0;
    }
}

int main()
{
    int playerscore = 0, compscore = 0, temp;
    char playerchar, compchar;
    char dict[] = {'r', 's', 'p'};

    printf("welcome to rock paper scissor\n");
    for (int i = 0; i < 3; i++)
    {
        printf("player turn\n");
        printf("choose 1 for rock 2 for scissor and 3 for paper\n");
        scanf("%d", &temp);
        getchar();
        playerchar = dict[temp - 1];
        printf("you chose %c \n\n", playerchar);

        printf("computer turn\n");
        printf("choose 1 for rock 2 for scissor and 3 for paper\n");
        temp = generaterandomnumber(3) + 1;
        compchar = dict[temp - 1];
        printf("computer chose %c \n\n", compchar);

        if (greater(compchar, playerchar) == 1)
        {
            compscore += 1;
            printf("computer got it \n");
        }

        else if (greater(compchar, playerchar) == -1)
        {
            printf("its a draw \n");
        }
        else
        {
            playerscore += 1;
            printf("you got it \n");
        }
        printf("you : %d \ncomputer : %d \n", playerscore, compscore);
    }

    if (playerscore > compscore)
    {
        printf("you win the game \n");
    }
    else if (playerscore < compscore)
    {
        printf("computer wins the game\n");
    }
    else
    {
        printf("its a draw\n");
    }

    return 0;
}