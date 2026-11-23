# LeetCode 2260: Minimum Consecutive Cards to Pick Up

**LeetCode Problem #2260 — Minimum Consecutive Cards to Pick Up**
Solve LeetCode Minimum Consecutive Cards to Pick Up using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Consecutive Cards to Pick Up |
| LeetCode | #2260 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  cards  where  cards[i]  represents the  value  of the  i th   card. A pair of cards are  matching  if the cards have the  same  value.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Consecutive Cards to Pick Up**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [3086. Minimum Moves to Pick K Ones](../3327-minimum-moves-to-pick-k-ones/)
- [995. Minimum Number of K Consecutive Bit Flips](../1037-minimum-number-of-k-consecutive-bit-flips/)
- [1703. Minimum Adjacent Swaps for K Consecutive Ones](../1805-minimum-adjacent-swaps-for-k-consecutive-ones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/)
