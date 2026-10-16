# LeetCode 2193: Minimum Number of Moves to Make Palindrome

**LeetCode Problem #2193 — Minimum Number of Moves to Make Palindrome**
Solve LeetCode Minimum Number of Moves to Make Palindrome using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Moves to Make Palindrome |
| LeetCode | #2193 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a string  s  consisting only of lowercase English letters.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Two Pointer Convergence & Scanning**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Number of Moves to Make Palindrome**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [1674. Minimum Moves to Make Array Complementary](../1793-minimum-moves-to-make-array-complementary/)
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../2753-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)
- [9. Palindrome Number](../0009-palindrome-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/)
