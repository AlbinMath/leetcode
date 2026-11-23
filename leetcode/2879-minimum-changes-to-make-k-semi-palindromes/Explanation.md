# LeetCode 2911: Minimum Changes to Make K Semi-palindromes

**LeetCode Problem #2911 — Minimum Changes to Make K Semi-palindromes**
Solve LeetCode Minimum Changes to Make K Semi-palindromes using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Changes to Make K Semi-palindromes |
| LeetCode | #2911 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a string  s  and an integer  k , partition  s  into  k    substrings   such that the letter changes needed to make each substring a  semi-palindrome  are minimized.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Two Pointer Convergence & Scanning**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Changes to Make K Semi-palindromes**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [1758. Minimum Changes To Make Alternating Binary String](../1884-minimum-changes-to-make-alternating-binary-string/)
- [2914. Minimum Number of Changes to Make Binary String Beautiful](../3174-minimum-number-of-changes-to-make-binary-string-beautiful/)
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../3249-minimum-number-of-operations-to-make-array-xor-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/)
