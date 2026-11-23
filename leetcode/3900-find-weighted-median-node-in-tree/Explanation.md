# LeetCode 3585: Find Weighted Median Node in Tree

**LeetCode Problem #3585 — Find Weighted Median Node in Tree**
Solve LeetCode Find Weighted Median Node in Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Weighted Median Node in Tree |
| LeetCode | #3585 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  n  and an  undirected, weighted  tree rooted at node 0 with  n  nodes numbered from 0 to  n - 1 . This is represented by a 2D array  edges  of length  n - 1 , where  edges[i] = [u i , v i , w i ]  indicates an edge from node  u i   to  v i   with weight  w i  .

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Weighted Median Node in Tree**. Applying **Modified Binary Search** yields the target result step by step.

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
Python

## Source Code
- [solution.py](./solution.py)

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
- [1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree](../1498-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)
- [608. Tree Node](../0608-tree-node/)
- [671. Second Minimum Node In a Binary Tree](../0671-second-minimum-node-in-a-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-weighted-median-node-in-tree/)
