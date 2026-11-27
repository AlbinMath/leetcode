# LeetCode 57: Insert Interval

**LeetCode Problem #57 — Insert Interval**
Solve LeetCode Insert Interval using Python and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Insert Interval |
| LeetCode | #57 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represent the start and the end of the `i^th` interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Two intervals are considered overlapping if they share **at least** one point.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals`* after the insertion*.

**Note** that you don't need to modify `intervals` in-place. You can make a new array and return it.

## Constraints
- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^5`
- `intervals` is sorted by `start_i` in **ascending** order.
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`

## Examples
### Example 1
- **Input:** `intervals = [[1,3],[6,9]], newInterval = [2,5]`
- **Output:** `[[1,5],[6,9]]`

### Example 2
- **Input:** `intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]`
- **Output:** `[[1,2],[3,10],[12,16]]`
- **Explanation:** Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Insert Interval**, we observe the problem requirements and utilize the **Heap** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `intervals = [[1,3],[6,9]], newInterval = [2,5]`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,5],[6,9]]`.

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
class Solution:
    def insert(self, intervals, newInterval):
        result = []

        i = 0
        n = len(intervals)

        # 1. Add intervals completely before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2. Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged interval
        result.append(newInterval)

        # 3. Add intervals completely after newInterval
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
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
- [436. Find Right Interval](../../0001-0500/0436-find-right-interval/)
- [986. Interval List Intersections](../../0501-1000/0986-interval-list-intersections/)
- [1124. Longest Well-Performing Interval](../../1001-1500/1124-longest-well-performing-interval/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/insert-interval/)
