# LeetCode 693: Binary Number with Alternating Bits

**LeetCode Problem #693 — Binary Number with Alternating Bits**
Solve LeetCode Binary Number with Alternating Bits using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary Number with Alternating Bits |
| LeetCode | #693 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Binary Number with Alternating Bits**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [762. Prime Number of Set Bits in Binary Representation](../0767-prime-number-of-set-bits-in-binary-representation/)
- [1290. Convert Binary Number in a Linked List to Integer](../1411-convert-binary-number-in-a-linked-list-to-integer/)
- [1356. Sort Integers by The Number of 1 Bits](../1458-sort-integers-by-the-number-of-1-bits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-number-with-alternating-bits/)
