# LeetCode 3658: GCD of Odd and Even Sums

**LeetCode Problem #3658 — GCD of Odd and Even Sums**
Solve LeetCode GCD of Odd and Even Sums using Kotlin and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | GCD of Odd and Even Sums |
| LeetCode | #3658 |
| Difficulty | Easy |
| Language | Kotlin |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  n . Your task is to compute the  GCD  (greatest common divisor) of two values:

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **GCD of Odd and Even Sums**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
Kotlin

## Source Code
- [solution.kt](./solution.kt)

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
- [328. Odd Even Linked List](../0328-odd-even-linked-list/)
- [1116. Print Zero Even Odd](../1216-print-zero-even-odd/)
- [3220. Odd and Even Transactions](../3530-odd-and-even-transactions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/gcd-of-odd-and-even-sums/)
