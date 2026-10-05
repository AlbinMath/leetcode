# LeetCode 1776: Car Fleet II

**LeetCode Problem #1776 — Car Fleet II**
Solve LeetCode Car Fleet II using JavaScript and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Car Fleet II |
| LeetCode | #1776 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  nums  and an integer  x . In one operation, you can either remove the leftmost or the rightmost element from the array  nums  and subtract its value from  x . Note that this  modifies  the array for future operations.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
Instead of simulating removing elements from the edges, the problem can be reframed into an inverse problem: 
If we remove a prefix and a suffix that sum to `x`, then the remaining elements in the middle form a contiguous subarray whose sum is `total_sum - x`. To minimize the number of operations (number of elements removed), we need to **maximize the length of this middle subarray**.

1. The code calculates the `total` sum of the array. The `target` sum for the middle subarray is then `total - x`.
2. Edge Cases: 
   - If `target < 0`, it's impossible to reach `x` since all numbers are positive, so it returns `-1`.
   - If `target === 0`, it means the entire array sums to `x`, so all elements must be removed. It returns `nums.length`.
3. It uses a **Sliding Window** technique with two pointers (`left` and `right`) to find the longest contiguous subarray that sums exactly to `target`.
4. It iterates the `right` pointer across the array, adding `nums[right]` to a running `sum`.
5. If the `sum` exceeds the `target`, it shrinks the window from the left by subtracting `nums[left]` and incrementing `left` until the `sum` is less than or equal to `target`.
6. Whenever the `sum` exactly equals the `target`, it updates `maxLength` with the size of the current window (`right - left + 1`).
7. Finally, if a valid subarray was found (`maxLength !== -1`), the minimum operations will be the total number of elements minus the longest subarray length (`nums.length - maxLength`). Otherwise, it returns `-1`.

## Algorithm
1. Initialize state variables / data structure (**Array / Hash Set**).
2. Process elements sequentially using **Dynamic Sliding Window Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Car Fleet II**. Applying **Dynamic Sliding Window Traversal** yields the target result step by step.

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
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)
- [1216. Valid Palindrome III](../1216-print-zero-even-odd/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)
