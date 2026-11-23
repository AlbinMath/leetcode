# LeetCode 1071: Greatest Common Divisor of Strings

**LeetCode Problem #1071 — Greatest Common Divisor of Strings**
Solve LeetCode Greatest Common Divisor of Strings using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Greatest Common Divisor of Strings |
| LeetCode | #1071 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
For two strings  s  and  t , we say " t  divides  s " if and only if  s = t + t + t + ... + t + t  (i.e.,  t  is concatenated with itself one or more times).

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Greatest Common Divisor of Strings**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
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
- [1979. Find Greatest Common Divisor of Array](../../2001-2500/2106-find-greatest-common-divisor-of-array/)
- [2709. Greatest Common Divisor Traversal](../../2501-3000/2827-greatest-common-divisor-traversal/)
- [2807. Insert Greatest Common Divisors in Linked List](../../2501-3000/2903-insert-greatest-common-divisors-in-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/greatest-common-divisor-of-strings/)
