"""
Find the Access Codes.

In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need
access to it. But the only door leading to the LAMBCHOP chamber is secured with
a unique lock system whose number of passcodes changes daily. Commander Lambda
gets a report every day that includes the locks' access codes, but only she
knows how to figure out which of several lists contains the access codes. You
need to find a way to determine which list contains the access codes once
you're ready to go in.

Fortunately, now that you're Commander Lambda's personal assistant, she's
confided to you that she made all the access codes "lucky triples" in order to
help her better find them in the lists. A "lucky triple" is a tuple (x, y, z)
where x divides y and y divides z, such as (1, 2, 4). With that information,
you can figure out which list contains the number of access codes that matches
the number of locks on the door when you're ready to go in (for example, if
there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access
codes).

Write a function answer(l) that takes a list of positive integers l and counts
the number of "lucky triples" of (lst[i], lst[j], lst[k]) where i < j < k.
The length of l is between 2 and 2000 inclusive.  The elements of l are between
1 and 999999 inclusive.  The answer fits within a signed 32-bit integer. Some
of the lists are purposely generated without any access codes to throw off
spies, so if no triples are found, return 0.
"""


def answer(l):
    """
    Return count of lucky triples.

    - Maintain a tempValues[i] for each item on the list representing the
    number of previous integers that divide l[i]
    - Loop through the list and test each integer l[j] with all previous
    item l[i], if l[j] divides l[i], you just add tempValues[i]
    to the luckyTriples.

    There exist exactly tempValues[j] items of l[i] such that
    l[i] divides l[j] and i < j
    """
    luckyTriples = 0
    tempValues = [0] * len(l)
    if len(l) >= 2 and len(l) <= 2000:
        for i in xrange(0, len(l)):
            j = 0
            for j in xrange(0, i):
                if l[i] % l[j] == 0:
                    tempValues[i] = tempValues[i] + 1
                    luckyTriples = luckyTriples + tempValues[j]
    return luckyTriples


if __name__ == '__main__':
    print answer([1, 2, 3, 4, 5, 6])
    print answer([1, 1, 1])
