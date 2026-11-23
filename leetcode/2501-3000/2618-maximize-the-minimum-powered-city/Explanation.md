# LeetCode 2528: Maximize the Minimum Powered City

**LeetCode Problem #2528 — Maximize the Minimum Powered City**
Solve LeetCode Maximize the Minimum Powered City using JavaScript and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize the Minimum Powered City |
| LeetCode | #2528 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  0-indexed  integer array  stations  of length  n , where  stations[i]  represents the number of power stations in the  i th   city.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array / Hash Set**).
2. Process elements sequentially using **Dynamic Sliding Window Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximize the Minimum Powered City**. Applying **Dynamic Sliding Window Traversal** yields the target result step by step.

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
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [2934. Minimum Operations to Maximize Last Elements in Arrays](../../3001-3500/3190-minimum-operations-to-maximize-last-elements-in-arrays/)
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1047-maximize-sum-of-array-after-k-negations/)
- [1659. Maximize Grid Happiness](../../1501-2000/1778-maximize-grid-happiness/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-the-minimum-powered-city/)
