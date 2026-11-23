# LeetCode 3209: Number of Subarrays With AND Value of K

**LeetCode Problem #3209 — Number of Subarrays With AND Value of K**
Solve LeetCode Number of Subarrays With AND Value of K using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Subarrays With AND Value of K |
| LeetCode | #3209 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an array of integers  nums  and an integer  k , return the number of  subarrays  of  nums  where the bitwise  AND  of the elements of the subarray equals  k .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Subarrays With AND Value of K**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [2447. Number of Subarrays With GCD Equal to K](../../2501-3000/2546-number-of-subarrays-with-gcd-equal-to-k/)
- [2470. Number of Subarrays With LCM Equal to K](../../2501-3000/2557-number-of-subarrays-with-lcm-equal-to-k/)
- [992. Subarrays with K Different Integers](../../1001-1500/1034-subarrays-with-k-different-integers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/)
