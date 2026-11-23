# LeetCode 1203: Sort Items by Groups Respecting Dependencies

**LeetCode Problem #1203 — Sort Items by Groups Respecting Dependencies**
Solve LeetCode Sort Items by Groups Respecting Dependencies using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sort Items by Groups Respecting Dependencies |
| LeetCode | #1203 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` items each belonging to zero or one of `m` groups where `group[i]` is the group that the `i`-th item belongs to and it's equal to `-1` if the `i`-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list. 
 There are some relations between these items where `beforeItems[i]` is a list containing all the items that should come before the `i`-th item in the sorted array (to the left of the `i`-th item).

Return any solution if there is more than one solution and return an **empty list** if there is no solution.

## Constraints
- `1 <= m <= n <= 3 * 10^4`
- `group.length == beforeItems.length == n`
- `-1 <= group[i] <= m - 1`
- `0 <= beforeItems[i].length <= n - 1`
- `0 <= beforeItems[i][j] <= n - 1`
- `i != beforeItems[i][j]`
- `beforeItems[i] `does not contain duplicates elements.

## Examples
### Example 1
- **Input:** `n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]`
- **Output:** `[6,3,4,1,5,2,0,7]`

### Example 2
- **Input:** `n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]`
- **Output:** `[]`
- **Explanation:** This is the same as

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sort Items by Groups Respecting Dependencies**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[6,3,4,1,5,2,0,7]`.

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
/**
 * @param {number} n
 * @param {number} m
 * @param {number[]} group
 * @param {number[][]} beforeItems
 * @return {number[]}
 */
var sortItems = function (n, m, group, beforeItems) {
    // give ungrouped items their own unique group
    let g = m;
    for (let i = 0; i < n; i++) if (group[i] === -1) group[i] = g++;

    const itemAdj = Array.from({ length: n }, () => []);
    const itemDeg = new Array(n).fill(0);
    const groupAdj = Array.from({ length: g }, () => []);
    const groupDeg = new Array(g).fill(0);

    for (let i = 0; i < n; i++) {
        for (const b of beforeItems[i]) {
            itemAdj[b].push(i);
            itemDeg[i]++;
            if (group[b] !== group[i]) {
                groupAdj[group[b]].push(group[i]);
                groupDeg[group[i]]++;
            }
        }
    }

    const topo = (size, adj, deg) => {
        const q = [];
        for (let i = 0; i < size; i++) if (deg[i] === 0) q.push(i);
        let head = 0;
        while (head < q.length) {
            const u = q[head++];
            for (const v of adj[u]) if (--deg[v] === 0) q.push(v);
        }
        return q.length === size ? q : null;
    };

    const itemOrder = topo(n, itemAdj, itemDeg);
    if (!itemOrder) return [];
    const groupOrder = topo(g, groupAdj, groupDeg);
    if (!groupOrder) return [];

    const buckets = Array.from({ length: g }, () => []);
    for (const it of itemOrder) buckets[group[it]].push(it);

    const res = [];
    for (const gr of groupOrder) for (const it of buckets[gr]) res.push(it);
    return res;
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
- [1773. Count Items Matching a Rule](../../1501-2000/1899-count-items-matching-a-rule/)
- [2146. K Highest Ranked Items Within a Price Range](../../2001-2500/2250-k-highest-ranked-items-within-a-price-range/)
- [3789. Minimum Cost to Acquire Required Items](../../4001-4500/4147-minimum-cost-to-acquire-required-items/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/)
