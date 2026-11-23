# LeetCode 2135: Count Words Obtained After Adding a Letter

**LeetCode Problem #2135 — Count Words Obtained After Adding a Letter**
Solve LeetCode Count Words Obtained After Adding a Letter using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Words Obtained After Adding a Letter |
| LeetCode | #2135 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two  0-indexed  arrays of strings  startWords  and  targetWords . Each string consists of  lowercase English letters  only.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Words Obtained After Adding a Letter**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [315. Count of Smaller Numbers After Self](../0315-count-of-smaller-numbers-after-self/)
- [2085. Count Common Words With One Occurrence](../2190-count-common-words-with-one-occurrence/)
- [2960. Count Tested Devices After Test Operations](../3220-count-tested-devices-after-test-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/)
