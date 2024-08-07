#!/usr/bin/env python3
"""
Minimum operations task
"""


def minOperations(n):
    # If n is less than 2, it's impossible to achieve more H(s), so return 0.
    if n < 2:
        return 0

    # Initialization of the number of operations to 0.
    operations = 0

    """ Because nothing less that 2 is possible we start
     factoring from 2 then work upwrds"""
    factor = 2

    # While n is greater than 1, we keep dividing it by the current factor.
    while n > 1:
        # While the current factor divides n, we keep
        # dividing and adding the factor to operations.
        while n % factor == 0:
            # Add the current factor to the operations
            # (each factor represents a copy-paste sequence).
            operations += factor
            # Divide n by the current factor.
            n //= factor
        # Move to the next factor.
        factor += 1

    return operations
