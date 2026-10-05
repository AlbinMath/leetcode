# LeetCode 2182: Construct String With Repeat Limit

**LeetCode Problem #2182 — Construct String With Repeat Limit**
Solve LeetCode Construct String With Repeat Limit using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence / Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Construct String With Repeat Limit |
| LeetCode | #2182 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Two Pointer Convergence / Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
A  critical point  in a linked list is defined as  either  a  local maxima  or a  local minima .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
Traverse the linked list, tracking the position of each critical point (where `prev.val`, `curr.val`, `curr.next.val` form a local min or max). The minimum distance is between consecutive critical points; the maximum is between the first and last.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence / Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Construct String With Repeat Limit**. Applying **Two Pointer Convergence / Scanning** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [3299. Sum of Consecutive Subsequences](../3299-find-the-maximum-number-of-elements-in-subset/)
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
