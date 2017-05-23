"""Binary searching."""

aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def binarySearch(dataSet, value):
    """Get the index of the searched value."""
    lowerBound = 0
    upperBound = len(dataSet) - 1
    found = False

    while not found:
        if upperBound < lowerBound:
            return "Not found {}".format(value)
        midPoint = (lowerBound + upperBound) // 2

        if dataSet[midPoint] < value:
            lowerBound = midPoint + 1

        if dataSet[midPoint] > value:
            upperBound = midPoint - 1

        if dataSet[midPoint] == value:
            found = True
            return "Found {} at index {}".format(value, midPoint)


if __name__ == '__main__':
    print "Found: {}".format(binarySearch(aList, 3))
    print "Not Found: {}".format(binarySearch(aList, 13))
