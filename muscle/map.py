"""Using map, reduce, filter and lambda."""


# 1. Using map, filter, reduce, write a code that create a list of (n)**2
# for range(10) for even integers

# 1a. get the list of even numbers using filter
evenNumbers = filter(lambda x: x % 2 == 0, [num for num in range(1, 11)])

# 1b. get the powers of the list
poweredList = map(lambda x: x**2, evenNumbers)

# 1c. get sum of poweredList using reduce
summedList = reduce(lambda x, y: x + y, poweredList)

if __name__ == '__main__':
    print poweredList
    print summedList
