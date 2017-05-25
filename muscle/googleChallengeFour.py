"""
Fuel Injection Perfection.

Commander Lambda has asked for your help to refine the automatic quantum
antimatter fuel injection system for her LAMBCHOP doomsday device. It's a great
chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit
of sabotage while you're at it - so you took the job gladly.

Quantum antimatter fuel comes in small pellets, which is convenient since the
many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a
time. However, minions dump pellets in bulk into the fuel intake. You need to
figure out the most efficient way to sort and shift the pellets down to a
single pellet at a time.

The fuel control mechanisms have three operations:

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy
released when a quantum antimatter pellet is cut in half, the safety controls
will only allow this to happen if there is an even number of pellets)

Write a function called answer(n) which takes a positive integer as a string
and returns the minimum number of operations needed to transform the number of
pellets to 1. The fuel intake control panel can only display a number up to
309 digits long, so there won't ever be more pellets than you can express in
that many digits.
"""


def answer(n):
    """
    Return minimum ops to convert n into 1.

    Using the binary representation of n and the Least Significant Bits,
    I determine if a number is odd or even.
    - if the least significant bit is zero, then divide by 2
    - if n is 3, or the 2 least significant bits are 01, then subtract
    - the other cases I add.
    """
    pellets = int(n)
    operations = 0
    while pellets > 1:
        if pellets % 2 == 0:
            pellets = pellets // 2
        elif pellets == 3 or pellets % 4 == 1:
            pellets = pellets - 1
        else:
            pellets = pellets + 1
        operations += 1
    return operations


if __name__ == '__main__':
    print answer("4")
    print answer("15")
