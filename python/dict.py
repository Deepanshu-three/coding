# data = input("data1:").split(",")
# data1 = input("data2:").split(",")
# if len (data)==len(data1):
#     d = dict(zip(data,data1))
#     print(sorted(d.item()))
# else:
#     print("length should be equal")
    
data1=input("data1: ").split(",")
data2=input("data2: ").split(",")
d=dict(zip(data1,data2))
for k in sorted(d.item()):
    print(k,i)