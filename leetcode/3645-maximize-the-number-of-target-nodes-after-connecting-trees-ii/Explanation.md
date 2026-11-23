# LeetCode 3373: Maximize the Number of Target Nodes After Connecting Trees II

**LeetCode Problem #3373 — Maximize the Number of Target Nodes After Connecting Trees II**
Solve LeetCode Maximize the Number of Target Nodes After Connecting Trees II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize the Number of Target Nodes After Connecting Trees II |
| LeetCode | #3373 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There exist two  undirected  trees with  n  and  m  nodes, labeled from  [0, n - 1]  and  [0, m - 1] , respectively.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximize the Number of Target Nodes After Connecting Trees II**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [3372. Maximize the Number of Target Nodes After Connecting Trees I](../3633-maximize-the-number-of-target-nodes-after-connecting-trees-i/)
- [3003. Maximize the Number of Partitions After Operations](../3233-maximize-the-number-of-partitions-after-operations/)
- [1005. Maximize Sum Of Array After K Negations](../1047-maximize-sum-of-array-after-k-negations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/)
