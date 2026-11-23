# LeetCode 257: Binary Tree Paths

**LeetCode Problem #257 — Binary Tree Paths**
Solve LeetCode Binary Tree Paths using PHP and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary Tree Paths |
| LeetCode | #257 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given the  root  of a binary tree.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Binary Tree Paths**. Applying **Modified Binary Search** yields the target result step by step.

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
PHP

## Source Code
- [solution.php](./solution.php)

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
- [1457. Pseudo-Palindromic Paths in a Binary Tree](../../1501-2000/1568-pseudo-palindromic-paths-in-a-binary-tree/)
- [2673. Make Costs of Paths Equal in a Binary Tree](../../2501-3000/2780-make-costs-of-paths-equal-in-a-binary-tree/)
- [2791. Count Paths That Can Form a Palindrome in a Tree](../../2501-3000/2905-count-paths-that-can-form-a-palindrome-in-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-tree-paths/)
