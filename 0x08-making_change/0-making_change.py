#!/usr/bin/python3
"""
Task: Change comes from within.
"""


def makeChange(coins, total):
    """
    Determines the fewest coins to meet a given amount
    """
    if total <= 0:
        return 0
    min_coins = [0] + [float('inf')] * total
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                num_coins = min_coins[i - coin] + 1
                if num_coins < min_coins[i]:
                    min_coins[i] = num_coins
    if min_coins[-1] == float("inf"):
        return -1
    return min_coins[total]
