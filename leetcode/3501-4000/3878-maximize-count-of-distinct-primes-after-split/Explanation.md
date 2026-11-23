# LeetCode 3569: Maximize Count of Distinct Primes After Split

**LeetCode Problem #3569 — Maximize Count of Distinct Primes After Split**
Solve LeetCode Maximize Count of Distinct Primes After Split using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Count of Distinct Primes After Split |
| LeetCode | #3569 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  nums  having length  n  and a 2D integer array  queries  where  queries[i] = [idx, val] .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximize Count of Distinct Primes After Split**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [204. Count Primes](../../0001-0500/0204-count-primes/)
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1047-maximize-sum-of-array-after-k-negations/)
- [1799. Maximize Score After N Operations](../../1501-2000/1906-maximize-score-after-n-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/)
