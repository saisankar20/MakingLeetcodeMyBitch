def minNum(samDaily, kellyDaily, difference):
    # If Kelly does not solve more per day than Sam, she can never surpass Sam.
    if kellyDaily <= samDaily:
        return -1
    
    # Otherwise, find the smallest integer d that satisfies
    #   difference < d * (kellyDaily - samDaily)
    # which is difference // (kellyDaily - samDaily) + 1.
    return difference // (kellyDaily - samDaily) + 1
