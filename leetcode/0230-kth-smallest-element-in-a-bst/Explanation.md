# LeetCode 230: Kth Smallest Element in a BST

**LeetCode Problem #230 — Kth Smallest Element in a BST**
Solve LeetCode Kth Smallest Element in a BST using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Kth Smallest Element in a BST |
| LeetCode | #230 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given the  root  of a binary search tree, and an integer  k , return  the   k th    smallest value ( 1-indexed ) of all the values of the nodes in the tree .

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
We iterate through the input using **Modified Binary Search**. By maintaining state efficiently in a **Sorted Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Kth Smallest Element in a BST**. Applying **Modified Binary Search** yields the target result step by step.

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
- [215. Kth Largest Element in an Array](../0215-kth-largest-element-in-an-array/)
- [703. Kth Largest Element in a Stream](../0789-kth-largest-element-in-a-stream/)
- [3116. Kth Smallest Amount With Single Denomination Combination](../3375-kth-smallest-amount-with-single-denomination-combination/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
