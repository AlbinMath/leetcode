# LeetCode 19: Remove Nth Node From End of List

**LeetCode Problem #19 — Remove Nth Node From End of List**
Solve LeetCode Remove Nth Node From End of List using JavaScript and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Nth Node From End of List |
| LeetCode | #19 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Array |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given the  head  of a linked list, remove the  n th   node from the end of the list and return its head.

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses the **Two Pointer (Fast & Slow)** technique to find the target node in a single pass.

1. **Dummy Node:** A `dummy` node is created before the `head`. This handles the edge case where the head itself needs to be removed.
2. **Advance Fast Pointer:** The `fast` pointer is moved `n` steps ahead from `dummy`.
3. **Move Both Pointers:** Both `fast` and `slow` are moved one step at a time until `fast.next` becomes `null`. At this point, `slow` is exactly one node **before** the node that needs to be removed.
4. **Remove the Node:** The target node is skipped by setting `slow.next = slow.next.next`.
5. It returns `dummy.next`, which is the new head of the list.

Time complexity is $O(L)$ where $L$ is the length of the list. Space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Linked List / Array**).
2. Process elements sequentially using **Floyd Cycle Detection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Remove Nth Node From End of List**. Applying **Floyd Cycle Detection** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [3062. Winner of the Linked List Game](../3062-create-a-dataframe-from-list/)
- [3561. Resulting String After Adjacent Removals](../3561-remove-methods-from-project/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
