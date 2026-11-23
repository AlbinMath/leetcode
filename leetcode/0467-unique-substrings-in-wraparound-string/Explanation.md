# LeetCode 467: Unique Substrings in Wraparound String

**LeetCode Problem #467 — Unique Substrings in Wraparound String**
Solve LeetCode Unique Substrings in Wraparound String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Unique Substrings in Wraparound String |
| LeetCode | #467 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
We define the string  base  to be the infinite wraparound string of  "abcdefghijklmnopqrstuvwxyz" , so  base  will look like this:

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Unique Substrings in Wraparound String**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [828. Count Unique Characters of All Substrings of a Given String](../0855-count-unique-characters-of-all-substrings-of-a-given-string/)
- [1593. Split a String Into the Max Number of Unique Substrings](../1715-split-a-string-into-the-max-number-of-unique-substrings/)
- [387. First Unique Character in a String](../0387-first-unique-character-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/unique-substrings-in-wraparound-string/)
