# LeetCode 1247: Minimum Swaps to Make Strings Equal

**LeetCode Problem #1247 — Minimum Swaps to Make Strings Equal**
Solve LeetCode Minimum Swaps to Make Strings Equal using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Swaps to Make Strings Equal |
| LeetCode | #1247 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two strings  s1  and  s2  of equal length consisting of letters  "x"  and  "y"   only . Your task is to make these two strings equal to each other. You can swap any two characters that belong to  different  strings, which means: swap  s1[i]  and  s2[j] .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Swaps to Make Strings Equal**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1318. Minimum Flips to Make a OR b Equal to c](../../1001-1500/1441-minimum-flips-to-make-a-or-b-equal-to-c/)
- [1347. Minimum Number of Steps to Make Two Strings Anagram](../../1001-1500/1469-minimum-number-of-steps-to-make-two-strings-anagram/)
- [1790. Check if One String Swap Can Make Strings Equal](../../1501-2000/1915-check-if-one-string-swap-can-make-strings-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/)
