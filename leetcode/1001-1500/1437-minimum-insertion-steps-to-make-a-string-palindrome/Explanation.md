# LeetCode 1312: Minimum Insertion Steps to Make a String Palindrome

**LeetCode Problem #1312 — Minimum Insertion Steps to Make a String Palindrome**
Solve LeetCode Minimum Insertion Steps to Make a String Palindrome using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Insertion Steps to Make a String Palindrome |
| LeetCode | #1312 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a string  s . In one step you can insert any character at any index of the string.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Two Pointer Convergence & Scanning**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Insertion Steps to Make a String Palindrome**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [1347. Minimum Number of Steps to Make Two Strings Anagram](../../1001-1500/1469-minimum-number-of-steps-to-make-two-strings-anagram/)
- [1653. Minimum Deletions to Make String Balanced](../../1501-2000/1756-minimum-deletions-to-make-string-balanced/)
- [1758. Minimum Changes To Make Alternating Binary String](../../1501-2000/1884-minimum-changes-to-make-alternating-binary-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/)
