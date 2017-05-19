"""Insertion sort algorithm."""

initial_list = [2, 7, 4, 1, 5, 3]


def insertionSort(aList):
    """Take in an unsorted list, return a sorted list by swapping."""
    for i in range(1, len(aList)):
        j = i - 1
        while aList[j] > aList[j + 1] and j >= 0:
            aList[j], aList[j + 1] = aList[j + 1], aList[j]
            j -= 1

    print "Sorted list: {}".format(aList)


def insertionSortComparing(aList):
    """Get a current value, compare and override if current Value is >."""
    for i in range(1, len(aList)):
        currentValue = aList[i]
        for j in range(i - 1, -1, -1):
            if aList[j] > aList[j + 1]:
                aList[j + 1] = aList[j]
            else:
                aList[j + 1] = currentValue
                break
    print "Sorted list: {}".format(aList)


if __name__ == '__main__':
    insertionSort(initial_list)
    insertionSortComparing(initial_list)
