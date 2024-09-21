#!/usr/bin/python3
"""function that calculate the fewest
   nb of coins needed to meet a given total
"""

def makeChange(coins, total):
    if total <= 0:
        return 0
    
    min_c = [float('inf')] * (total + 1)
    min_c[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                min_c[i] = min(min_c[i], min_c[i - coin] + 1)

    return min_c[total] if min_c[total] != float('inf') else -1
