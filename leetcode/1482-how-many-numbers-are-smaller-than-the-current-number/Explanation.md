# How Many Numbers Are Smaller Than The Current Number

## Problem Explanation
Given an array `nums`, for each element return how many numbers in the array are strictly smaller than it.

## How the Code Works
The code uses **Counting Sort + Prefix Sum** for an efficient $O(N)$ solution.

1. **Count Frequencies:** Count how many times each value `0–100` appears.
2. **Prefix Sum:** Transform the count array so `count[i]` = total numbers ≤ `i`.
3. **Build Result:** For each `num` in the original array, the count of numbers strictly smaller is `count[num - 1]` (or `0` if `num == 0`).

Time complexity is $O(N + K)$ where $K = 100$, and space complexity is $O(K)$.
