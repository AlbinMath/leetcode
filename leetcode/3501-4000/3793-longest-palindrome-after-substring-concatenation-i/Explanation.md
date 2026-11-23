# LeetCode 3503: Longest Palindrome After Substring Concatenation I

**LeetCode Problem #3503 — Longest Palindrome After Substring Concatenation I**
Solve LeetCode Longest Palindrome After Substring Concatenation I using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Palindrome After Substring Concatenation I |
| LeetCode | #3503 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two strings,  s  and  t .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Two Pointer Convergence & Scanning**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Palindrome After Substring Concatenation I**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [1493. Longest Subarray of 1's After Deleting One Element](../../1501-2000/1586-longest-subarray-of-1s-after-deleting-one-element/)
- [1946. Largest Number After Mutating Substring](../../2001-2500/2077-largest-number-after-mutating-substring/)
- [3485. Longest Common Prefix of K Strings After Removal](../../3501-4000/3784-longest-common-prefix-of-k-strings-after-removal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/)
