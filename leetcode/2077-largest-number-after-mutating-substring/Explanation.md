# LeetCode 1946: Largest Number After Mutating Substring

**LeetCode Problem #1946 — Largest Number After Mutating Substring**
Solve LeetCode Largest Number After Mutating Substring using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Number After Mutating Substring |
| LeetCode | #1946 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a string  num , which represents a large integer. You are also given a  0-indexed  integer array  change  of length  10  that maps each digit  0-9  to another digit. More formally, digit  d  maps to digit  change[d] .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Largest Number After Mutating Substring**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1297. Maximum Number of Occurrences of a Substring](../1423-maximum-number-of-occurrences-of-a-substring/)
- [1456. Maximum Number of Vowels in a Substring of Given Length](../1567-maximum-number-of-vowels-in-a-substring-of-given-length/)
- [1624. Largest Substring Between Two Equal Characters](../1746-largest-substring-between-two-equal-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-number-after-mutating-substring/)
