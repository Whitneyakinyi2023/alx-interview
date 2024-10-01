#!/usr/bin/python3
"""prime"""


def sieve_of_eratosthenes(n):
    """Function for sieving"""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return sieve


def play_game(n, primes):
    """Play game function"""
    remaining = set(range(1, n + 1))
    maria_turn = True
    while True:
        # Find the smallest prime number still in the set
        prime_to_pick = None
        for num in sorted(remaining):
            if primes[num]:  # Check if it's a prime
                prime_to_pick = num
                break
        if prime_to_pick is None:
            # No prime left, current player loses
            return "Ben" if maria_turn else "Maria"
        # Remove the prime and its multiples
        for multiple in range(prime_to_pick, n + 1, prime_to_pick):
            remaining.discard(multiple)
        # Switch turns
        maria_turn = not maria_turn


def isWinner(x, nums):
    """Function to determine who is the winner"""
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_game(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
