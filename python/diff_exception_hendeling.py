try:
    a = int(input())
    c = 1/a
# except Exception as e:
    # print("exception occur")
    # print(e)

except ValueError as e:
    print("Please enter a valid value")
    
except ZeroDivisionError as e:
    print("Please enter value other than zero")    
print("Thanks for using the code")