# LeetCode 2236: Root Equals Sum of Children

**LeetCode Problem #2236 — Root Equals Sum of Children**
Solve LeetCode Root Equals Sum of Children using Java and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Root Equals Sum of Children |
| LeetCode | #2236 |
| Difficulty | Easy |
| Language | Java |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Array |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
In a linked list of size  n , where  n  is  even , the  i th   node ( 0-indexed ) of the linked list is known as the  twin  of the  (n-1-i) th   node, if  0 <= i <= (n / 2) - 1 .

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Find the middle using fast/slow pointers, reverse the second half, then iterate both halves simultaneously to compute twin sums and track the maximum.

## Algorithm
1. Initialize state variables / data structure (**Linked List / Array**).
2. Process elements sequentially using **Floyd Cycle Detection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Root Equals Sum of Children**. Applying **Floyd Cycle Detection** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
Java

## Source Code
- [solution.java](./solution.java)

## Why This Works
By utilizing **Fast & Slow Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2216. Minimum Deletions to Make Array Beautiful](../2216-delete-the-middle-node-of-a-linked-list/)
- [1. Two Sum](../0001-two-sum/)
- [19. Remove Nth Node From End of List](../0019-remove-nth-node-from-end-of-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/)
