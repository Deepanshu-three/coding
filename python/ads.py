n=int(input())
while(n>0):
    res=""
    temp=int(input())
    if 360%temp==0:
        res=res+"y "
    else:
        res=res+"n "
    if temp<=360:
        res=res+"y "
    else:
        res=res+"n "
    if (temp*(temp+1)/2)<=360:
        res=res+"y "
    else:
        res=res+"n "
    print(res)
    n=n-1
    12