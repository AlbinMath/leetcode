# LeetCode 56: Merge Intervals

**LeetCode Problem #56 — Merge Intervals**
Solve LeetCode Merge Intervals using JavaScript, Python and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Merge Intervals |
| LeetCode | #56 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

## Constraints
- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Examples
### Example 1
- **Input:** `intervals = [[1,3],[2,6],[8,10],[15,18]]`
- **Output:** `[[1,6],[8,10],[15,18]]`
- **Explanation:** Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

### Example 2
- **Input:** `intervals = [[1,4],[4,5]]`
- **Output:** `[[1,5]]`
- **Explanation:** Intervals [1,4] and [4,5] are considered overlapping.

### Example 3
- **Input:** `intervals = [[4,7],[1,4]]`
- **Output:** `[[1,7]]`
- **Explanation:** Intervals [1,4] and [4,7] are considered overlapping.

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Merge Intervals**, we observe the problem requirements and utilize the **Heap** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `intervals = [[1,3],[2,6],[8,10],[15,18]]`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,6],[8,10],[15,18]]`.
4. **Verification:** Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var merge = function(intervals) {
    // Sort intervals by their starting point
    intervals.sort((a, b) => a[0] - b[0]);

    const result = [];

    for (const interval of intervals) {
        // If result is empty or intervals do not overlap
        if (
            result.length === 0 ||
            result[result.length - 1][1] < interval[0]
        ) {
            result.push(interval);
        } else {
            // Merge overlapping intervals
            result[result.length - 1][1] = Math.max(
                result[result.length - 1][1],
                interval[1]
            );
        }
    }

    return result;
};
```

### Python
```python
class Solution:
    def merge(self, intervals):
        intervals.sort()
        res = []
        for s, e in intervals:
            if res and s <= res[-1][1]:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append([s, e])
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
- [352. Data Stream as Disjoint Intervals](../../0001-0500/0352-data-stream-as-disjoint-intervals/)
- [435. Non-overlapping Intervals](../../0001-0500/0435-non-overlapping-intervals/)
- [1288. Remove Covered Intervals](../../1001-1500/1288-remove-covered-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/merge-intervals/)
