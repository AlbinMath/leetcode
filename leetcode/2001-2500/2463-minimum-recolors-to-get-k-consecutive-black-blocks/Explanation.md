# LeetCode 2379: Minimum Recolors to Get K Consecutive Black Blocks

**LeetCode Problem #2379 — Minimum Recolors to Get K Consecutive Black Blocks**
Solve LeetCode Minimum Recolors to Get K Consecutive Black Blocks using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Recolors to Get K Consecutive Black Blocks |
| LeetCode | #2379 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  0-indexed  string  blocks  of length  n , where  blocks[i]  is either  &#39;W&#39;  or  &#39;B&#39; , representing the color of the  i th   block. The characters  &#39;W&#39;  and  &#39;B&#39;  denote the colors white and black, respectively.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Recolors to Get K Consecutive Black Blocks**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [995. Minimum Number of K Consecutive Bit Flips](../../1001-1500/1037-minimum-number-of-k-consecutive-bit-flips/)
- [1703. Minimum Adjacent Swaps for K Consecutive Ones](../../1501-2000/1805-minimum-adjacent-swaps-for-k-consecutive-ones/)
- [1413. Minimum Value to Get Positive Step by Step Sum](../../1501-2000/1514-minimum-value-to-get-positive-step-by-step-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/)
