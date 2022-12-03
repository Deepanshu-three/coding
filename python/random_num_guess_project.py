import random
randnumber = random.randint(1,100)
userguess = None
guesses = 0

while(userguess!=randnumber):
    userguess = int(input("Enter your guess: "))
    guesses+=1
    if (userguess>randnumber):
        print("You have guessed it wronge! Enter a smaller nnumber")
    else:
        print("You have guessed it wronge! Enter a larger number")

print(f"You guess the number is {guesses} guesses")
with open("highscore.txt","r") as f:
    highscore = int(f.read())
    
if(guesses<highscore):
    print("You have just broken the highscore!")
    with open("highscore.txt","w") as f:
        f.write(str(guesses))    
