# LeetCode 2653: Sliding Subarray Beauty

**LeetCode Problem #2653 — Sliding Subarray Beauty**
Solve LeetCode Sliding Subarray Beauty using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sliding Subarray Beauty |
| LeetCode | #2653 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer array  nums  containing  n  integers, find the  beauty  of each subarray of size  k .

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array / Hash Set**).
2. Process elements sequentially using **Dynamic Sliding Window Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Sliding Subarray Beauty**. Applying **Dynamic Sliding Window Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [239. Sliding Window Maximum](../../0001-0500/0239-sliding-window-maximum/)
- [480. Sliding Window Median](../../0001-0500/0480-sliding-window-median/)
- [773. Sliding Puzzle](../../0501-1000/0787-sliding-puzzle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sliding-subarray-beauty/)
