# LeetCode 3859: Count Subarrays With K Distinct Integers

**LeetCode Problem #3859 — Count Subarrays With K Distinct Integers**
Solve LeetCode Count Subarrays With K Distinct Integers using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Subarrays With K Distinct Integers |
| LeetCode | #3859 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer array  nums  and two integers  k  and  m .

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Complement Lookup / Hash Table Frequency**. By maintaining state efficiently in a **Dictionary / Hash Map**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Subarrays With K Distinct Integers**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [2302. Count Subarrays With Score Less Than K](../../2001-2500/2394-count-subarrays-with-score-less-than-k/)
- [2962. Count Subarrays Where Max Element Appears at Least K Times](../../3001-3500/3213-count-subarrays-where-max-element-appears-at-least-k-times/)
- [3420. Count Non-Decreasing Subarrays After K Operations](../../3501-4000/3674-count-non-decreasing-subarrays-after-k-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/)
