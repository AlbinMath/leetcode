# LeetCode 2540: Minimum Common Value

**LeetCode Problem #2540 — Minimum Common Value**
Solve LeetCode Minimum Common Value using C++ and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Common Value |
| LeetCode | #2540 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given two integer arrays  nums1  and  nums2 , sorted in non-decreasing order, return  the  minimum integer common  to both arrays . If there is no common integer amongst  nums1  and  nums2 , return  -1 .

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
Use **two pointers**, one for each array. If values match, return it. Otherwise advance the pointer with the smaller value. If either pointer reaches the end, return -1. Time: $O(N + M)$, Space: $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Array / Hash Set**).
2. Process elements sequentially using **Dynamic Sliding Window Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Common Value**. Applying **Dynamic Sliding Window Traversal** yields the target result step by step.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [14. Longest Common Prefix](../0014-longest-common-prefix/)
- [64. Minimum Path Sum](../0064-minimum-path-sum/)
- [76. Minimum Window Substring](../0076-minimum-window-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-common-value/)
