# LeetCode 1944: Number of Visible People in a Queue

**LeetCode Problem #1944 — Number of Visible People in a Queue**
Solve LeetCode Number of Visible People in a Queue using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Visible People in a Queue |
| LeetCode | #1944 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There are  n  people standing in a queue, and they numbered from  0  to  n - 1  in  left to right  order. You are given an array  heights  of  distinct  integers where  heights[i]  represents the height of the  i th   person.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Visible People in a Queue**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1610. Maximum Number of Visible Points](../1733-maximum-number-of-visible-points/)
- [1866. Number of Ways to Rearrange Sticks With K Sticks Visible](../1996-number-of-ways-to-rearrange-sticks-with-k-sticks-visible/)
- [3881. Direction Assignments with Exactly K Visible People](../4251-direction-assignments-with-exactly-k-visible-people/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-visible-people-in-a-queue/)
