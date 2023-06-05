# Smallest Odd Composite Finder

This Python script finds the smallest odd composite number that cannot be expressed as the sum of a prime number and twice a square.

## Description

This script uses a brute-force method to check each odd composite number starting from 9 (the smallest odd composite) to find a number that cannot be expressed as the sum of a prime and twice a square.

The main functions in this script are:

- `is_prime(n)`: Checks if a number `n` is prime.
- `integer_square_root(n)`: Computes the integer square root of a number `n`.
- `check_number(n)`: Checks if a number `n` can be written as the sum of a prime and twice a square.
- `smallest_odd_composite()`: Finds the smallest odd composite number that cannot be written as the sum of a prime and twice a square.
