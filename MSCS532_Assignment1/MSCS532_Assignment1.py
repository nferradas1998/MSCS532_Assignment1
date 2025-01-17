
def insertion_sort_monotonically_descending(numArr):
    print("initial array", numArr)
    for i in range(1, len(numArr)):
        current = numArr[i]
        print("current value being sorted: ",current, "at position ", i)
        position = i - 1

        while position >= 0 and numArr[position] < current:
            numArr[position + 1] = numArr[position]
            position -= 1

        numArr[position + 1] = current
        print("new order for the array after key was sorted: ", numArr)

    
    return numArr

arr = [2, 5, 9, 1, 3,6, 1, 0]
print("sorted array: ", insertion_sort_monotonically_descending(arr))