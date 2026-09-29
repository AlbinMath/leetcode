# Minimum Moves To Make Array Complementary

## Problem Explanation
Given an even-length array `nums` and integer `limit`, you can replace any element with a value in `[1, limit]`. Find the minimum number of replacements so that `nums[i] + nums[n-1-i]` is the same for all pairs.

## How the Code Works
The code uses a **Difference Array** technique to efficiently calculate the cost for every possible target sum.

1. For each pair `(a, b)`, determine the ranges of target sums achievable with 0, 1, or 2 replacements.
2. Use a difference array to mark these ranges: target sum = `a+b` needs 0 moves, sums in `[min(a,b)+1, max(a,b)+limit]` need 1 move, all others need 2.
3. Sweep through the difference array to find the target sum with minimum total moves.

Time complexity is $O(N + \text{limit})$ and space complexity is $O(\text{limit})$.
