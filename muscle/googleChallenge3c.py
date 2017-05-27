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


def answer(m):
    """
    Using Markov Absorbing chains.

    - Order matrix so that rows start with terminal states.
    - Find R and Q
    - Calculate FR = (I-Q)^-1
    """
    return m


def orderMatrixStartingWithTerminal(matrix):
    """Order matrix starting with terminal states. Insertion sorted."""
    for i in range(0, len(matrix) - 1):
        minIndex = i
        for j in range(i + 1, len(matrix)):
            if sum(matrix[j]) < sum(matrix[minIndex]):
                minIndex = j
            if minIndex != i:
                matrix[i], matrix[minIndex] = matrix[minIndex], matrix[i]
    # 1. findR and findQ
    matrixR = findR(matrix)
    matrixQ = findQ(matrix)
    matrixI = generateIdentity(len(matrixQ[0]))
    matrixA = subtractMatrices(matrixI, matrixQ)
    return matrixA


def findQ(matrix):
    """The sub matrix from the ordered matrix."""
    matrixLength = len(matrix)
    filteredMatrix = filter(lambda m: sum(m) != 0, matrix)
    filteredMatrixLength = len(filteredMatrix)

    nonTerminal = matrixLength - filteredMatrixLength
    matrixQ = []
    for value in filteredMatrix:
        q, total = [], float(sum(value))
        for i in range(nonTerminal - 1):
            q.extend([float(value[i])/total])
        matrixQ.append(q)
    return matrixQ


def findR(matrix):
    """The sub matrix from the ordered matrix."""
    matrixLength = len(matrix)
    filteredMatrix = filter(lambda m: sum(m) != 0, matrix)
    filteredMatrixLength = len(filteredMatrix)
    nonTerminal = matrixLength - filteredMatrixLength
    matrixR = []
    for value in filteredMatrix:
        r, total = [], sum(value)
        for i in range(1, nonTerminal + 1):
            r.extend([float(value[-i])/total])
        matrixR.append(list(reversed(r)))
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


def findFR(I, Q):
    """To find FR=(I-Q)^-1. Find inverse of Identinty - matrixQ."""
    return I, Q


if __name__ == '__main__':
    ordered = orderMatrixStartingWithTerminal(
        [
            [0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
        ])
    print ordered
