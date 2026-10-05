# LeetCode 2762: Continuous Subarrays

**LeetCode Problem #2762 — Continuous Subarrays**
Solve LeetCode Continuous Subarrays using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Continuous Subarrays |
| LeetCode | #2762 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Write a class that allows getting and setting key-value pairs, however a  time until expiration  is associated with each key.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
Uses a Map to store `{value, timer}` for each key. On `set`, clear any existing timer and create a new `setTimeout` that deletes the key after `duration` ms. On `get`, return the value if the key exists. On `count`, return the Map's size.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Continuous Subarrays**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [2749. Minimum Operations to Make the Integer Zero](../2749-promise-time-limit/)
- [636. Exclusive Time of Functions](../0636-exclusive-time-of-functions/)
- [1801. Number of Orders in the Backlog](../1801-average-time-of-process-per-machine/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cache-with-time-limit/)
