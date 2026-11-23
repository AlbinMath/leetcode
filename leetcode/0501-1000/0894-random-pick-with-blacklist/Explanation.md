# LeetCode 710: Random Pick with Blacklist

**LeetCode Problem #710 — Random Pick with Blacklist**
Solve LeetCode Random Pick with Blacklist using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Random Pick with Blacklist |
| LeetCode | #710 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  n  and an array of  unique  integers  blacklist . Design an algorithm to pick a random integer in the range  [0, n - 1]  that is  not  in  blacklist . Any integer that is in the mentioned range and not in  blacklist  should be  equally likely  to be returned.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Random Pick with Blacklist**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [398. Random Pick Index](../../0001-0500/0398-random-pick-index/)
- [528. Random Pick with Weight](../../0501-1000/0912-random-pick-with-weight/)
- [2260. Minimum Consecutive Cards to Pick Up](../../2001-2500/2338-minimum-consecutive-cards-to-pick-up/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/random-pick-with-blacklist/)
