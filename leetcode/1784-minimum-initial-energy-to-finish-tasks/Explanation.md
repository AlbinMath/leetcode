# LeetCode 1665: Minimum Initial Energy to Finish Tasks

**LeetCode Problem #1665 — Minimum Initial Energy to Finish Tasks**
Solve LeetCode Minimum Initial Energy to Finish Tasks using C++ and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Initial Energy to Finish Tasks |
| LeetCode | #1665 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem
You are given an array  tasks  where  tasks[i] = [actual i , minimum i ] :

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
1. **Sort:** Tasks are sorted by `(minimum - actual)` in descending order. This prioritizes tasks with the largest gap between their minimum requirement and actual cost.
2. **Greedy:** Iterate through tasks, tracking the cumulative `actual` energy spent (`current`). For each task, update `energy = max(energy, current + minimum)`.
3. Return `energy`.

Time complexity is $O(N \log N)$ and space complexity is $O(\log N)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Initial Energy to Finish Tasks**. Applying **Modified Binary Search** yields the target result step by step.

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
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)
- [1658. Minimum Operations to Reduce X to Zero](../1776-minimum-operations-to-reduce-x-to-zero/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/)
