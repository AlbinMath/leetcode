# LeetCode 2216: Minimum Deletions to Make Array Beautiful

**LeetCode Problem #2216 — Minimum Deletions to Make Array Beautiful**
Solve LeetCode Minimum Deletions to Make Array Beautiful using Java and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Deletions to Make Array Beautiful |
| LeetCode | #2216 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Array |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given the  head  of a linked list.  Delete  the  middle node , and return  the   head   of the modified linked list .

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Use **fast and slow pointers**. Fast moves 2 steps while slow moves 1. When fast reaches the end, slow is just before the middle. Delete the middle by setting `slow.next = slow.next.next`.

## Algorithm
1. Initialize state variables / data structure (**Linked List / Array**).
2. Process elements sequentially using **Floyd Cycle Detection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Deletions to Make Array Beautiful**. Applying **Floyd Cycle Detection** yields the target result step by step.

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
- [19. Remove Nth Node From End of List](../0019-remove-nth-node-from-end-of-list/)
- [2236. Root Equals Sum of Children](../2236-maximum-twin-sum-of-a-linked-list/)
- [61. Rotate List](../0061-rotate-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)
