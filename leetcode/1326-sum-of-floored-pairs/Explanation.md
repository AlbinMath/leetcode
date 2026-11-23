# LeetCode 1862: Sum of Floored Pairs

**LeetCode Problem #1862 — Sum of Floored Pairs**
Solve LeetCode Sum of Floored Pairs using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Floored Pairs |
| LeetCode | #1862 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer array  nums , return the sum of  floor(nums[i] / nums[j])  for all pairs of indices  0 <= i, j < nums.length  in the array. Since the answer may be too large, return it  modulo   10 9  + 7 .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Sum of Floored Pairs**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [677. Map Sum Pairs](../0677-map-sum-pairs/)
- [1679. Max Number of K-Sum Pairs](../1798-max-number-of-k-sum-pairs/)
- [1835. Find XOR Sum of All Pairs Bitwise AND](../1963-find-xor-sum-of-all-pairs-bitwise-and/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-floored-pairs/)
