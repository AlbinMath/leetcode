# LeetCode 239: Sliding Window Maximum

**LeetCode Problem #239 — Sliding Window Maximum**
Solve LeetCode Sliding Window Maximum using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sliding Window Maximum |
| LeetCode | #239 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array of integers  nums , there is a sliding window of size  k  which is moving from the very left of the array to the very right. You can only see the  k  numbers in the window. Each time the sliding window moves right by one position.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
We iterate through the input using **Dynamic Sliding Window Traversal**. By maintaining state efficiently in a **Array / Hash Set**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array / Hash Set**).
2. Process elements sequentially using **Dynamic Sliding Window Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Sliding Window Maximum**. Applying **Dynamic Sliding Window Traversal** yields the target result step by step.

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
- [53. Maximum Subarray](../0053-maximum-subarray/)
- [76. Minimum Window Substring](../0076-minimum-window-substring/)
- [104. Maximum Depth of Binary Tree](../0104-maximum-depth-of-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sliding-window-maximum/)
