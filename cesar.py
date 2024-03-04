encrypt = input("Input Text: ")
list = list(encrypt)
print(list)

res = []
for i in list:
    res.extend(ord(num) for num in i)
print(res)
