# LeetCode 3658: GCD of Odd and Even Sums

**LeetCode Problem #3658 — GCD of Odd and Even Sums**
Solve LeetCode GCD of Odd and Even Sums using Kotlin and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | GCD of Odd and Even Sums |
| LeetCode | #3658 |
| Difficulty | Easy |
| Language | Kotlin |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  n . Your task is to compute the  GCD  (greatest common divisor) of two values:

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **GCD of Odd and Even Sums**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Kotlin

## Source Code
- [solution.kt](./solution.kt)

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
- [1116. Print Zero Even Odd](../1216-print-zero-even-odd/)
- [3220. Odd and Even Transactions](../3530-odd-and-even-transactions/)
- [1252. Cells with Odd Values in a Matrix](../1378-cells-with-odd-values-in-a-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/gcd-of-odd-and-even-sums/)
