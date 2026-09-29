# Find Two Non Overlapping Sub Arrays Each With Target Sum

## Problem Explanation
Given an array of positive integers and a target, find two non-overlapping subarrays each with sum equal to target, minimizing the sum of their lengths. Return -1 if not possible.

## How the Code Works
The code uses a **Sliding Window** to find all subarrays with the target sum, combined with a DP approach to track the shortest valid subarray ending at or before each index. It then considers all valid pairs of non-overlapping subarrays and finds the minimum combined length.

Time complexity is $O(N)$ and space complexity is $O(N)$.
