# LeetCode 2318: Number of Distinct Roll Sequences

**LeetCode Problem #2318 — Number of Distinct Roll Sequences**
Solve LeetCode Number of Distinct Roll Sequences using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Distinct Roll Sequences |
| LeetCode | #2318 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  n . You roll a fair 6-sided dice  n  times. Determine the total number of  distinct  sequences of rolls possible such that the following conditions are satisfied:

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Distinct Roll Sequences**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1467. Probability of a Two Boxes Having The Same Number of Distinct Balls](../../1501-2000/1577-probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)
- [2954. Count the Number of Infection Sequences](../../3001-3500/3224-count-the-number-of-infection-sequences/)
- [3160. Find the Number of Distinct Colors Among the Balls](../../3001-3500/3434-find-the-number-of-distinct-colors-among-the-balls/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-distinct-roll-sequences/)
