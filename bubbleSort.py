"""Bubble sort algorithm."""

initial_list = [2, 7, 4, 1, 5, 3]


def bubbleSort(aList):
    """Take in an unsorted list, return a sorted list."""
    for i in range(0, len(aList) - 1):
        for j in range(0, len(aList) - 1 - i):
            if aList[j] > aList[j + 1]:
                aList[j], aList[j + 1] = aList[j + 1], aList[j]

    print "Sorted List {}".format(aList)


if __name__ == '__main__':
    bubbleSort(initial_list)
