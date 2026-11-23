# LeetCode 863: All Nodes Distance K in Binary Tree

**LeetCode Problem #863 — All Nodes Distance K in Binary Tree**
Solve LeetCode All Nodes Distance K in Binary Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | All Nodes Distance K in Binary Tree |
| LeetCode | #863 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given the  root  of a binary tree, the value of a target node  target , and an integer  k , return  an array of the values of all nodes that have a distance   k   from the target node.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **All Nodes Distance K in Binary Tree**. Applying **Modified Binary Search** yields the target result step by step.

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
- [1461. Check If a String Contains All Binary Codes of Size K](../../1501-2000/1557-check-if-a-string-contains-all-binary-codes-of-size-k/)
- [1361. Validate Binary Tree Nodes](../../1001-1500/1275-validate-binary-tree-nodes/)
- [1448. Count Good Nodes in Binary Tree](../../1501-2000/1544-count-good-nodes-in-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)
