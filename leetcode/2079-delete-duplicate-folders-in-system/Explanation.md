# LeetCode 1948: Delete Duplicate Folders in System

**LeetCode Problem #1948 — Delete Duplicate Folders in System**
Solve LeetCode Delete Duplicate Folders in System using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Delete Duplicate Folders in System |
| LeetCode | #1948 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Due to a bug, there are many duplicate folders in a file system. You are given a 2D array  paths , where  paths[i]  is an array representing an absolute path to the  i th   folder in the file system.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Delete Duplicate Folders in System**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [196. Delete Duplicate Emails](../0196-delete-duplicate-emails/)
- [182. Duplicate Emails](../0182-duplicate-emails/)
- [217. Contains Duplicate](../0217-contains-duplicate/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delete-duplicate-folders-in-system/)
