def is_prime(n):
    """
    Check if a number is prime.

    Args:
    n (int): number to check

    Returns:
    bool: True if number is prime, False otherwise
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def integer_square_root(n):
    """
    Calculate the integer square root of a number.

    Args:
    n (int): number to find the square root of

    Returns:
    int: the largest integer less than or equal to the square root of n
    """
    x = n
    y = (x + 1) // 2

    while y < x:
        x = y
        y = (x + n // x) // 2

    return x


def check_number(n):
    """
    Check if a number can be written as the sum of a prime and twice a square.

    Args:
    n (int): number to check

    Returns:
    bool: True if the number can be expressed in the form, False otherwise
    """
    max_square = integer_square_root(n // 2)
    for i in range(max_square + 1):
        remainder = n - 2 * i**2
        if is_prime(remainder):
            return True
    return False


def smallest_odd_composite():
    """
    Find the smallest odd composite that cannot be written as the sum of a prime and twice a square.

    Returns:
    int: smallest odd composite that cannot be written in the form
    """
    n = 9
    while True:
        if not is_prime(n) and n % 2 != 0:
            if not check_number(n):
                return n
        n += 2


print(smallest_odd_composite())
