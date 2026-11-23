# LeetCode 1771: Maximize Palindrome Length From Subsequences

**LeetCode Problem #1771 — Maximize Palindrome Length From Subsequences**
Solve LeetCode Maximize Palindrome Length From Subsequences using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Palindrome Length From Subsequences |
| LeetCode | #1771 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two strings,  word1  and  word2 . You want to construct a string in the following manner:

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Two Pointer Convergence & Scanning**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximize Palindrome Length From Subsequences**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
Python

## Source Code
- [solution.py](./solution.py)

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
- [1930. Unique Length-3 Palindromic Subsequences](../../2001-2500/2059-unique-length-3-palindromic-subsequences/)
- [2002. Maximum Product of the Length of Two Palindromic Subsequences](../../2001-2500/2130-maximum-product-of-the-length-of-two-palindromic-subsequences/)
- [2259. Remove Digit From Number to Maximize Result](../../2001-2500/2337-remove-digit-from-number-to-maximize-result/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/)
