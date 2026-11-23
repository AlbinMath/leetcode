# LeetCode 1593: Split a String Into the Max Number of Unique Substrings

**LeetCode Problem #1593 — Split a String Into the Max Number of Unique Substrings**
Solve LeetCode Split a String Into the Max Number of Unique Substrings using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split a String Into the Max Number of Unique Substrings |
| LeetCode | #1593 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a string  s  ,  return  the maximum number of unique substrings that the given string can be split into .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Split a String Into the Max Number of Unique Substrings**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [2767. Partition String Into Minimum Beautiful Substrings](../2883-partition-string-into-minimum-beautiful-substrings/)
- [2871. Split Array Into Maximum Number of Subarrays](../3080-split-array-into-maximum-number-of-subarrays/)
- [467. Unique Substrings in Wraparound String](../0467-unique-substrings-in-wraparound-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/)
