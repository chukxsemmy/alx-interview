#!/usr/bin/python3

"""
Task: Change comes from within
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins
    needed to meet a given amount total
    """

    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        n = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    num_coin = 0
    for i in coins:
        if total % i == 0:
            num_coin += int(total / i)
            return coin_count
        if total - i >= 0:
            if int(total / i) > 1:
                num_coin += int(total / i)
                total = total % i
            else:
                num_coin += 1
                total -= i
                if total == 0:
                    break
    if total > 0:
        return -1
    return num_coin
