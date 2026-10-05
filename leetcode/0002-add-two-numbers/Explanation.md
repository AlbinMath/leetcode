# LeetCode 2: Add Two Numbers

**LeetCode Problem #2 — Add Two Numbers**
Solve LeetCode Add Two Numbers using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Add Two Numbers |
| LeetCode | #2 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two  non-empty  linked lists representing two non-negative integers. The digits are stored in  reverse order , and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
The code uses a simulated digit-by-digit addition, similar to how you would add numbers on paper:
1. It initializes a `dummy` node to act as the head of the result list, and a `current` pointer to build the new list.
2. It uses a `carry` variable (initially 0) to keep track of values that carry over to the next place value (e.g., if sum >= 10).
3. A `while` loop runs as long as there is a node in `l1`, a node in `l2`, or a remaining `carry` greater than 0.
4. Inside the loop, it safely extracts the values from `l1` and `l2` (defaulting to 0 if one list is shorter than the other).
5. It calculates the `total` sum for the current position (`val1 + val2 + carry`).
6. The `digit` to store in the new node is `total % 10`, and the new `carry` for the next iteration is `total // 10`.
7. It creates a new node with this `digit`, attaches it to the result list, and moves all pointers (`l1`, `l2`, and `current`) forward.
8. Finally, it returns `dummy.next`, which is the head of the newly constructed sum list.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Add Two Numbers**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
Python

## Source Code
- [solution.py](./solution.py)

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
- [2723. Add Two Promises](../2859-add-two-promises/)
- [1. Two Sum](../0001-two-sum/)
- [4. Median of Two Sorted Arrays](../0004-median-of-two-sorted-arrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/add-two-numbers/)
