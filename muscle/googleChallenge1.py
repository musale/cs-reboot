"""Braille Translation.

Because Commander Lambda is an equal-opportunity despot, she has several
visually-impaired minions. But she never bothered to follow intergalactic
standards for workplace accommodations, so those minions have a hard time
navigating her space station. You figure printing out Braille signs will help
them, and - since you'll be promoting efficiency at the same time - increase
your chances of a promotion.

Braille is a writing system used to read by touch instead of by sight. Each
character is composed of 6 dots in a 2x3 grid, where each dot can either be a
bump or be flat (no bump). You plan to translate the signs around the space
station to Braille so that the minions under Commander Lambda's command can
feel the bumps on the signs and "read" the text with their touch. The special
printer which can print the bumps onto the signs expects the dots in the
following order:
1 4
2 5
3 6

So given the plain text word "code", you get the Braille dots:

11 10 11 10
00 01 01 01
00 10 00 00

where 1 represents a bump and 0 represents no bump.  Put together, "code"
becomes the output string "100100101010100110100010".

Write a function answer(plaintext) that takes a string parameter and returns
a string of 1's and 0's representing the bumps and absence of bumps in the
input string. Your function should be able to encode the 26 lowercase letters,
handle capital letters by adding a Braille capitalization mark before that
character, and use a blank character (000000) for spaces. All signs on the
space station are less than fifty characters long and use only letters and
spaces.
"""
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
