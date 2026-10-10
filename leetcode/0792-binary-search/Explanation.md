# LeetCode 704: Binary Search

**LeetCode Problem #704 — Binary Search**
Solve LeetCode Binary Search using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary Search |
| LeetCode | #704 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem
Given an array of integers  nums  which is sorted in ascending order, and an integer  target , write a function to search  target  in  nums . If  target  exists, then return its index. Otherwise, return  -1 .

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
We iterate through the input using **Modified Binary Search**. By maintaining state efficiently in a **Sorted Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Binary Search**. Applying **Modified Binary Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(log n)
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
- [108. Convert Sorted Array to Binary Search Tree](../0108-convert-sorted-array-to-binary-search-tree/)
- [501. Find Mode in Binary Search Tree](../0501-find-mode-in-binary-search-tree/)
- [700. Search in a Binary Search Tree](../0783-search-in-a-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-search/)
