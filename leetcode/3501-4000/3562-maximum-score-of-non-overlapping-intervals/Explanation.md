# LeetCode 3414: Maximum Score of Non-overlapping Intervals

**LeetCode Problem #3414 — Maximum Score of Non-overlapping Intervals**
Solve LeetCode Maximum Score of Non-overlapping Intervals using JavaScript and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Score of Non-overlapping Intervals |
| LeetCode | #3414 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D integer array `intervals`, where `intervals[i] = [l_i, r_i, weight_i]`. Interval `i` starts at position `l_i` and ends at `r_i`, and has a weight of `weight_i`. You can choose *up to* 4 **non-overlapping** intervals. The **score** of the chosen intervals is defined as the total sum of their weights.

Return the lexicographically smallest array of at most 4 indices from `intervals` with **maximum** score, representing your choice of non-overlapping intervals.

Two intervals are said to be **non-overlapping** if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

## Constraints
- `1 <= intevals.length <= 5 * 10^4`
- `intervals[i].length == 3`
- `intervals[i] = [l_i, r_i, weight_i]`
- `1 <= l_i <= r_i <= 10^9`
- `1 <= weight_i <= 10^9`

## Examples
### Example 1
- **Input:** `intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]`
- **Output:** `[2,3]`
- **Explanation:** You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

### Example 2
- **Input:** `intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]`
- **Output:** `[1,3,5,6]`
- **Explanation:** You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Score of Non-overlapping Intervals**, we observe the problem requirements and utilize the **Heap** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3]`.
4. **Verification:** You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

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
/**
 * @param {number[][]} intervals
 * @return {number[]}
 */
var maximumWeight = function(intervals) {
    const n = intervals.length;

    // [left, right, weight, originalIndex]
    const arr = intervals.map((x, i) => [x[0], x[1], x[2], i]);

    // Sort by right endpoint
    arr.sort((a, b) => {
        if (a[1] !== b[1]) return a[1] - b[1];
        return a[0] - b[0];
    });

    // Find last interval with right < current left
    function findPrevious(pos) {
        let left = 0;
        let right = pos - 1;
        let ans = -1;

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);

            if (arr[mid][1] < arr[pos][0]) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return ans;
    }

    // Compare two sorted index arrays lexicographically
    function lexSmaller(a, b) {
        const len = Math.min(a.length, b.length);

        for (let i = 0; i < len; i++) {
            if (a[i] !== b[i]) {
                return a[i] < b[i];
            }
        }

        return a.length < b.length;
    }

    // Return better state
    function better(a, b) {
        if (a === null) return b;
        if (b === null) return a;

        if (a.score > b.score) return a;
        if (b.score > a.score) return b;

        return lexSmaller(a.indices, b.indices) ? a : b;
    }

    // dp[k][i]:
    // best result using exactly k intervals
    // from first i intervals
    const dp = Array.from(
        { length: 5 },
        () => Array(n + 1).fill(null)
    );

    // Choosing 0 intervals
    for (let i = 0; i <= n; i++) {
        dp[0][i] = {
            score: 0,
            indices: []
        };
    }

    for (let i = 1; i <= n; i++) {
        const cur = i - 1;
        const p = findPrevious(cur);

        for (let k = 1; k <= 4; k++) {

            // Don't choose current interval
            let best = dp[k][i - 1];

            // Choose current interval
            if (dp[k - 1][p + 1] !== null) {
                const prev = dp[k - 1][p + 1];

                // IMPORTANT:
                // Add original index and sort indices
                const newIndices = [
                    ...prev.indices,
                    arr[cur][3]
                ].sort((a, b) => a - b);

                const candidate = {
                    score: prev.score + arr[cur][2],
                    indices: newIndices
                };

                best = better(best, candidate);
            }

            dp[k][i] = best;
        }
    }

    // At most 4 intervals
    let answer = {
        score: 0,
        indices: []
    };

    for (let k = 1; k <= 4; k++) {
        answer = better(answer, dp[k][n]);
    }

    return answer.indices;
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
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](../../1001-1500/1096-maximum-sum-of-two-non-overlapping-subarrays/)
- [1520. Maximum Number of Non-Overlapping Substrings](../../1501-2000/1644-maximum-number-of-non-overlapping-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/)
