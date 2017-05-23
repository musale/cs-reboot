"""Interpolation searching."""

aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def interpolationSearch(dataSet, value):
    """Find the value from the data set."""
    lowerIndex = 0
    upperIndex = len(dataSet) - 1

    while dataSet[lowerIndex] <= value and dataSet[upperIndex] >= value:
        midPoint = lowerIndex + (
            (upperIndex - lowerIndex) / (
                dataSet[upperIndex] - dataSet[lowerIndex])) * (
                    value - dataSet[lowerIndex])

        if dataSet[midPoint] < value:
            lowerIndex = midPoint + 1
        elif dataSet[midPoint] > value:
            upperIndex = midPoint - 1
        else:
            return "Found {} at index {}".format(value, midPoint)

    if dataSet[lowerIndex] == value:
        return "Found {} at index {}".format(value, lowerIndex)
    return "Not found {}".format(value)  # Index can be out of range


if __name__ == '__main__':
    print interpolationSearch(aList, 10)
    print interpolationSearch(aList, 14)
