# LeetCode 508: Most Frequent Subtree Sum

**LeetCode Problem #508 — Most Frequent Subtree Sum**
Solve LeetCode Most Frequent Subtree Sum using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Most Frequent Subtree Sum |
| LeetCode | #508 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given the  root  of a binary tree, return the most frequent  subtree sum . If there is a tie, return all the values with the highest frequency in any order.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Complement Lookup / Hash Table Frequency**. By maintaining state efficiently in a **Dictionary / Hash Map**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Most Frequent Subtree Sum**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [1838. Frequency of the Most Frequent Element](../1966-frequency-of-the-most-frequent-element/)
- [3044. Most Frequent Prime](../3314-most-frequent-prime/)
- [3962. Maximum Subarray Sum After at Most K Swaps](../4246-maximum-subarray-sum-after-at-most-k-swaps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/most-frequent-subtree-sum/)
