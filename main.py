def removeEvens(k):
    NewList = k
    numPop = 0
    for i in range (0, len(k)):
        if NewList[i - numPop] % 2 == 0 and newList[i - numPop] != 0:
            NewList.pop(i - numPop)
            numPop = numPop + 1
    return NewList

print (removeEvens([1, 2, 3, 4, 5, 6]))
