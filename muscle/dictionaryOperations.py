"""Exercises that would require dictionary exercise."""

# 1. We have two sorted lists, and we want to write a function to merge
# the two lists into one sorted list


# 1a. We can pop the values into a new list and then merge with + operator
def popValues():
    """Get the firstList and secondList and then pop the values."""
    firstList = [3, 4, 6, 10, 11, 18]
    secondList = [1, 5, 7, 12, 13, 19, 21]
    newList = []
    while firstList and secondList:
        if firstList[0] < secondList[0]:
            newList.append(firstList.pop(0))
        else:
            newList.append(secondList.pop(0))
    return newList + firstList + secondList


def extendValues():
    """Using list.extend() function."""
    firstList = [3, 4, 6, 10, 11, 18]
    secondList = [1, 5, 7, 12, 13, 19, 21]
    firstList.extend(secondList)
    return sorted(firstList)


if __name__ == '__main__':
    print popValues()
    print extendValues()
