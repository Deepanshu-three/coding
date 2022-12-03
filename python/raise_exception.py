def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("this is not valid")

a = increment('df364')
print(a)