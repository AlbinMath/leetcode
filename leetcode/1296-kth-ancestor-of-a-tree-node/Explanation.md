# LeetCode 1483: Kth Ancestor of a Tree Node

**LeetCode Problem #1483 — Kth Ancestor of a Tree Node**
Solve LeetCode Kth Ancestor of a Tree Node using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Kth Ancestor of a Tree Node |
| LeetCode | #1483 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a tree with  n  nodes numbered from  0  to  n - 1  in the form of a parent array  parent  where  parent[i]  is the parent of  i th   node. The root of the tree is node  0 . Find the  k th   ancestor of a given node.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Kth Ancestor of a Tree Node**. Applying **Modified Binary Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [235. Lowest Common Ancestor of a Binary Search Tree](../0235-lowest-common-ancestor-of-a-binary-search-tree/)
- [236. Lowest Common Ancestor of a Binary Tree](../0236-lowest-common-ancestor-of-a-binary-tree/)
- [608. Tree Node](../0608-tree-node/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/)
