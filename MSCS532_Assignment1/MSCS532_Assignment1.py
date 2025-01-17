
def insertion_sort_monotonically_descending(numArr):
    for i in range(1, len(numArr)):
        current = numArr[i]
        position = i - 1

        while position >= 0 and numArr[position] < current:
            numArr[position + 1] = numArr[position]
            position -= 1

        numArr[position + 1] = current
    
    return numArr