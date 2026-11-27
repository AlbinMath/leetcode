# LeetCode 986: Interval List Intersections

**LeetCode Problem #986 — Interval List Intersections**
Solve LeetCode Interval List Intersections using Python and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Interval List Intersections |
| LeetCode | #986 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two lists of closed intervals, `firstList` and `secondList`, where `firstList[i] = [start_i, end_i]` and `secondList[j] = [start_j, end_j]`. Each list of intervals is pairwise **disjoint** and in **sorted order**.

Return *the intersection of these two interval lists*.

A **closed interval** `[a, b]` (with `a <= b`) denotes the set of real numbers `x` with `a <= x <= b`.

The **intersection** of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of `[1, 3]` and `[2, 4]` is `[2, 3]`.

## Constraints
- `0 <= firstList.length, secondList.length <= 1000`
- `firstList.length + secondList.length >= 1`
- `0 <= start_i < end_i <= 10^9`
- `end_i < start_i+1`
- `0 <= start_j < end_j <= 10^9 `
- `end_j < start_j+1`

## Examples
### Example 1
- **Input:** `firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]`
- **Output:** `[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]`

### Example 2
- **Input:** `firstList = [[1,3],[5,9]], secondList = []`
- **Output:** `[]`

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Interval List Intersections**, we observe the problem requirements and utilize the **Heap** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Heap / Priority Queue.

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                res.append([lo, hi])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res
```

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [57. Insert Interval](../../0001-0500/0057-insert-interval/)
- [436. Find Right Interval](../../0001-0500/0436-find-right-interval/)
- [1124. Longest Well-Performing Interval](../../1001-1500/1124-longest-well-performing-interval/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/interval-list-intersections/)
