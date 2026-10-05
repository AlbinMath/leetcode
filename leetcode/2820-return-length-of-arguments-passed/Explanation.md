# LeetCode 2820: Election Results

**LeetCode Problem #2820 — Election Results**
Solve LeetCode Election Results using TypeScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Election Results |
| LeetCode | #2820 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Write a function  argumentsLength  that returns the count of arguments passed to it.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
Uses rest parameters: `function(...args) { return args.length; }`. The spread operator collects all arguments into an array, and `.length` gives the count.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Election Results**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
TypeScript

## Source Code
- [solution.ts](./solution.ts)

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
- [3225. Maximum Score From Grid Operations](../3225-length-of-longest-subarray-with-at-most-k-frequency/)
- [3329. Count Substrings With K-Frequency Characters II](../3329-find-the-length-of-the-longest-common-prefix/)
- [3349. Adjacent Increasing Subarrays Detection I](../3349-maximum-length-substring-with-two-occurrences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/return-length-of-arguments-passed/)
