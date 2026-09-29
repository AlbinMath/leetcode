# Find All Numbers Disappeared In An Array

## Problem Explanation
Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return an array of all the integers in `[1, n]` that do not appear in `nums`. The solution must run in $O(N)$ time without extra space (output array doesn't count).

## How the Code Works
The code uses the **array itself as a hash set** by negating values at corresponding indices.

1. **Mark Presence:** For each number `num` in the array, compute `index = |num| - 1` (using absolute value since values may already be negated). If `nums[index]` is positive, negate it to mark that the number `index + 1` exists in the array.
2. **Find Missing:** After marking, iterate through the array. If `nums[i]` is still positive, it means no number `i + 1` was encountered in the array, so `i + 1` is missing and gets pushed to the result.

Time complexity is $O(N)$ and space complexity is $O(1)$ (excluding the output array).
