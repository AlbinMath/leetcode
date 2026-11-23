# LeetCode 3950: Exactly One Consecutive Set Bits Pair

**LeetCode Problem #3950 — Exactly One Consecutive Set Bits Pair**
Solve LeetCode Exactly One Consecutive Set Bits Pair using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Exactly One Consecutive Set Bits Pair |
| LeetCode | #3950 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  n .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Exactly One Consecutive Set Bits Pair**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [3480. Maximize Subarrays After Removing One Conflicting Pair](../../3501-4000/3789-maximize-subarrays-after-removing-one-conflicting-pair/)
- [3963. Create Grid With Exactly One Path](../../4001-4500/4342-create-grid-with-exactly-one-path/)
- [3821. Find Nth Smallest Integer With K One Bits](../../4001-4500/4189-find-nth-smallest-integer-with-k-one-bits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/)
