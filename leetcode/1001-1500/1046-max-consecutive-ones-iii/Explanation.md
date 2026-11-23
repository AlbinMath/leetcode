# LeetCode 1004: Max Consecutive Ones III

**LeetCode Problem #1004 — Max Consecutive Ones III**
Solve LeetCode Max Consecutive Ones III using JavaScript, Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Max Consecutive Ones III |
| LeetCode | #1004 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a binary array  nums  and an integer  k , return  the maximum number of consecutive   1  &#39;s in the array if you can flip at most   k   0 &#39;s.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Max Consecutive Ones III**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)

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
- [485. Max Consecutive Ones](../../0001-0500/0485-max-consecutive-ones/)
- [600. Non-negative Integers without Consecutive Ones](../../0501-1000/0600-non-negative-integers-without-consecutive-ones/)
- [1703. Minimum Adjacent Swaps for K Consecutive Ones](../../1501-2000/1805-minimum-adjacent-swaps-for-k-consecutive-ones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/)
