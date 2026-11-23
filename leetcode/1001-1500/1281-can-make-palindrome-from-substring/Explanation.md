# LeetCode 1177: Can Make Palindrome from Substring

**LeetCode Problem #1177 — Can Make Palindrome from Substring**
Solve LeetCode Can Make Palindrome from Substring using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Can Make Palindrome from Substring |
| LeetCode | #1177 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a string  s  and array  queries  where  queries[i] = [left i , right i , k i ] . We may rearrange the substring  s[left i ...right i ]  for each query and then choose up to  k i   of them to replace with any lowercase English letter.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Two Pointer Convergence & Scanning**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Can Make Palindrome from Substring**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [1502. Can Make Arithmetic Progression From Sequence](../../1501-2000/1626-can-make-arithmetic-progression-from-sequence/)
- [2930. Number of Strings Which Can Be Rearranged to Contain Substring](../../3001-3500/3200-number-of-strings-which-can-be-rearranged-to-contain-substring/)
- [3503. Longest Palindrome After Substring Concatenation I](../../3501-4000/3793-longest-palindrome-after-substring-concatenation-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/can-make-palindrome-from-substring/)
