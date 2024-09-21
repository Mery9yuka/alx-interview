#!/usr/bin/python3
"""function that calculate the fewest
   nb of coins needed to meet a given total
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        minCoin = 0
        for j in coin:
            while(total >= j):
                minCoin += 1
                total -= j
        if total == 0:
            return minCoin
        return -1
