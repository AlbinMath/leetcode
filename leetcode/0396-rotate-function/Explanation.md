# Rotate Function

## Problem Explanation
Given an integer array `nums` of length `n`, define the rotation function `F(k)` as:
`F(k) = 0 * nums[k] + 1 * nums[k+1] + ... + (n-1) * nums[k+n-1]` (indices are mod `n`).
Return the maximum value of `F(0), F(1), ..., F(n-1)`.

## How the Code Works
The code uses a mathematical relationship between consecutive rotation functions to compute all values in $O(N)$ time.

1. **Compute F(0) and Sum:** It first calculates the sum of all elements (`sum`) and `F(0) = 0*nums[0] + 1*nums[1] + ... + (n-1)*nums[n-1]`.
2. **Recurrence Relation:** There is a mathematical relationship: `F(k) = F(k-1) + sum - n * nums[n-k]`. This is derived from the observation that when rotating, every element's weight increases by 1 (adding `sum`), except the element that wraps around from the end to position 0 (which loses `n` times its value).
3. It iterates from `k = 1` to `k = n-1`, computing each `F(k)` using the formula and tracking the maximum.

Time complexity is $O(N)$ and space complexity is $O(1)$.
