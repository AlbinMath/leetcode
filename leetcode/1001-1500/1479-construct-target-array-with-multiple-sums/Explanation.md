# LeetCode 1354: Construct Target Array With Multiple Sums

**LeetCode Problem #1354 — Construct Target Array With Multiple Sums**
Solve LeetCode Construct Target Array With Multiple Sums using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Construct Target Array With Multiple Sums |
| LeetCode | #1354 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array  target  of n integers. From a starting array  arr  consisting of  n  1&#39;s, you may perform the following procedure :

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Construct Target Array With Multiple Sums**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [3314. Construct the Minimum Bitwise Array I](../../3501-4000/3605-construct-the-minimum-bitwise-array-i/)
- [3315. Construct the Minimum Bitwise Array II](../../3501-4000/3611-construct-the-minimum-bitwise-array-ii/)
- [3875. Construct Uniform Parity Array I](../../4001-4500/4256-construct-uniform-parity-array-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/construct-target-array-with-multiple-sums/)
