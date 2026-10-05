# LeetCode 2236: Root Equals Sum of Children

**LeetCode Problem #2236 — Root Equals Sum of Children**
Solve LeetCode Root Equals Sum of Children using Java and Two Pointers. This solution finds the optimal result using Two Pointer Convergence / Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Root Equals Sum of Children |
| LeetCode | #2236 |
| Difficulty | Easy |
| Language | Java |
| Algorithm | Two Pointer Convergence / Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
In a linked list of size  n , where  n  is  even , the  i th   node ( 0-indexed ) of the linked list is known as the  twin  of the  (n-1-i) th   node, if  0 <= i <= (n / 2) - 1 .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
Find the middle using fast/slow pointers, reverse the second half, then iterate both halves simultaneously to compute twin sums and track the maximum.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence / Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Root Equals Sum of Children**. Applying **Two Pointer Convergence / Scanning** yields the target result step by step.

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
Java

## Source Code
- [solution.java](./solution.java)

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
- [2216. Minimum Deletions to Make Array Beautiful](../2216-delete-the-middle-node-of-a-linked-list/)
- [1. Two Sum](../0001-two-sum/)
- [19. Remove Nth Node From End of List](../0019-remove-nth-node-from-end-of-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/)
