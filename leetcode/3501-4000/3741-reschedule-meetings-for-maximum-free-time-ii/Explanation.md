# LeetCode 3440: Reschedule Meetings for Maximum Free Time II

**LeetCode Problem #3440 — Reschedule Meetings for Maximum Free Time II**
Solve LeetCode Reschedule Meetings for Maximum Free Time II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reschedule Meetings for Maximum Free Time II |
| LeetCode | #3440 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  eventTime  denoting the duration of an event. You are also given two integer arrays  startTime  and  endTime , each of length  n .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Reschedule Meetings for Maximum Free Time II**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [3439. Reschedule Meetings for Maximum Free Time I](../../3501-4000/3743-reschedule-meetings-for-maximum-free-time-i/)
- [4009. Minimum Possible Maximum Waiting Time](../../4001-4500/4244-minimum-possible-maximum-waiting-time/)
- [53. Maximum Subarray](../../0001-0500/0053-maximum-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/)
