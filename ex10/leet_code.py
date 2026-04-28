from math import comb, factorial
from itertools import product

def getProbability(balls):
    k    = len(balls)
    n    = sum(balls) // 2   # each box gets n balls

    # Total ways to split 2n balls into two groups of n
    total_ways = comb(sum(balls), n)

    favorable = 0

    # Try all ways to assign how many balls of each color go to box1
    # split[i] = number of balls of color i going to box 1
    def backtrack(idx, box1_count, box1_distinct, box2_distinct, ways):
        nonlocal favorable

        if idx == k:
            if box1_count == n and box1_distinct == box2_distinct:
                favorable += ways
            return

        for x in range(balls[idx] + 1):          # x balls of color idx → box1
            y = balls[idx] - x                   # rest → box2
            new_ways        = ways * comb(balls[idx], x)
            new_b1_distinct = box1_distinct + (1 if x > 0 else 0)
            new_b2_distinct = box2_distinct + (1 if y > 0 else 0)
            backtrack(idx + 1,
                      box1_count + x,
                      new_b1_distinct,
                      new_b2_distinct,
                      new_ways)

    backtrack(0, 0, 0, 0, 1)

    return favorable / total_ways

# Tests
print(getProbability([1, 1]))           # 1.0
print(getProbability([2, 1, 1]))        # 0.6667
print(getProbability([1, 2, 1, 2]))     # 0.5909