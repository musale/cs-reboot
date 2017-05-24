"""
Hamming distance.

Distance between two strings of equal length is the number of positions
at which the corresponding symbols are different.
"""


def hammingDistance(stringOne, stringTwo):
    """Get hamming distance between 2 strings."""
    if len(stringOne) != len(stringTwo):
        return "Strings should have the same distance"

    # using zip, create key, value pairs of the 2 strings and compare
    return sum(key != value for key, value in zip(stringOne, stringTwo))


if __name__ == '__main__':
    print hammingDistance("karolin", "kathrin")
    print hammingDistance("1011101", "1001001")
