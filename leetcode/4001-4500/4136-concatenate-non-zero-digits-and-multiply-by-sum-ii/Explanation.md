# LeetCode 3756: Concatenate Non-Zero Digits and Multiply by Sum II

**LeetCode Problem #3756 — Concatenate Non-Zero Digits and Multiply by Sum II**
Solve LeetCode Concatenate Non-Zero Digits and Multiply by Sum II using Java and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Concatenate Non-Zero Digits and Multiply by Sum II |
| LeetCode | #3756 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a string  s  of length  m  consisting of digits. You are also given a 2D integer array  queries , where  queries[i] = [l i , r i ] .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **SQL Query / Relational Join & Grouping**. By maintaining state efficiently in a **Relational Table**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Concatenate Non-Zero Digits and Multiply by Sum II**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Java

## Source Code
- [solution.java](./solution.java)

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [3754. Concatenate Non-Zero Digits and Multiply by Sum I](../../4001-4500/4135-concatenate-non-zero-digits-and-multiply-by-sum-i/)
- [1281. Subtract the Product and Sum of Digits of an Integer](../../1001-1500/1406-subtract-the-product-and-sum-of-digits-of-an-integer/)
- [1837. Sum of Digits in Base K](../../1501-2000/1965-sum-of-digits-in-base-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/)
