# LeetCode 436: Find Right Interval

**LeetCode Problem #436 — Find Right Interval**
Solve LeetCode Find Right Interval using JavaScript and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Right Interval |
| LeetCode | #436 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of `intervals`, where `intervals[i] = [start_i, end_i]` and each `start_i` is **unique**.

The **right interval** for an interval `i` is an interval `j` such that `start_j >= end_i` and `start_j` is **minimized**. Note that `i` may equal `j`.

Return *an array of **right interval** indices for each interval `i`*. If no **right interval** exists for interval `i`, then put `-1` at index `i`.

## Constraints
- `1 <= intervals.length <= 2 * 10^4`
- `intervals[i].length == 2`
- `-10^6 <= start_i <= end_i <= 10^6`
- The start point of each interval is **unique**.

## Examples
### Example 1
- **Input:** `intervals = [[1,2]]`
- **Output:** `[-1]`
- **Explanation:** There is only one interval in the collection, so it outputs -1.

### Example 2
- **Input:** `intervals = [[3,4],[2,3],[1,2]]`
- **Output:** `[-1,0,1]`
- **Explanation:** There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start_0 = 3 is the smallest start that is >= end_1 = 3.
The right interval for [1,2] is [2,3] since start_1 = 2 is the smallest start that is >= end_2 = 2.

### Example 3
- **Input:** `intervals = [[1,4],[2,3],[3,4]]`
- **Output:** `[-1,2,-1]`
- **Explanation:** There is no right interval for [1,4] and [3,4].
The right interval for [2,3] is [3,4] since start_2 = 3 is the smallest start that is >= end_1 = 3.

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Right Interval**, we observe the problem requirements and utilize the **Heap** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `intervals = [[1,2]]`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[-1]`.
4. **Verification:** There is only one interval in the collection, so it outputs -1.

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
var findRightInterval = function(intervals) {
    const n = intervals.length;
    const starts = [];

    for (let i = 0; i < n; i++) {
        starts.push([intervals[i][0], i]);
    }

    starts.sort((a, b) => a[0] - b[0]);

    const result = [];

    for (let i = 0; i < n; i++) {
        const target = intervals[i][1];
        let left = 0;
        let right = n - 1;
        let ans = -1;

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);

            if (starts[mid][0] >= target) {
                ans = starts[mid][1];
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        result.push(ans);
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
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)
- [153. Find Minimum in Rotated Sorted Array](../../0001-0500/0153-find-minimum-in-rotated-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-right-interval/)
