# LeetCode 2144: Minimum Cost of Buying Candies With Discount

**LeetCode Problem #2144 — Minimum Cost of Buying Candies With Discount**
Solve LeetCode Minimum Cost of Buying Candies With Discount using Kotlin and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost of Buying Candies With Discount |
| LeetCode | #2144 |
| Difficulty | Easy |
| Language | Kotlin |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
A shop is selling candies at a discount. For  every two  candies sold, the shop gives a  third  candy for  free .

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
Sort costs in descending order. Every third candy (index 2, 5, 8, ...) is free. Sum all costs except every third one.

## Algorithm
1. Initialize state variables / data structure (**Array / Hash Set**).
2. Process elements sequentially using **Dynamic Sliding Window Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Cost of Buying Candies With Discount**. Applying **Dynamic Sliding Window Traversal** yields the target result step by step.

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
Kotlin

## Source Code
- [solution.kt](./solution.kt)

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
- [64. Minimum Path Sum](../0064-minimum-path-sum/)
- [76. Minimum Window Substring](../0076-minimum-window-substring/)
- [111. Minimum Depth of Binary Tree](../0111-minimum-depth-of-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/)
