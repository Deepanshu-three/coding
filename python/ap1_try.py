while True:
    print("press q to quit")
    a = input("Enter a number: ")
    if a=='q':
        break
    try:
        print("Trying...")
        if int(a)>9:
            print("U entered a two digit number!")
        else:
            print("U entered a one digit number!")
    except Exception as e:
        print(f"Your input resulted in erro try entering a number again")
    finally:
        print("Thanks for playing")

print("Thanks for playing") 