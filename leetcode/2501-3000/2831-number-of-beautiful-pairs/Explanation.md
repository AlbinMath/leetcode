# LeetCode 2748: Number of Beautiful Pairs

**LeetCode Problem #2748 — Number of Beautiful Pairs**
Solve LeetCode Number of Beautiful Pairs using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Beautiful Pairs |
| LeetCode | #2748 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  0-indexed  integer array  nums . A pair of indices  i ,  j  where  0 <= i < j < nums.length  is called beautiful if the  first digit  of  nums[i]  and the  last digit  of  nums[j]  are  coprime .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Beautiful Pairs**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [2588. Count the Number of Beautiful Subarrays](../../2501-3000/2656-count-the-number-of-beautiful-subarrays/)
- [2597. The Number of Beautiful Subsets](../../2501-3000/2696-the-number-of-beautiful-subsets/)
- [2914. Minimum Number of Changes to Make Binary String Beautiful](../../3001-3500/3174-minimum-number-of-changes-to-make-binary-string-beautiful/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-beautiful-pairs/)
