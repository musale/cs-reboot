"""
Doomsday Fuel.

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the
exotic matter involved. It starts as raw ore, then during processing, begins
randomly changing between forms, eventually reaching a stable form. There may
be multiple stable forms that a sample could ultimately reach, not all of which
are useful as fuel.

Commander Lambda has tasked you to help the scientists increase fuel creation
efficiency by predicting the end state of a given ore sample. You have
carefully studied the different structures that the ore can take and which
transitions it undergoes. It appears that, while random, the probability of
each structure transforming is fixed. That is, each time the ore is in 1 state,
it has the same probabilities of entering the next state (which might be the
same state).  You have recorded the observed transitions in a matrix. The
others in the lab have hypothesized more exotic forms that the ore can become,
but you haven't seen all of them.

Write a function answer(m) that takes an array of array of nonnegative ints
representing how many times that state has gone to the next state and return
an array of ints for each terminal state giving the exact probabilities of each
terminal state, represented as the numerator for each state, then the
denominator for all of them at the end and in simplest form. The matrix is at
most 10 by 10. It is guaranteed that no matter which state the ore is in, there
is a path from that state to a terminal state. That is, the processing will
always eventually end in a stable state. The ore starts in state 0. The
denominator will fit within a signed 32-bit integer during the calculation,
as long as the fraction is simplified regularly.

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 & s5 w/equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but w/different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, & unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in
the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].
"""
from __future__ import division

import fractions


def answer(m):
    """
    Using Markov Absorbing chains.

    - Order matrix so that rows start with terminal states.
    - Find R and Q
    - Calculate FR = (I-Q)^-1.
    """
    if m == [[0]]:
        probabilities = [1, 1]
    else:
        matrix = arrangeMatrix(m)
        matrixQ = findQ(matrix)
        matrixR = findR(matrix)
        matrixI = generateIdentity(len(matrixQ[0]))
        matrixA = subtractMatrices(matrixI, matrixQ)
        matrixF = getMatrixInverse(matrixA)
        matrixFR = multiplyMatricest(matrixF, matrixR)
        probabilities = getProbabilities(matrixFR[0])
    return probabilities


def findQ(matrix):
    """The sub matrix from the ordered matrix."""
    matrixLength = len(matrix)
    filteredMatrix = filter(lambda m: sum(m) != 0, matrix)
    filteredMatrixLength = len(filteredMatrix)
    nonTerminalLength = matrixLength - filteredMatrixLength
    matrixQ = []
    for value in filteredMatrix:
        matrixQ.append(value[nonTerminalLength:])
    return matrixQ


def findR(matrix):
    """The sub matrix from the ordered matrix."""
    matrixLength = len(matrix)
    filteredMatrix = filter(lambda m: sum(m) != 0, matrix)
    filteredMatrixLength = len(filteredMatrix)
    nonTerminalLength = matrixLength - filteredMatrixLength
    matrixR = []
    for value in filteredMatrix:
        matrixR.append(value[:nonTerminalLength])
    return matrixR


def generateIdentity(size):
    """Generate an identity matrix based on the size supplied."""
    identity = []
    tracker = 0
    for i in range(size):
        row = [0] * size
        if i == tracker:
            row[i] = 1
            tracker += 1
        identity.append(row)
    return identity


def subtractMatrices(matrixA, matrixB):
    """Subtract 2 square matrices."""
    return map(lambda i: map(lambda x, y: x - y, matrixA[i], matrixB[i]),
               xrange(len(matrixA)))


def multiplyMatricest(m1, m2):
    """Multiply matrices."""
    r, m = [], []
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            sums = 0
            for k in range(len(m2)):
                sums = sums + (m1[i][k] * m2[k][j])
            r.append(sums)
        m.append(r)
        r = []
    return m


def findFR(I, Q):
    """To find FR=(I-Q)^-1. Find inverse of Identinty - matrixQ."""
    return I, Q


def transposeMatrix(m):
    """Transpose matrix."""
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t


def getMatrixMinor(m, i, j):
    """Get matrix minor."""
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def getMatrixDeternminant(m):
    """Get a matrix determinant."""
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c) * m[0][c] * \
            getMatrixDeternminant(getMatrixMinor(m, 0, c))
    return determinant


def getMatrixInverse(m):
    """Get a matrix inverse."""
    determinant = getMatrixDeternminant(m)
    # special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                [-1 * m[1][0] / determinant, m[0][0] / determinant]]

    # find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1)**(r + c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors


def getProbabilities(aList):
    """Get the numerators from the top value of the FR matrix."""
    probabilityList = []
    denominators = []
    for value in aList:
        denominators.append(
            fractions.Fraction(value).limit_denominator().denominator)
    lcm = leastCommonMultiple(*denominators)
    for value in aList:
        denominator = fractions.Fraction(value).limit_denominator().denominator
        numerator = fractions.Fraction(value).limit_denominator().numerator
        probabilityList.append(int((numerator * lcm) / denominator))
    probabilityList.append(lcm)
    return probabilityList


def leastCommonMultiple(*numbers):
    """Return lowest common multiple."""
    def lcm(a, b):
        return (a * b) // fractions.gcd(a, b)
    return reduce(lcm, numbers, 1)


def arrangeMatrix(matrix):
    """Arrange matrix."""
    matrixWithTerminalFirst = []
    terminalIndexes = []
    nonTerminalIndexes = []
    for key, column in enumerate(matrix):
        newRow = []
        if all([v == 0 for v in column]):
            # add the state to terminal indexes
            terminalIndexes.append(key)
            for j in column:
                newRow.append(0)
            # newRow[key] = 1
            matrixWithTerminalFirst.append(newRow)
        else:
            # add to nonTerminalIndexes
            nonTerminalIndexes.append(key)
    terminalIndexes.extend(nonTerminalIndexes)
    filteredMatrix = filter(lambda m: sum(m) != 0, matrix)
    for value in filteredMatrix:
        newRow = []
        rowSum = sum(value)
        for _, index in enumerate(terminalIndexes):
            newRow.append(value[index] / rowSum)
        matrixWithTerminalFirst.append(newRow)

    return matrixWithTerminalFirst


if __name__ == '__main__':
    # TEST 1
    m1 = [
            [0, 2, 1, 0, 0],
            [0, 0, 0, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
    a1 = [7, 6, 8, 21]

    # TEST 2
    m2 = [
            [0, 1, 0, 0, 0, 1],
            [4, 0, 0, 3, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
    a2 = [0, 3, 2, 9, 14]

    ordered1 = answer(m1)
    ordered2 = answer(m2)
    print ordered1,  a1
    print ordered2,  a2
