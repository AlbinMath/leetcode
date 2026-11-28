# LeetCode 2406: Divide Intervals Into Minimum Number of Groups

**LeetCode Problem #2406 — Divide Intervals Into Minimum Number of Groups**
Solve LeetCode Divide Intervals Into Minimum Number of Groups using JavaScript and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Divide Intervals Into Minimum Number of Groups |
| LeetCode | #2406 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D integer array `intervals` where `intervals[i] = [left_i, right_i]` represents the **inclusive** interval `[left_i, right_i]`.

You have to divide the intervals into one or more **groups** such that each interval is in **exactly** one group, and no two intervals that are in the same group **intersect** each other.

Return *the **minimum** number of groups you need to make*.

Two intervals **intersect** if there is at least one common number between them. For example, the intervals `[1, 5]` and `[5, 8]` intersect.

## Constraints
- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `1 <= left_i <= right_i <= 10^6`

## Examples
### Example 1
- **Input:** `intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]`
- **Output:** `3`
- **Explanation:** We can divide the intervals into the following groups:
- Group 1: [1, 5], [6, 8].
- Group 2: [2, 3], [5, 10].
- Group 3: [1, 10].
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.

### Example 2
- **Input:** `intervals = [[1,3],[5,6],[8,10],[11,13]]`
- **Output:** `1`
- **Explanation:** None of the intervals overlap, so we can put all of them in one group.

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Divide Intervals Into Minimum Number of Groups**, we observe the problem requirements and utilize the **Greedy** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We can divide the intervals into the following groups:
- Group 1: [1, 5], [6, 8].
- Group 2: [2, 3], [5, 10].
- Group 3: [1, 10].
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.

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
var minGroups = function(intervals) {
    intervals.sort((a, b) => a[0] - b[0]);
    let heap = [];
    function push(value) {
        heap.push(value);
        let i = heap.length - 1;
        while (i > 0) {
            let parent = Math.floor((i - 1) / 2);
            if (heap[parent] <= heap[i]) break;
            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    }
    function pop() {
        let min = heap[0];
        let last = heap.pop();
        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let left = 2 * i + 1;
                let right = 2 * i + 2;
                let smallest = i;
                if (
                    left < heap.length &&
                    heap[left] < heap[smallest]
                ) {
                    smallest = left;
                }
                if (
                    right < heap.length &&
                    heap[right] < heap[smallest]
                ) {
                    smallest = right;
                }
                if (smallest === i) break;
                [heap[i], heap[smallest]] =
                    [heap[smallest], heap[i]];
                i = smallest;
            }
        }
        return min;
    }
    for (let [start, end] of intervals) {
        if (heap.length > 0 && heap[0] < start) {
            pop();
        }
        push(end);
    }
    return heap.length;
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
- [2493. Divide Nodes Into the Maximum Number of Groups](../../2001-2500/2493-divide-nodes-into-the-maximum-number-of-groups/)
- [1689. Partitioning Into Minimum Number Of Deci-Binary Numbers](../../1501-2000/1689-partitioning-into-minimum-number-of-deci-binary-numbers/)
- [2910. Minimum Number of Groups to Create a Valid Assignment](../../2501-3000/2910-minimum-number-of-groups-to-create-a-valid-assignment/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/)
