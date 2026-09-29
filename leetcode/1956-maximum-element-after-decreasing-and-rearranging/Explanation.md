# Maximum Element After Decreasing And Rearranging

## Problem Explanation
Given an array, you can rearrange it and decrease elements (but not increase). The first element must be 1, and adjacent elements can differ by at most 1. Return the maximum possible value of the last element.

## How the Code Works
1. **Sort** the array in ascending order.
2. Initialize `max = 0`. For each element, set `max = min(num, max + 1)`. This greedily builds the longest possible increasing sequence where each step increases by at most 1.
3. Return `max`.

Time complexity is $O(N \log N)$ and space complexity is $O(\log N)$ for sorting.
