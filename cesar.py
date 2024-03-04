count = 1

encrypt = input("Input Text: ")
list1 = list(encrypt)


list2 = []
for i in list1:
    list2.extend(ord(char) for char in i)

while count != 26:
    for i in range(len(list2)):
        if list2[i] == 32 or list2[i] in [33, 44, 46, 63]:  #Checks for special characters e.g space, question mark
            continue #runs through loop, only works in a loop

        if list2[i] == 90:
            list2[i] = 65
        elif list2[i] == 122:
            list2[i] = 97
        else:
            list2[i] += 1

    text_list = [chr(val) for val in list2]
    print("Letters Plus " + str(count) + ": ", ''.join(text_list))
    count += 1
