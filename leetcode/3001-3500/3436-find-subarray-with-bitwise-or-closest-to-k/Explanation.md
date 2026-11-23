# LeetCode 3171: Find Subarray With Bitwise OR Closest to K

**LeetCode Problem #3171 — Find Subarray With Bitwise OR Closest to K**
Solve LeetCode Find Subarray With Bitwise OR Closest to K using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Subarray With Bitwise OR Closest to K |
| LeetCode | #3171 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array  nums  and an integer  k . You need to find a  subarray  of  nums  such that the  absolute difference  between  k  and the bitwise  OR  of the subarray elements is as  small  as possible. In other words, select a subarray  nums[l..r]  such that  |k - (nums[l] OR nums[l + 1] ... OR nums[r])|  is minimum.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Subarray With Bitwise OR Closest to K**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [658. Find K Closest Elements](../../0501-1000/0658-find-k-closest-elements/)
- [560. Subarray Sum Equals K](../../0501-1000/0560-subarray-sum-equals-k/)
- [713. Subarray Product Less Than K](../../0501-1000/0713-subarray-product-less-than-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/)
