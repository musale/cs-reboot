"""Selection sort algorithm."""
initial_list = [2, 7, 4, 1, 5, 3]


def sortList(aList):
    """Take in an unsorted list, returns a sorted list."""
    for i in range(0, len(aList) - 1):
        minIndex = i
        for j in range(i + 1, len(aList)):
            if aList[j] < aList[minIndex]:
                minIndex = j
            if minIndex != i:
                aList[i], aList[minIndex] = aList[minIndex], aList[i]

    print "Sorted List: {}".format(aList)


if __name__ == '__main__':
    sortList(initial_list)
