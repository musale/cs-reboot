"""Linear searching."""

aList = [23, 24, 72, 85, 49, 92, 27, 36, 62, 82]


def linearSearch(data, value):
    """Return value location if a value is found in data."""
    for key, item in enumerate(data):
        if item == value:
            return key
    return "{} not found".format(value)


if __name__ == '__main__':
    print "Found 24 at index {}".format(linearSearch(aList, 24))
    print "Not Found:  {}".format(linearSearch(aList, 25))
