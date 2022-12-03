import string
punctuation = string.punctuation

result = " "

str = "List [] , tuple () Dictionary{} comment"

for i in str:
    if i not in punctuation:
        result = result+i
        
print("set of paunctuation in string.punctuation is", punctuation)
print("string after removing all puntuation is", result)