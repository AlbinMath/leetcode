# LeetCode 2305: Fair Distribution of Cookies

**LeetCode Problem #2305 — Fair Distribution of Cookies**
Solve LeetCode Fair Distribution of Cookies using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Fair Distribution of Cookies |
| LeetCode | #2305 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  cookies , where  cookies[i]  denotes the number of cookies in the  i th   bag. You are also given an integer  k  that denotes the number of children to distribute  all  the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Fair Distribution of Cookies**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
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
- [888. Fair Candy Swap](../../0501-1000/0924-fair-candy-swap/)
- [1664. Ways to Make a Fair Array](../../1501-2000/1783-ways-to-make-a-fair-array/)
- [455. Assign Cookies](../../0001-0500/0455-assign-cookies/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/fair-distribution-of-cookies/)
