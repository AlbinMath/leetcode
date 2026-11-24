# LeetCode 2662: Minimum Cost of a Path With Special Roads

**LeetCode Problem #2662 — Minimum Cost of a Path With Special Roads**
Solve LeetCode Minimum Cost of a Path With Special Roads using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost of a Path With Special Roads |
| LeetCode | #2662 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `start` where `start = [startX, startY]` represents your initial position `(startX, startY)` in a 2D space. You are also given the array `target` where `target = [targetX, targetY]` represents your target position `(targetX, targetY)`.

The **cost** of going from a position `(x1, y1)` to any other position in the space `(x2, y2)` is `|x2 - x1| + |y2 - y1|`.

There are also some **special roads**. You are given a 2D array `specialRoads` where `specialRoads[i] = [x1_i, y1_i, x2_i, y2_i, cost_i]` indicates that the `i^th` special road goes in **one direction** from `(x1_i, y1_i)` to `(x2_i, y2_i)` with a cost equal to `cost_i`. You can use each special road any number of times.

Return the **minimum** cost required to go from `(startX, startY)` to `(targetX, targetY)`.

## Constraints
- `start.length == target.length == 2`
- `1 <= startX <= targetX <= 10^5`
- `1 <= startY <= targetY <= 10^5`
- `1 <= specialRoads.length <= 200`
- `specialRoads[i].length == 5`
- `startX <= x1_i, x2_i <= targetX`
- `startY <= y1_i, y2_i <= targetY`
- `1 <= cost_i <= 10^5`

## Examples
### Example 1
- **Input:** `start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]`
- **Output:** `5`
- **Explanation:** (1,1) to (1,2) with a cost of |1 - 1| + |2 - 1| = 1. 
 (1,2) to (3,3). Use ` specialRoads[0] ` with the cost 2. 
 (3,3) to (3,4) with a cost of |3 - 3| + |4 - 3| = 1. 
 (3,4) to (4,5). Use ` specialRoads[1] ` with the cost 1. 
 

 So the total cost is 1 + 2 + 1 + 1 = 5.

### Example 2
- **Input:** `start = [3,2], target = [5,7], specialRoads = [[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]`
- **Output:** `7`
- **Explanation:** It is optimal not to use any special edges and go directly from the starting to the ending position with a cost |5 - 3| + |7 - 2| = 7. 

 Note that the `specialRoads[0]` is directed from (5,7) to (3,2).

### Example 3
- **Input:** `start = [1,1], target = [10,4], specialRoads = [[4,2,1,1,3],[1,2,7,4,4],[10,3,6,1,2],[6,1,1,2,3]]`
- **Output:** `8`
- **Explanation:** (1,1) to (1,2) with a cost of |1 - 1| + |2 - 1| = 1. 
 (1,2) to (7,4). Use ` specialRoads[1] ` with the cost 4. 
 (7,4) to (10,4) with a cost of |10 - 7| + |4 - 4| = 3.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Cost of a Path With Special Roads**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** (1,1) to (1,2) with a cost of |1 - 1| + |2 - 1| = 1. 
 (1,2) to (3,3). Use ` specialRoads[0] ` with the cost 2. 
 (3,3) to (3,4) with a cost of |3 - 3| + |4 - 3| = 1. 
 (3,4) to (4,5). Use ` specialRoads[1] ` with the cost 1. 
 

 So the total cost is 1 + 2 + 1 + 1 = 5.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minimumCost = function (start, target, specialRoads) {
    const pts = [start, target];
    const index = new Map();
    const key = (x, y) => x * 100001 + y;
    const getId = (x, y) => {
        const k = key(x, y);
        if (!index.has(k)) {
            index.set(k, pts.length);
            pts.push([x, y]);
        }
        return index.get(k);
    };

    // Reserve ids for start (0) and target (1)
    index.set(key(start[0], start[1]), 0);
    index.set(key(target[0], target[1]), 1);

    const special = []; // [fromId, toId, cost]
    for (const [x1, y1, x2, y2, c] of specialRoads) {
        special.push([getId(x1, y1), getId(x2, y2), c]);
    }

    const V = pts.length;
    const out = Array.from({ length: V }, () => []);
    for (const [a, b, c] of special) out[a].push([b, c]);

    const dist = new Array(V).fill(Infinity);
    const done = new Array(V).fill(false);
    dist[0] = 0;

    for (let iter = 0; iter < V; iter++) {
        let u = -1;
        for (let i = 0; i < V; i++) {
            if (!done[i] && (u === -1 || dist[i] < dist[u])) u = i;
        }
        if (u === -1 || dist[u] === Infinity) break;
        done[u] = true;

        const [ux, uy] = pts[u];
        // Free movement to every other point
        for (let v = 0; v < V; v++) {
            if (done[v]) continue;
            const d = dist[u] + Math.abs(pts[v][0] - ux) + Math.abs(pts[v][1] - uy);
            if (d < dist[v]) dist[v] = d;
        }
        // Special roads leaving u
        for (const [v, c] of out[u]) {
            if (!done[v] && dist[u] + c < dist[v]) dist[v] = dist[u] + c;
        }
    }

    return dist[1];
};
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [3650. Minimum Cost Path with Edge Reversals](../../3501-4000/3650-minimum-cost-path-with-edge-reversals/)
- [4003. Minimum Cost Path with Alternating Directions III](../../4001-4500/4003-minimum-cost-path-with-alternating-directions-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/)
