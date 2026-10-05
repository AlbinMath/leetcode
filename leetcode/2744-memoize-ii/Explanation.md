# LeetCode 2744: Find Maximum Number of String Pairs

**LeetCode Problem #2744 — Find Maximum Number of String Pairs**
Solve LeetCode Find Maximum Number of String Pairs using TypeScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Maximum Number of String Pairs |
| LeetCode | #2744 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a function  fn , return a  memoized  version of that function.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
Uses a **trie-like cache** or `WeakMap`/`Map` structure keyed by argument references. For each call, traverses the cache structure using each argument as a key, creating new nodes as needed. At the final node, stores the computed result for future lookups.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Maximum Number of String Pairs**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)
- [602. Friend Requests II: Who Has the Most Friends](../0602-friend-requests-ii-who-has-the-most-friends/)
- [977. Squares of a Sorted Array](../0977-distinct-subsequences-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/memoize-ii/)
