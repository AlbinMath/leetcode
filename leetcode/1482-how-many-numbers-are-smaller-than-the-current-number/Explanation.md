# LeetCode 1365: How Many Numbers Are Smaller Than the Current Number

**LeetCode Problem #1365 — How Many Numbers Are Smaller Than the Current Number**
Solve LeetCode How Many Numbers Are Smaller Than the Current Number using TypeScript and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | How Many Numbers Are Smaller Than the Current Number |
| LeetCode | #1365 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given the array  nums , for each  nums[i]  find out how many numbers in the array are smaller than it. That is, for each  nums[i]  you have to count the number of valid  j&#39;s  such that  j != i   and   nums[j] < nums[i] .

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **Counting Sort + Prefix Sum** for an efficient $O(N)$ solution.

1. **Count Frequencies:** Count how many times each value `0–100` appears.
2. **Prefix Sum:** Transform the count array so `count[i]` = total numbers ≤ `i`.
3. **Build Result:** For each `num` in the original array, the count of numbers strictly smaller is `count[num - 1]` (or `0` if `num == 0`).

Time complexity is $O(N + K)$ where $K = 100$, and space complexity is $O(K)$.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **How Many Numbers Are Smaller Than the Current Number**. Applying **Prefix Sum Precomputation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2. Add Two Numbers](../0002-add-two-numbers/)
- [9. Palindrome Number](../0009-palindrome-number/)
- [17. Letter Combinations of a Phone Number](../0017-letter-combinations-of-a-phone-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)
