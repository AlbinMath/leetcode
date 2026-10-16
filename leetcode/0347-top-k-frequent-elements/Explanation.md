# LeetCode 347: Top K Frequent Elements

**LeetCode Problem #347 — Top K Frequent Elements**
Solve LeetCode Top K Frequent Elements using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Top K Frequent Elements |
| LeetCode | #347 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n log n) |
| Space Complexity | O(1) |

## Problem
Given an integer array  nums  and an integer  k , return  the   k   most frequent elements . You may return the answer in  any order .

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
We iterate through the input using **Modified Binary Search**. By maintaining state efficiently in a **Sorted Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Top K Frequent Elements**. Applying **Modified Binary Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n log n)
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
- [658. Find K Closest Elements](../0658-find-k-closest-elements/)
- [3759. Count Elements With at Least K Greater Values](../4141-count-elements-with-at-least-k-greater-values/)
- [23. Merge k Sorted Lists](../0023-merge-k-sorted-lists/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)
