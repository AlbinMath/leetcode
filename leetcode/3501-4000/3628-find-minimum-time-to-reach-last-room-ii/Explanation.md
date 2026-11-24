# LeetCode 3342: Find Minimum Time to Reach Last Room II

**LeetCode Problem #3342 — Find Minimum Time to Reach Last Room II**
Solve LeetCode Find Minimum Time to Reach Last Room II using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Minimum Time to Reach Last Room II |
| LeetCode | #3342 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a dungeon with `n x m` rooms arranged as a grid.

You are given a 2D array `moveTime` of size `n x m`, where `moveTime[i][j]` represents the **minimum** time in seconds when you can **start moving** to that room. You start from the room `(0, 0)` at time `t = 0` and can move to an **adjacent** room. Moving between **adjacent** rooms takes one second for one move and two seconds for the next, **alternating** between the two.

Return the **minimum** time to reach the room `(n - 1, m - 1)`.

Two rooms are **adjacent** if they share a common wall, either *horizontally* or *vertically*.

## Constraints
- `2 <= n == moveTime.length <= 750`
- `2 <= m == moveTime[i].length <= 750`
- `0 <= moveTime[i][j] <= 10^9`

## Examples
### Example 1
- **Input:** `moveTime = [[0,4],[4,4]]`
- **Output:** `7`
- **Explanation:** The minimum time required is 7 seconds. 

 
 At time `t == 4`, move from room `(0, 0)` to room `(1, 0)` in one second. 
 At time `t == 5`, move from room `(1, 0)` to room `(1, 1)` in two seconds.

### Example 2
- **Input:** `moveTime = [[0,0,0,0],[0,0,0,0]]`
- **Output:** `6`
- **Explanation:** The minimum time required is 6 seconds. 

 
 At time `t == 0`, move from room `(0, 0)` to room `(1, 0)` in one second. 
 At time `t == 1`, move from room `(1, 0)` to room `(1, 1)` in two seconds. 
 At time `t == 3`, move from room `(1, 1)` to room `(1, 2)` in one second. 
 At time `t == 4`, move from room `(1, 2)` to room `(1, 3)` in two seconds.

### Example 3
- **Input:** `moveTime = [[0,1],[1,2]]`
- **Output:** `4`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Minimum Time to Reach Last Room II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `moveTime = [[0,4],[4,4]]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** The minimum time required is 7 seconds. 

 
 At time `t == 4`, move from room `(0, 0)` to room `(1, 0)` in one second. 
 At time `t == 5`, move from room `(1, 0)` to room `(1, 1)` in two seconds.

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
    const SHIFT = 1048576; // 2^20 > 562500
    const dist = new Float64Array(V).fill(Infinity);
    dist[0] = 0;

    // Min-heap of encoded keys: time * SHIFT + index
    const heap = new Float64Array(4 * V + 4);
    let size = 0;
    const push = (key) => {
        let i = size++;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p] <= key) break;
            heap[i] = heap[p];
            i = p;
        }
        heap[i] = key;
    };
    const pop = () => {
        const top = heap[0];
        const last = heap[--size];
        let i = 0;
        while (true) {
            let l = 2 * i + 1;
            if (l >= size) break;
            if (l + 1 < size && heap[l + 1] < heap[l]) l++;
            if (heap[l] >= last) break;
            heap[i] = heap[l];
            i = l;
        }
        heap[i] = last;
        return top;
    };

    const dr = [1, -1, 0, 0], dc = [0, 0, 1, -1];
    push(0);

    while (size > 0) {
        const key = pop();
        const u = key % SHIFT;
        const t = (key - u) / SHIFT;
        if (t > dist[u]) continue;
        if (u === V - 1) return t;

        const r = (u / m) | 0, c = u % m;
        const cost = ((r + c) & 1) === 0 ? 1 : 2;
        for (let d = 0; d < 4; d++) {
            const nr = r + dr[d], nc = c + dc[d];
            if (nr < 0 || nc < 0 || nr >= n || nc >= m) continue;
            const nt = Math.max(t, moveTime[nr][nc]) + cost;
            const ni = nr * m + nc;
            if (nt < dist[ni]) {
                dist[ni] = nt;
                push(nt * SHIFT + ni);
            }
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
- [3341. Find Minimum Time to Reach Last Room I](../../3501-4000/3627-find-minimum-time-to-reach-last-room-i/)
- [1928. Minimum Cost to Reach Destination in Time](../../2001-2500/2040-minimum-cost-to-reach-destination-in-time/)
- [2045. Second Minimum Time to Reach Destination](../../2001-2500/2171-second-minimum-time-to-reach-destination/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/)
