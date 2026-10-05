# LeetCode 2472: Maximum Number of Non-overlapping Palindrome Substrings

**LeetCode Problem #2472 — Maximum Number of Non-overlapping Palindrome Substrings**
Solve LeetCode Maximum Number of Non-overlapping Palindrome Substrings using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Non-overlapping Palindrome Substrings |
| LeetCode | #2472 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a string  s  and a  positive  integer  k .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
Uses **DP** combined with palindrome detection (expand-around-center or Manacher's). For each position, compute `dp[i]` = max non-overlapping palindromes in `s[0..i-1]`. When a palindrome of length ≥ k ending at position i is found, update dp accordingly.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Number of Non-overlapping Palindrome Substrings**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [1520. Maximum Number of Non-Overlapping Substrings](../1644-maximum-number-of-non-overlapping-substrings/)
- [1621. Number of Sets of K Non-Overlapping Line Segments](../1725-number-of-sets-of-k-non-overlapping-line-segments/)
- [3414. Maximum Score of Non-overlapping Intervals](../3562-maximum-score-of-non-overlapping-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/)
