# LeetCode 2958: Length of Longest Subarray With at Most K Frequency

**LeetCode Problem #2958 — Length of Longest Subarray With at Most K Frequency**
Solve LeetCode Length of Longest Subarray With at Most K Frequency using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Length of Longest Subarray With at Most K Frequency |
| LeetCode | #2958 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer array  nums  and an integer  k .

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Complement Lookup / Hash Table Frequency**. By maintaining state efficiently in a **Dictionary / Hash Map**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Length of Longest Subarray With at Most K Frequency**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [1437. Check If All 1's Are at Least Length K Places Away](../1548-check-if-all-1s-are-at-least-length-k-places-away/)
- [1566. Detect Pattern of Length M Repeated K or More Times](../1689-detect-pattern-of-length-m-repeated-k-or-more-times/)
- [3043. Find the Length of the Longest Common Prefix](../3329-find-the-length-of-the-longest-common-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/)
