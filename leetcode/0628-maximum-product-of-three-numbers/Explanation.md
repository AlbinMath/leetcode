# Maximum Product Of Three Numbers

## Problem Explanation
Given an integer array `nums`, find three numbers whose product is maximum and return that product. The array may contain negative numbers.

For example, `nums = [1,2,3]` → `6`, but `nums = [-100,-98,1,2,3]` → `29400` (from `-100 * -98 * 3`).

## How the Code Works
The code uses **sorting** and considers two possible candidates for the maximum product:

1. **Sort the Array:** Sort `nums` in ascending order.
2. **Two Candidates:**
   - `a * b * c` — the product of the three largest numbers (last three elements in the sorted array).
   - `a * x * y` — the product of the largest number and the two smallest numbers (first two elements). This handles the case where two large negative numbers multiply to give a large positive result.
3. Return the maximum of these two candidates.

Time complexity is $O(N \log N)$ for sorting and space complexity is $O(\log N)$.
