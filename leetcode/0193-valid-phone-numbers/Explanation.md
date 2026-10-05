# LeetCode 193: Valid Phone Numbers

**LeetCode Problem #193 — Valid Phone Numbers**
Solve LeetCode Valid Phone Numbers using Shell and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Phone Numbers |
| LeetCode | #193 |
| Difficulty | Easy |
| Language | Shell |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a text file  file.txt  that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The solution uses `grep -E` (extended regular expressions) to match lines that conform to one of the two valid formats:
- `^([0-9]{3}-[0-9]{3}-[0-9]{4})$` matches the format `xxx-xxx-xxxx`.
- `^(\([0-9]{3}\) [0-9]{3}-[0-9]{4})$` matches the format `(xxx) xxx-xxxx`.
- The `^` and `$` anchors ensure the entire line must match (no extra characters before or after).
- The `|` operator combines both patterns so either format is accepted.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Valid Phone Numbers**. Applying **Iterative Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Shell

## Source Code
- [solution.sh](./solution.sh)

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
- [3803. Count Residue Prefixes](../3803-find-products-with-valid-serial-numbers/)
- [2. Add Two Numbers](../0002-add-two-numbers/)
- [17. Letter Combinations of a Phone Number](../0017-letter-combinations-of-a-phone-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-phone-numbers/)
