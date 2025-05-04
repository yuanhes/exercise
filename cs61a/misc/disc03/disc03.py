def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        print(n % 10)
        swipe(n // 10)
        print(n % 10)


def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    else:
        return n * skip_factorial(n - 2)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    if n == 2:
        return True
    else:
        return not dividable(n, int(n ** 0.5))

def dividable(n, m):
    """Returns True if n can be divided by positive number not greater than m.
    >>> dividable(25, 4)
    False
    >>> dividable(25, 5)
    True
    """
    assert n > m, "N must be greater than M."

    if m == 1:
        return False
    if n % m == 0:
        return True
    else:
        return dividable(n, m-1)

def is_prime_iter(n):
    assert n > 1
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who
        "*** YOUR CODE HERE ***"
        if has_seven(i) or i % 7 == 0:
            direction = - direction
        who = who + direction
        if who > k:
            who = 1
        elif who < 1:
            who = k
        return f(i+1, who, direction)
    return f(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)


#from karel.stanfordkarel import *
#
#def main():
#   # your code here...
#   if front_is_clear():
#      move()
#      if front_is_clear():
#         move()
#      main()
#      move()
#   else:
#      turn_left()
#      turn_left()
