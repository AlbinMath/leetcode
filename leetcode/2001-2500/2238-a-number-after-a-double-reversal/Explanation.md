# LeetCode 2119: A Number After a Double Reversal

**LeetCode Problem #2119 — A Number After a Double Reversal**
Solve LeetCode A Number After a Double Reversal using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | A Number After a Double Reversal |
| LeetCode | #2119 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Reversing  an integer means to reverse all its digits.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **A Number After a Double Reversal**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [1946. Largest Number After Mutating Substring](../../2001-2500/2077-largest-number-after-mutating-substring/)
- [2400. Number of Ways to Reach a Position After Exactly k Steps](../../2001-2500/2477-number-of-ways-to-reach-a-position-after-exactly-k-steps/)
- [3003. Maximize the Number of Partitions After Operations](../../3001-3500/3233-maximize-the-number-of-partitions-after-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/a-number-after-a-double-reversal/)
