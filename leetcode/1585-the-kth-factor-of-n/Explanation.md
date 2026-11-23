# LeetCode 1492: The kth Factor of n

**LeetCode Problem #1492 — The kth Factor of n**
Solve LeetCode The kth Factor of n using Kotlin, Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The kth Factor of n |
| LeetCode | #1492 |
| Difficulty | Medium |
| Language | Kotlin, Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two positive integers  n  and  k . A factor of an integer  n  is defined as an integer  i  where  n % i == 0 .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **The kth Factor of n**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Kotlin, Python

## Source Code
- [solution.kt](./solution.kt)
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
- [215. Kth Largest Element in an Array](../0215-kth-largest-element-in-an-array/)
- [230. Kth Smallest Element in a BST](../0230-kth-smallest-element-in-a-bst/)
- [378. Kth Smallest Element in a Sorted Matrix](../0378-kth-smallest-element-in-a-sorted-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-kth-factor-of-n/)
