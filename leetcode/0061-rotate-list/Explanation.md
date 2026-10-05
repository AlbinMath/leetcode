# LeetCode 61: Rotate List

**LeetCode Problem #61 — Rotate List**
Solve LeetCode Rotate List using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence / Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rotate List |
| LeetCode | #61 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Two Pointer Convergence / Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given the  head  of a linked list, rotate the list to the right by  k  places.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
1. **Edge Cases:** Returns immediately if the list is empty, has one node, or `k` is 0.
2. **Find Length and Tail:** Traverses the list to find its length `n` and a pointer to the `tail` node.
3. **Effective Rotations:** Computes `k = k % n` to avoid redundant full rotations. If `k` becomes 0, no rotation is needed.
4. **Make Circular:** Connects the tail to the head (`tail->next = head`), creating a circular list.
5. **Find the New Tail:** The new tail is the node at position `n - k - 1` from the current head (i.e., `steps = n - k` steps from the beginning). This is where the list will be "cut."
6. **Break the Circle:** The new head is `newTail->next`, and the circle is broken by setting `newTail->next = nullptr`.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence / Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Rotate List**. Applying **Two Pointer Convergence / Scanning** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [19. Remove Nth Node From End of List](../0019-remove-nth-node-from-end-of-list/)
- [48. Rotate Image](../0048-rotate-image/)
- [396. Rotate Function](../0396-rotate-function/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rotate-list/)
