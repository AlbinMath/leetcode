# LeetCode 3751: Total Waviness of Numbers in Range I

**LeetCode Problem #3751 — Total Waviness of Numbers in Range I**
Solve LeetCode Total Waviness of Numbers in Range I using Java and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Total Waviness of Numbers in Range I |
| LeetCode | #3751 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two integers  num1  and  num2  representing an  inclusive  range  [num1, num2] .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Total Waviness of Numbers in Range I**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Java

## Source Code
- [solution.java](./solution.java)

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
- [3753. Total Waviness of Numbers in Range II](../4128-total-waviness-of-numbers-in-range-ii/)
- [201. Bitwise AND of Numbers Range](../0201-bitwise-and-of-numbers-range/)
- [908. Smallest Range I](../0944-smallest-range-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/)
