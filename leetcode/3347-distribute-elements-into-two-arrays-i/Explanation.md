# LeetCode 3069: Distribute Elements Into Two Arrays I

**LeetCode Problem #3069 — Distribute Elements Into Two Arrays I**
Solve LeetCode Distribute Elements Into Two Arrays I using Go and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distribute Elements Into Two Arrays I |
| LeetCode | #3069 |
| Difficulty | Easy |
| Language | Go |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  1-indexed  array of  distinct  integers  nums  of length  n .

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Complement Lookup / Hash Table Frequency**. By maintaining state efficiently in a **Dictionary / Hash Map**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Distribute Elements Into Two Arrays I**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
Go

## Source Code
- [solution.go](./solution.go)

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
- [4. Median of Two Sorted Arrays](../0004-median-of-two-sorted-arrays/)
- [349. Intersection of Two Arrays](../0349-intersection-of-two-arrays/)
- [350. Intersection of Two Arrays II](../0350-intersection-of-two-arrays-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distribute-elements-into-two-arrays-i/)
