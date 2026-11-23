# LeetCode 1679: Max Number of K-Sum Pairs

**LeetCode Problem #1679 — Max Number of K-Sum Pairs**
Solve LeetCode Max Number of K-Sum Pairs using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Max Number of K-Sum Pairs |
| LeetCode | #1679 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  nums  and an integer  k .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Max Number of K-Sum Pairs**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [363. Max Sum of Rectangle No Larger Than K](../../0001-0500/0363-max-sum-of-rectangle-no-larger-than-k/)
- [3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K](../../3001-3500/3240-maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/)
- [1301. Number of Paths with Max Score](../../1001-1500/1234-number-of-paths-with-max-score/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/max-number-of-k-sum-pairs/)
