def reduceTheNumber(number, k):
    stringLength = len(number)
    print(k)
    i = 0
    newString = ""
    if len(number) <= k:
        print("line7", number)
        newString = str(number)
        print("line9", newString)
        print("line10", i)
        return newString
    while i < len(number):
        sub_string = number[i:i+k]
        result = sub_string
        added = 0
        for char in sub_string:
            added += int(char)
            print(added)
        newString += str(added)
        print(result)
        print("line21", i)
        i += k
    print("line18", newString)
    # return newString
    print("line25", i)
    if len(newString) >= k:
        reduceTheNumber(newString, k)
        # print(newString)
        # return newString
    else:
        print(newString)
        return newString