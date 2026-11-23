# LeetCode 1576: Replace All ?'s to Avoid Consecutive Repeating Characters

**LeetCode Problem #1576 — Replace All ?'s to Avoid Consecutive Repeating Characters**
Solve LeetCode Replace All ?'s to Avoid Consecutive Repeating Characters using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Replace All ?'s to Avoid Consecutive Repeating Characters |
| LeetCode | #1576 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a string  s  containing only lowercase English letters and the  &#39;?&#39;  character, convert  all  the  &#39;?&#39;  characters into lowercase letters such that the final string does not contain any  consecutive repeating  characters. You  cannot  modify the non  &#39;?&#39;  characters.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Replace All ?'s to Avoid Consecutive Repeating Characters**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1844. Replace All Digits with Characters](../../1501-2000/1954-replace-all-digits-with-characters/)
- [1446. Consecutive Characters](../../1501-2000/1542-consecutive-characters/)
- [3970. Shortest Path With At Most K Consecutive Identical Characters](../../4001-4500/4104-shortest-path-with-at-most-k-consecutive-identical-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/)
