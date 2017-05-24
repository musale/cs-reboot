"""Braille."""
import string

capitalLetter = [[0, 0], [0, 0], [0, 1]]
space = [[0, 0], [0, 0], [0, 0]]
brailleLetters = [
    [[1, 0], [0, 0], [0, 0]], [[1, 0], [1, 0], [0, 0]],
    [[1, 1], [0, 0], [0, 0]], [[1, 1], [0, 1], [0, 0]],
    [[1, 0], [0, 1], [0, 0]], [[1, 1], [1, 0], [0, 0]],
    [[1, 1], [1, 1], [0, 0]], [[1, 0], [1, 1], [0, 0]],
    [[0, 1], [1, 0], [0, 0]], [[0, 1], [1, 1], [0, 0]],
    [[1, 0], [0, 0], [1, 0]], [[1, 0], [1, 0], [1, 0]],
    [[1, 1], [0, 0], [1, 0]], [[1, 1], [0, 1], [1, 0]],
    [[1, 0], [0, 1], [1, 0]], [[1, 1], [1, 0], [1, 0]],
    [[1, 1], [1, 1], [1, 0]], [[1, 0], [1, 1], [1, 0]],
    [[0, 1], [1, 0], [1, 0]], [[0, 1], [1, 1], [1, 0]],
    [[1, 0], [0, 0], [1, 1]], [[1, 0], [1, 0], [1, 1]],
    [[0, 1], [1, 1], [0, 1]], [[1, 1], [0, 0], [1, 1]],
    [[1, 1], [0, 1], [1, 1]], [[1, 0], [0, 1], [1, 1]],
]
alphabet = string.ascii_lowercase


def answer(plaintext):
    """Take a plain text convert to braille."""
    brailleText = ""
    if len(plaintext) <= 50 and not hasNumbers(plaintext):
        brailleTextMatrices = []
        for letter in plaintext:
            if letter.isupper():
                brailleTextMatrices.append(capitalLetter)
            if letter == " ":
                brailleTextMatrices.append(space)
            if letter != " ":
                brailleTextMatrices.append(
                    brailleLetters[alphabet.index(letter.lower())])
        for matrix in brailleTextMatrices:
            brailleText += readMatrix(matrix)
    print brailleText


def hasNumbers(plainText):
    """Check the string has no numbers."""
    return any(char.isdigit() for char in plainText)


def readMatrix(matrix):
    """Read a matrix in the form [[0,0],[0,0],[0,0]] to a string 000000."""
    stringFormat = "{0}{1}{2}{3}{4}{5}"
    tempList = []
    for value in matrix:
        tempList.extend(value)

    return stringFormat.format(
        tempList[0], tempList[2], tempList[4], tempList[1], tempList[3],
        tempList[5])


if __name__ == '__main__':
    answer("code")
    answer("Code")
    answer("The quick brown fox jumped over the lazy dog")
    readMatrix([[0, 1], [2, 3], [4, 5]])
