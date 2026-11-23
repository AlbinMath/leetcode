# LeetCode 906: Super Palindromes

**LeetCode Problem #906 — Super Palindromes**
Solve LeetCode Super Palindromes using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Super Palindromes |
| LeetCode | #906 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Let&#39;s say a positive integer is a  super-palindrome  if it is a palindrome, and it is also the square of a palindrome.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Two Pointer Convergence & Scanning**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Super Palindromes**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [372. Super Pow](../0372-super-pow/)
- [517. Super Washing Machines](../0517-super-washing-machines/)
- [2911. Minimum Changes to Make K Semi-palindromes](../2879-minimum-changes-to-make-k-semi-palindromes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/super-palindromes/)
