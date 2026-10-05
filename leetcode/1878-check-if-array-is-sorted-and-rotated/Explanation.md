# LeetCode 1878: Get Biggest Three Rhombus Sums in a Grid

**LeetCode Problem #1878 — Get Biggest Three Rhombus Sums in a Grid**
Solve LeetCode Get Biggest Three Rhombus Sums in a Grid using C++ and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Get Biggest Three Rhombus Sums in a Grid |
| LeetCode | #1878 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an array  nums , return  true   if the array was originally sorted in non-decreasing order, then rotated  some  number of positions (including zero) . Otherwise, return  false .

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code counts the number of "breaks" where `nums[i] > nums[(i+1) % n]`. A sorted-and-rotated array can have **at most one** such break (at the rotation point). If there are 0 or 1 breaks, return `true`; otherwise, `false`.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Get Biggest Three Rhombus Sums in a Grid**. Applying **Modified Binary Search** yields the target result step by step.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [33. Search in Rotated Sorted Array](../0033-search-in-rotated-sorted-array/)
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)
