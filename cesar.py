count = 0

encrypt = input("Input Text: ")
list1 = list(encrypt)
print(list1)

list2 = []
for i in list1:
    list2.extend(ord(char) for char in i)

print(list2)

while count != 26:
    for i in range(len(list2)):
        if list2[i] == 32:  # Check for space
            continue  # Skip increment for space
        if list2[i] == 33: #these lines check for special characters (like space, question mark)
            continue  
        if list2[i] == 44:
            continue  
        if list2[i] == 46:
            continue  
        if list2[i] == 63:
            continue  

        elif list2[i] == 90:
            list2[i] = 65
        elif list2[i] == 122:
            list2[i] = 97
        else:
            list2[i] += 1

    print(list2)
    count += 1
