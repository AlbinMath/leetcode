# LeetCode 1281: Subtract the Product and Sum of Digits of an Integer

**LeetCode Problem #1281 — Subtract the Product and Sum of Digits of an Integer**
Solve LeetCode Subtract the Product and Sum of Digits of an Integer using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Subtract the Product and Sum of Digits of an Integer |
| LeetCode | #1281 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an integer number  n , return the difference between the product of its digits and the sum of its digits.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Mathematical Simulation & Modular Arithmetic**. By maintaining state efficiently in a **Primitive Types**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Subtract the Product and Sum of Digits of an Integer**. Applying **Prefix Sum Precomputation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../1629-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
- [1837. Sum of Digits in Base K](../1965-sum-of-digits-in-base-k/)
- [1945. Sum of Digits of String After Convert](../2076-sum-of-digits-of-string-after-convert/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)
