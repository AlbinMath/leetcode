# LeetCode 2537: Count the Number of Good Subarrays

**LeetCode Problem #2537 — Count the Number of Good Subarrays**
Solve LeetCode Count the Number of Good Subarrays using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Good Subarrays |
| LeetCode | #2537 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer array  nums  and an integer  k , return  the number of  good  subarrays of   nums .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count the Number of Good Subarrays**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1248. Count Number of Nice Subarrays](../../1001-1500/1370-count-number-of-nice-subarrays/)
- [2588. Count the Number of Beautiful Subarrays](../../2501-3000/2656-count-the-number-of-beautiful-subarrays/)
- [2963. Count the Number of Good Partitions](../../3001-3500/3212-count-the-number-of-good-partitions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-good-subarrays/)
