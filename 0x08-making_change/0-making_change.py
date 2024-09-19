#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    """Total change"""
    if total <= 0:
        return 0
    # Initialize dp array with a large number, meaning not achievable initially
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins to make 0 total
    # Dynamic programming to fill the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    # If dp[total] is still float('inf'), it means we couldn't form the total
    return dp[total] if dp[total] != float('inf') else -1
