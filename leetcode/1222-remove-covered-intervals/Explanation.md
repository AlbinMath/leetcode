# LeetCode 1222: Queens That Can Attack the King

**LeetCode Problem #1222 — Queens That Can Attack the King**
Solve LeetCode Queens That Can Attack the King using Java and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Queens That Can Attack the King |
| LeetCode | #1222 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem
Given an array  intervals  where  intervals[i] = [l i , r i ]  represent the interval  [l i , r i ) , remove all intervals that are covered by another interval in the list.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code uses **Sorting + Greedy**.

1. **Sort:** Sort intervals by start ascending. If starts are equal, sort by end **descending**. This ensures that if two intervals share the same start, the longer one comes first.
2. **Iterate:** Track `maxEnd` — the maximum end value seen so far. For each interval:
   - If `interval[1] > maxEnd`: This interval is NOT covered (it extends beyond all previous intervals), so increment the `count` and update `maxEnd`.
   - Otherwise: This interval is covered by a previous one (its end is ≤ `maxEnd`), so skip it.

Time complexity is $O(N \log N)$ for sorting and space complexity is $O(\log N)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Queens That Can Attack the King**. Applying **Modified Binary Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Java

## Source Code
- [solution.java](./solution.java)

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
- [19. Remove Nth Node From End of List](../0019-remove-nth-node-from-end-of-list/)
- [3561. Resulting String After Adjacent Removals](../3561-remove-methods-from-project/)
- [3562. Maximum Profit from Trading Stocks with Discounts](../3562-maximum-score-of-non-overlapping-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-covered-intervals/)
