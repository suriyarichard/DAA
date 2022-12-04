def selectionSort( itemsList ):
    n = len( itemsList )
    for i in range( n - 1 ): 
        minValueIndex = i
        for j in range( i + 1, n ):
            if itemsList[j] < itemsList[minValueIndex] :
                minValueIndex = j
        if minValueIndex != i :
            temp = itemsList[i]
            itemsList[i] = itemsList[minValueIndex]
            itemsList[minValueIndex] = temp
    return itemsList

el = [45,87,12,32,9,60,11,5]
print("The unsorted list is: ", el)  
print("The sorted list is: ",selectionSort(el))
