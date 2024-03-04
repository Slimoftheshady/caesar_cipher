count = 0

def CheckSpecialChr(i):
    if i == 32:
        return i
    elif i == 33:
        return i
    elif i == 44:
        return i
    elif i == 46:
        return i
    elif i == 63:
        return i
    else:
        return i

encrypt = input("Input Text: ")
list1 = list(encrypt)
print(list1)

list2 = []
for i in list1:
    list2.extend(ord(char) for char in i)

print(list2)

while count != 26:
    for i in range(len(list2)):
        list2[i] = CheckSpecialChr(list2[i])
        if list2[i] == 90:
            list2[i] = 65
        elif list2[i] == 122:
            list2[i] = 97
        else:
            list2[i] += 1

    print(list2)
    count += 1