# LeetCode 1846: Maximum Element After Decreasing and Rearranging

**LeetCode Problem #1846 — Maximum Element After Decreasing and Rearranging**
Solve LeetCode Maximum Element After Decreasing and Rearranging using Java and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Element After Decreasing and Rearranging |
| LeetCode | #1846 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem
You are given an array of positive integers  arr . Perform some operations (possibly none) on  arr  so that it satisfies these conditions:

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
1. **Sort** the array in ascending order.
2. Initialize `max = 0`. For each element, set `max = min(num, max + 1)`. This greedily builds the longest possible increasing sequence where each step increases by at most 1.
3. Return `max`.

Time complexity is $O(N \log N)$ and space complexity is $O(\log N)$ for sorting.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Element After Decreasing and Rearranging**. Applying **Modified Binary Search** yields the target result step by step.

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
Java

## Source Code
- [solution.java](./solution.java)

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
- [3300. Minimum Element After Replacement With Digit Sum](../3606-minimum-element-after-replacement-with-digit-sum/)
- [27. Remove Element](../0027-remove-element/)
- [34. Find First and Last Position of Element in Sorted Array](../0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/)
