"""Exercises that would require dictionary exercise."""
from collections import defaultdict


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

# 2. Get word frequency


ss = """I figured it out
I figured it out from black and white
Seconds and hours
Maybe they had to take some time"""


def fromKeys():
    """Get the sentence, split it into a list using spaces."""
    words = ss.split()
    # Initialize dictionary with word as key and count as zero
    newDict = {}.fromkeys(words, 0)
    for word in words:
        newDict[word] += 1
    return newDict


# 3.  make a dictionary with the number of digits as the key
# and list of numbers the value


justNumbers = [1, 2, 4, 8, 16, 32, 64, 128,
               256, 512, 1024, 32768, 65536, 4294967296]


def getNumberCounts():
    """Get the number counts using using collections.defaultdict(int)."""
    newDict = defaultdict(list)
    for num in justNumbers:
        newDict[len(str(num))].append(num)
    return newDict


if __name__ == '__main__':
    print popValues()
    print extendValues()
    print fromKeys()
    print getNumberCounts()
