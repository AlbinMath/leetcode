# LeetCode 2359: Find Closest Node to Given Two Nodes

**LeetCode Problem #2359 — Find Closest Node to Given Two Nodes**
Solve LeetCode Find Closest Node to Given Two Nodes using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Closest Node to Given Two Nodes |
| LeetCode | #2359 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  directed  graph of  n  nodes numbered from  0  to  n - 1 , where each node has  at most one  outgoing edge.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Closest Node to Given Two Nodes**. Applying **Modified Binary Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [564. Find the Closest Palindrome](../../0501-1000/0564-find-the-closest-palindrome/)
- [658. Find K Closest Elements](../../0501-1000/0658-find-k-closest-elements/)
- [1521. Find a Value of a Mysterious Function Closest to Target](../../1501-2000/1645-find-a-value-of-a-mysterious-function-closest-to-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/)
