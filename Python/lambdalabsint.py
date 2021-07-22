# Find all the pairs of two integers in an unsorted array that sum up to a given S. 
# For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] 
# because 11 + -4 = 7 and 2 + 5 = 7.
def sumOf(listof):
    print(listof)
    answer = 7
    newList = []
    for i in range(len(listof)):
        print(i, listof[i])
        ival = listof[i]
        for j in range(i + 1, len(listof)):
            integers = ival + listof[j]
            # print(i , integers)
            semiList = []
            if integers == 7:
                semiList.append(ival)
                semiList.append(listof[j])
                newList.append(semiList)
                # print(semiList)
    print(newList)
listof = [3, 5, 2, -4, 8, 11]
result = sumOf(listof)