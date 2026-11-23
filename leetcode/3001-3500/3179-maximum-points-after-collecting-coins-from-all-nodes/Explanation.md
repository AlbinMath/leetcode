# LeetCode 2920: Maximum Points After Collecting Coins From All Nodes

**LeetCode Problem #2920 — Maximum Points After Collecting Coins From All Nodes**
Solve LeetCode Maximum Points After Collecting Coins From All Nodes using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Points After Collecting Coins From All Nodes |
| LeetCode | #2920 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There exists an undirected tree rooted at node  0  with  n  nodes labeled from  0  to  n - 1 . You are given a 2D  integer  array  edges  of length  n - 1 , where  edges[i] = [a i , b i ]  indicates that there is an edge between nodes  a i   and  b i   in the tree. You are also given a  0-indexed  array  coins  of size  n  where  coins[i]  indicates the number of coins in the vertex  i , and an integer  k .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Points After Collecting Coins From All Nodes**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [3413. Maximum Coins From K Consecutive Bags](../../3501-4000/3715-maximum-coins-from-k-consecutive-bags/)
- [1423. Maximum Points You Can Obtain from Cards](../../1501-2000/1538-maximum-points-you-can-obtain-from-cards/)
- [2503. Maximum Number of Points From Grid Queries](../../2501-3000/2588-maximum-number-of-points-from-grid-queries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/)
