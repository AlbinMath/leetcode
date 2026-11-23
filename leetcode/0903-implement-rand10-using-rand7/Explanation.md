# LeetCode 470: Implement Rand10() Using Rand7()

**LeetCode Problem #470 — Implement Rand10() Using Rand7()**
Solve LeetCode Implement Rand10() Using Rand7() using JavaScript and Trie. This solution finds the optimal result using Prefix Tree Lookup in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Implement Rand10() Using Rand7() |
| LeetCode | #470 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Prefix Tree Lookup |
| Data Structure | Trie Node |
| Pattern | Trie |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given the  API   rand7()  that generates a uniform random integer in the range  [1, 7] , write a function  rand10()  that generates a uniform random integer in the range  [1, 10] . You can only call the API  rand7() , and you shouldn&#39;t call any other API. Please  do not  use a language&#39;s built-in random API.

## Key Insight
Leverage **Trie** with **Trie Node** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Trie Node**).
2. Process elements sequentially using **Prefix Tree Lookup**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Implement Rand10() Using Rand7()**. Applying **Prefix Tree Lookup** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Trie**

## Topics
- Trie
- String
- Prefix Search

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Trie**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

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
- [1320. Minimum Distance to Type a Word Using Two Fingers](../1443-minimum-distance-to-type-a-word-using-two-fingers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/implement-rand10-using-rand7/)
