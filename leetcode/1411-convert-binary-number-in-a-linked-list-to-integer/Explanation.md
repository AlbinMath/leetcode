# LeetCode 1290: Convert Binary Number in a Linked List to Integer

**LeetCode Problem #1290 — Convert Binary Number in a Linked List to Integer**
Solve LeetCode Convert Binary Number in a Linked List to Integer using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Convert Binary Number in a Linked List to Integer |
| LeetCode | #1290 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given  head  which is a reference node to a singly-linked list. The value of each node in the linked list is either  0  or  1 . The linked list holds the binary representation of a number.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Convert Binary Number in a Linked List to Integer**. Applying **Modified Binary Search** yields the target result step by step.

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
Python

## Source Code
- [solution.py](./solution.py)

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
- [108. Convert Sorted Array to Binary Search Tree](../0108-convert-sorted-array-to-binary-search-tree/)
- [141. Linked List Cycle](../0141-linked-list-cycle/)
- [203. Remove Linked List Elements](../0203-remove-linked-list-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/)
