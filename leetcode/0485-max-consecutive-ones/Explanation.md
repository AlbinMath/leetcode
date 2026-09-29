# Max Consecutive Ones

## Problem Explanation
Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

For example, `nums = [1,1,0,1,1,1]` → the answer is `3` (the last three `1`s).

## How the Code Works
The code uses a simple **single-pass counting** approach.

1. It maintains two variables: `current` (the length of the current streak of `1`s) and `max` (the longest streak seen so far).
2. For each element:
   - If it's `1`, increment `current` and update `max` if `current` exceeds it.
   - If it's `0`, reset `current` to `0`.
3. Return `max`.

Time complexity is $O(N)$ and space complexity is $O(1)$.
