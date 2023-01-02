a = int(input())

for i in range(2,a):
    if a%i==0:
        result = True
    else:
        result = False

if result:
    print("not prime")
else:
    print("prime")  