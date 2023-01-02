n = int(input("Enter the number you want a table of: "))
for j in range(1,n+1):
    table = [j*i for i in range(1,11)]
    print(table)
    with open("table.txt","a") as f:
        f.write(str(table))
        f.write("\n") 