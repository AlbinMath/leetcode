# LeetCode 3341: Find Minimum Time to Reach Last Room I

**LeetCode Problem #3341 — Find Minimum Time to Reach Last Room I**
Solve LeetCode Find Minimum Time to Reach Last Room I using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Minimum Time to Reach Last Room I |
| LeetCode | #3341 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a dungeon with `n x m` rooms arranged as a grid.

You are given a 2D array `moveTime` of size `n x m`, where `moveTime[i][j]` represents the **minimum** time in seconds **after** which the room opens and can be moved to. You start from the room `(0, 0)` at time `t = 0` and can move to an **adjacent** room. Moving between adjacent rooms takes *exactly* one second.

Return the **minimum** time to reach the room `(n - 1, m - 1)`.

Two rooms are **adjacent** if they share a common wall, either *horizontally* or *vertically*.

## Constraints
- `2 <= n == moveTime.length <= 50`
- `2 <= m == moveTime[i].length <= 50`
- `0 <= moveTime[i][j] <= 10^9`

## Examples
### Example 1
- **Input:** `moveTime = [[0,4],[4,4]]`
- **Output:** `6`
- **Explanation:** The minimum time required is 6 seconds. 

 
 At time `t == 4`, move from room `(0, 0)` to room `(1, 0)` in one second. 
 At time `t == 5`, move from room `(1, 0)` to room `(1, 1)` in one second.

### Example 2
- **Input:** `moveTime = [[0,0,0],[0,0,0]]`
- **Output:** `3`
- **Explanation:** The minimum time required is 3 seconds. 

 
 At time `t == 0`, move from room `(0, 0)` to room `(1, 0)` in one second. 
 At time `t == 1`, move from room `(1, 0)` to room `(1, 1)` in one second. 
 At time `t == 2`, move from room `(1, 1)` to room `(1, 2)` in one second.

### Example 3
- **Input:** `moveTime = [[0,1],[1,2]]`
- **Output:** `3`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Minimum Time to Reach Last Room I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `moveTime = [[0,4],[4,4]]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The minimum time required is 6 seconds. 

 
 At time `t == 4`, move from room `(0, 0)` to room `(1, 0)` in one second. 
 At time `t == 5`, move from room `(1, 0)` to room `(1, 1)` in one second.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minTimeToReach = function (moveTime) {
    const n = moveTime.length, m = moveTime[0].length;
    const V = n * m;
    const dist = new Array(V).fill(Infinity);
    const done = new Array(V).fill(false);
    dist[0] = 0;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    for (let iter = 0; iter < V; iter++) {
        let u = -1;
        for (let i = 0; i < V; i++) {
            if (!done[i] && (u === -1 || dist[i] < dist[u])) u = i;
        }
        if (u === -1 || dist[u] === Infinity) break;
        if (u === V - 1) return dist[u];
        done[u] = true;

        const r = (u / m) | 0, c = u % m;
        for (const [dr, dc] of dirs) {
            const nr = r + dr, nc = c + dc;
            if (nr < 0 || nc < 0 || nr >= n || nc >= m) continue;
            const ni = nr * m + nc;
            if (done[ni]) continue;
            const nt = Math.max(dist[u], moveTime[nr][nc]) + 1;
            if (nt < dist[ni]) dist[ni] = nt;
        }
    }
    return dist[V - 1];
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3342. Find Minimum Time to Reach Last Room II](../../3001-3500/3342-find-minimum-time-to-reach-last-room-ii/)
- [1723. Find Minimum Time to Finish All Jobs](../../1501-2000/1723-find-minimum-time-to-finish-all-jobs/)
- [3494. Find the Minimum Amount of Time to Brew Potions](../../3001-3500/3494-find-the-minimum-amount-of-time-to-brew-potions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/)
