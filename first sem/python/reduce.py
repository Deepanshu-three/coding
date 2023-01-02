from functools import reduce
l = [1,2,3121,31,231,24,31,4,31,24,1,4]

a = reduce(max,l)
print(a)