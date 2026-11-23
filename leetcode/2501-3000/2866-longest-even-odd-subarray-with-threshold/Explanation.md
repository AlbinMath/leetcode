# LeetCode 2760: Longest Even Odd Subarray With Threshold

**LeetCode Problem #2760 — Longest Even Odd Subarray With Threshold**
Solve LeetCode Longest Even Odd Subarray With Threshold using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Even Odd Subarray With Threshold |
| LeetCode | #2760 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  0-indexed  integer array  nums  and an integer  threshold .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Even Odd Subarray With Threshold**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
Python

## Source Code
- [solution.py](./solution.py)

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
- [978. Longest Turbulent Subarray](../../1001-1500/1020-longest-turbulent-subarray/)
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](../../1501-2000/1549-longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)
- [1493. Longest Subarray of 1's After Deleting One Element](../../1501-2000/1586-longest-subarray-of-1s-after-deleting-one-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/)
