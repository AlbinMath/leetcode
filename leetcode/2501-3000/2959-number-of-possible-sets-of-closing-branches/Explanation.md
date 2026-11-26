# LeetCode 2959: Number of Possible Sets of Closing Branches

**LeetCode Problem #2959 — Number of Possible Sets of Closing Branches**
Solve LeetCode Number of Possible Sets of Closing Branches using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Possible Sets of Closing Branches |
| LeetCode | #2959 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a company with `n` branches across the country, some of which are connected by roads. Initially, all branches are reachable from each other by traveling some roads.

The company has realized that they are spending an excessive amount of time traveling between their branches. As a result, they have decided to close down some of these branches (**possibly none**). However, they want to ensure that the remaining branches have a distance of at most `maxDistance` from each other.

The **distance** between two branches is the **minimum** total traveled length needed to reach one branch from another.

You are given integers `n`, `maxDistance`, and a **0-indexed** 2D array `roads`, where `roads[i] = [u_i, v_i, w_i]` represents the **undirected** road between branches `u_i` and `v_i` with length `w_i`.

Return *the number of possible sets of closing branches, so that any branch has a distance of at most *`maxDistance`* from any other*.

**Note** that, after closing a branch, the company will no longer have access to any roads connected to it.

**Note** that, multiple roads are allowed.

## Constraints
- `1 <= n <= 10`
- `1 <= maxDistance <= 10^5`
- `0 <= roads.length <= 1000`
- `roads[i].length == 3`
- `0 <= u_i, v_i <= n - 1`
- `u_i != v_i`
- `1 <= w_i <= 1000`
- All branches are reachable from each other by traveling some roads.

## Examples
### Example 1
- **Input:** `n = 3, maxDistance = 5, roads = [[0,1,2],[1,2,10],[0,2,10]]`
- **Output:** `5`
- **Explanation:** The possible sets of closing branches are:
- The set [2], after closing, active branches are [0,1] and they are reachable to each other within distance 2.
- The set [0,1], after closing, the active branch is [2].
- The set [1,2], after closing, the active branch is [0].
- The set [0,2], after closing, the active branch is [1].
- The set [0,1,2], after closing, there are no active branches.
It can be proven, that there are only 5 possible sets of closing branches.

### Example 2
- **Input:** `n = 3, maxDistance = 5, roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]`
- **Output:** `7`
- **Explanation:** The possible sets of closing branches are:
- The set [], after closing, active branches are [0,1,2] and they are reachable to each other within distance 4.
- The set [0], after closing, active branches are [1,2] and they are reachable to each other within distance 2.
- The set [1], after closing, active branches are [0,2] and they are reachable to each other within distance 2.
- The set [0,1], after closing, the active branch is [2].
- The set [1,2], after closing, the active branch is [0].
- The set [0,2], after closing, the active branch is [1].
- The set [0,1,2], after closing, there are no active branches.
It can be proven, that there are only 7 possible sets of closing branches.

### Example 3
- **Input:** `n = 1, maxDistance = 10, roads = []`
- **Output:** `2`
- **Explanation:** The possible sets of closing branches are:
- The set [], after closing, the active branch is [0].
- The set [0], after closing, there are no active branches.
It can be proven, that there are only 2 possible sets of closing branches.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Possible Sets of Closing Branches**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, maxDistance = 5, roads = [[0,1,2],[1,2,10],[0,2,10]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The possible sets of closing branches are:
- The set [2], after closing, active branches are [0,1] and they are reachable to each other within distance 2.
- The set [0,1], after closing, the active branch is [2].
- The set [1,2], after closing, the active branch is [0].
- The set [0,2], after closing, the active branch is [1].
- The set [0,1,2], after closing, there are no active branches.
It can be proven, that there are only 5 possible sets of closing branches.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var numberOfSets = function (n, maxDistance, roads) {
    const INF = 1e9;

    // Base matrix with the cheapest road between each pair
    const base = Array.from({ length: n }, () => new Array(n).fill(INF));
    for (let i = 0; i < n; i++) base[i][i] = 0;
    for (const [u, v, w] of roads) {
        if (w < base[u][v]) {
            base[u][v] = w;
            base[v][u] = w;
        }
    }

    let count = 0;
    for (let mask = 0; mask < (1 << n); mask++) {
        // Copy distances among active nodes only
        const d = base.map((row) => row.slice());

        // Floyd-Warshall, using only active intermediate nodes
        for (let k = 0; k < n; k++) {
            if (!(mask >> k & 1)) continue;
            for (let i = 0; i < n; i++) {
                if (!(mask >> i & 1)) continue;
                for (let j = 0; j < n; j++) {
                    if (!(mask >> j & 1)) continue;
                    if (d[i][k] + d[k][j] < d[i][j]) {
                        d[i][j] = d[i][k] + d[k][j];
                    }
                }
            }
        }

        let ok = true;
        for (let i = 0; i < n && ok; i++) {
            if (!(mask >> i & 1)) continue;
            for (let j = i + 1; j < n; j++) {
                if (!(mask >> j & 1)) continue;
                if (d[i][j] > maxDistance) {
                    ok = false;
                    break;
                }
            }
        }
        if (ok) count++;
    }
    return count;
};
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3309. Maximum Possible Number by Binary Concatenation](../../3001-3500/3309-maximum-possible-number-by-binary-concatenation/)
- [3317. Find the Number of Possible Ways for an Event](../../3001-3500/3317-find-the-number-of-possible-ways-for-an-event/)
- [1621. Number of Sets of K Non-Overlapping Line Segments](../../1501-2000/1621-number-of-sets-of-k-non-overlapping-line-segments/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/)
