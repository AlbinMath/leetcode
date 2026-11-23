# LeetCode 1305: All Elements in Two Binary Search Trees

**LeetCode Problem #1305 — All Elements in Two Binary Search Trees**
Solve LeetCode All Elements in Two Binary Search Trees using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | All Elements in Two Binary Search Trees |
| LeetCode | #1305 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given two binary search trees  root1  and  root2 , return  a list containing all the integers from both trees sorted in  ascending  order .

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
We iterate through the input using **Modified Binary Search**. By maintaining state efficiently in a **Sorted Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **All Elements in Two Binary Search Trees**. Applying **Modified Binary Search** yields the target result step by step.

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
- [95. Unique Binary Search Trees II](../0095-unique-binary-search-trees-ii/)
- [96. Unique Binary Search Trees](../0096-unique-binary-search-trees/)
- [558. Logical OR of Two Binary Grids Represented as Quad-Trees](../0773-logical-or-of-two-binary-grids-represented-as-quad-trees/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/)
