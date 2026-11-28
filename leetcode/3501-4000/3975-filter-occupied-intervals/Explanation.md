# LeetCode 3975: Filter Occupied Intervals

**LeetCode Problem #3975 — Filter Occupied Intervals**
Solve LeetCode Filter Occupied Intervals using JavaScript and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Filter Occupied Intervals |
| LeetCode | #3975 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D integer array `occupiedIntervals`, where `occupiedIntervals[i] = [start_i, end_i]` represents a time interval during which you are occupied. Each interval starts at `start_i` and ends at `end_i`, **inclusive**. These intervals may **overlap**.

You are also given two integers `freeStart` and `freeEnd`, which define a free time interval from `freeStart` to `freeEnd`, inclusive.

Your task is to merge **all** occupied intervals that overlap or touch, then remove **all** integer points in the free interval from the merged occupied intervals.

Two intervals touch if the second interval starts **immediately after** the first one ends. For example, `[1, 1]` and `[2, 2]` touch and should be merged into `[1, 2]`.

Return the **remaining** occupied intervals in **sorted** order. The returned intervals must be **non-overlapping** and must contain the **minimum** number of intervals possible. If there are no remaining occupied points, return an empty list.

## Constraints
- `1 <= occupiedIntervals.length <= 5 * 10^4`
- `occupiedIntervals[i].length == 2`
- `1 <= start_i <= end_i <= 10^9`
- `1 <= freeStart <= freeEnd <= 10^9`

## Examples
### Example 1
- **Input:** `occupiedIntervals = [[2,6],[4,8],[10,10],[10,12],[14,16]], freeStart = 7, freeEnd = 11`
- **Output:** `[[2,6],[12,12],[14,16]]`
- **Explanation:** After merging, the occupied intervals are `[2, 8]`, `[10, 12]`, and `[14, 16]`. 
 Excluding the free interval `[7, 11]` results in `[2, 6]`, `[12, 12]`, and `[14, 16]`.

### Example 2
- **Input:** `occupiedIntervals = [[1,5],[2,3]], freeStart = 3, freeEnd = 8`
- **Output:** `[[1,2]]`
- **Explanation:** After merging, the occupied interval is `[1, 5]`. 
 Excluding the free interval `[3, 8]` results in `[1, 2]`.

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Filter Occupied Intervals**, we observe the problem requirements and utilize the **Greedy** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `occupiedIntervals = [[2,6],[4,8],[10,10],[10,12],[14,16]], freeStart = 7, freeEnd = 11`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[2,6],[12,12],[14,16]]`.
4. **Verification:** After merging, the occupied intervals are `[2, 8]`, `[10, 12]`, and `[14, 16]`. 
 Excluding the free interval `[7, 11]` results in `[2, 6]`, `[12, 12]`, and `[14, 16]`.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var filterOccupiedIntervals = function(occupiedIntervals, freeStart, freeEnd) {
    occupiedIntervals.sort((a, b) => a[0] - b[0]);
    const merged = [];
    for (const [start, end] of occupiedIntervals) {
        if (
            merged.length === 0 ||
            start > merged[merged.length - 1][1] + 1
        ) {
            merged.push([start, end]);
        } else {
            merged[merged.length - 1][1] = Math.max(
                merged[merged.length - 1][1],
                end
            );
        }
    }
    const result = [];
    for (const [start, end] of merged) {
        if (end < freeStart || start > freeEnd) {
            result.push([start, end]);
            continue;
        }
        if (start < freeStart) {
            result.push([start, freeStart - 1]);
        }
        if (end > freeEnd) {
            result.push([freeEnd + 1, end]);
        }
    }
    return result;
};
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
- [56. Merge Intervals](../../0001-0500/0056-merge-intervals/)
- [352. Data Stream as Disjoint Intervals](../../0001-0500/0352-data-stream-as-disjoint-intervals/)
- [435. Non-overlapping Intervals](../../0001-0500/0435-non-overlapping-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/filter-occupied-intervals/)
