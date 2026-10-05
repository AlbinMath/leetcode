# LeetCode 448: Find All Numbers Disappeared in an Array

**LeetCode Problem #448 — Find All Numbers Disappeared in an Array**
Solve LeetCode Find All Numbers Disappeared in an Array using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find All Numbers Disappeared in an Array |
| LeetCode | #448 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an array  nums  of  n  integers where  nums[i]  is in the range  [1, n] , return  an array of all the integers in the range   [1, n]   that do not appear in   nums .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses the **array itself as a hash set** by negating values at corresponding indices.

1. **Mark Presence:** For each number `num` in the array, compute `index = |num| - 1` (using absolute value since values may already be negated). If `nums[index]` is positive, negate it to mark that the number `index + 1` exists in the array.
2. **Find Missing:** After marking, iterate through the array. If `nums[i]` is still positive, it means no number `i + 1` was encountered in the array, so `i + 1` is missing and gets pushed to the result.

Time complexity is $O(N)$ and space complexity is $O(1)$ (excluding the output array).

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find All Numbers Disappeared in an Array**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)
- [1979. Find Greatest Common Divisor of Array](../2106-find-greatest-common-divisor-of-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)
