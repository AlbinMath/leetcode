# LeetCode 470: Implement Rand10() Using Rand7()

**LeetCode Problem #470 — Implement Rand10() Using Rand7()**
Solve LeetCode Implement Rand10() Using Rand7() using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Implement Rand10() Using Rand7() |
| LeetCode | #470 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given the  API   rand7()  that generates a uniform random integer in the range  [1, 7] , write a function  rand10()  that generates a uniform random integer in the range  [1, 10] . You can only call the API  rand7() , and you shouldn&#39;t call any other API. Please  do not  use a language&#39;s built-in random API.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Implement Rand10() Using Rand7()**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [225. Implement Stack using Queues](../0225-implement-stack-using-queues/)
- [232. Implement Queue using Stacks](../0232-implement-queue-using-stacks/)
- [208. Implement Trie (Prefix Tree)](../0208-implement-trie-prefix-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/implement-rand10-using-rand7/)
