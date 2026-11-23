# LeetCode 4032: Longest Subarray With at Most K Distinct Prime Factors

**LeetCode Problem #4032 — Longest Subarray With at Most K Distinct Prime Factors**
Solve LeetCode Longest Subarray With at Most K Distinct Prime Factors using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Subarray With at Most K Distinct Prime Factors |
| LeetCode | #4032 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer array  nums  consisting of positive integers and an integer  k .

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Subarray With at Most K Distinct Prime Factors**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [2958. Length of Longest Subarray With at Most K Frequency](../3225-length-of-longest-subarray-with-at-most-k-frequency/)
- [3830. Longest Alternating Subarray After Removing At Most One Element](../4198-longest-alternating-subarray-after-removing-at-most-one-element/)
- [3962. Maximum Subarray Sum After at Most K Swaps](../4246-maximum-subarray-sum-after-at-most-k-swaps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-subarray-with-at-most-k-distinct-prime-factors/)
