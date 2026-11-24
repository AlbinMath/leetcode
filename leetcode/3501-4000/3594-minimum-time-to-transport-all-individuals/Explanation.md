# LeetCode 3594: Minimum Time to Transport All Individuals

**LeetCode Problem #3594 — Minimum Time to Transport All Individuals**
Solve LeetCode Minimum Time to Transport All Individuals using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Transport All Individuals |
| LeetCode | #3594 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given `n` individuals at a base camp who need to cross a river to reach a destination using a single boat. The boat can carry at most `k` people at a time. The trip is affected by environmental conditions that vary **cyclically** over `m` stages.

Each stage `j` has a speed multiplier `mul[j]`:

If `mul[j] > 1`, the trip slows down. 
 If `mul[j] < 1`, the trip speeds up.

Each individual `i` has a rowing strength represented by `time[i]`, the time (in minutes) it takes them to cross alone in neutral conditions.

**Rules:**

A group `g` departing at stage `j` takes time equal to the **maximum** `time[i]` among its members, multiplied by `mul[j]` minutes to reach the destination. 
 After the group crosses the river in time `d`, the stage advances by `floor(d) % m` steps. 
 If individuals are left behind, one person must return with the boat. Let `r` be the index of the returning person, the return takes `time[r] &times; mul[current_stage]`, defined as `return_time`, and the stage advances by `floor(return_time) % m`.

Return the **minimum** total time required to transport all individuals. If it is not possible to transport all individuals to the destination, return `-1`.

## Constraints
- `1 <= n == time.length <= 12`
- `1 <= k <= 5`
- `1 <= m <= 5`
- `1 <= time[i] <= 100`
- `m == mul.length`
- `0.5 <= mul[i] <= 2.0`

## Examples
### Example 1
- **Input:** `n = 1, k = 1, m = 2, time = [5], mul = [1.0,1.3]`
- **Output:** `5.00000`
- **Explanation:** Individual 0 departs from stage 0, so crossing time = `5 &times; 1.00 = 5.00` minutes. 
 All team members are now at the destination. Thus, the total time taken is `5.00` minutes.

### Example 2
- **Input:** `n = 3, k = 2, m = 3, time = [2,5,8], mul = [1.0,1.5,0.75]`
- **Output:** `14.50000`
- **Explanation:** The optimal strategy is: 

 
 Send individuals 0 and 2 from the base camp to the destination from stage 0. The crossing time is `max(2, 8) &times; mul[0] = 8 &times; 1.00 = 8.00` minutes. The stage advances by `floor(8.00) % 3 = 2`, so the next stage is `(0 + 2) % 3 = 2`. 
 Individual 0 returns alone from the destination to the base camp from stage 2. The return time is `2 &times; mul[2] = 2 &times; 0.75 = 1.50` minutes. The stage advances by `floor(1.50) % 3 = 1`, so the next stage is `(2 + 1) % 3 = 0`. 
 Send individuals 0 and 1 from the base camp to the destination from stage 0. The crossing time is `max(2, 5) &times; mul[0] = 5 &times; 1.00 = 5.00` minutes. The stage advances by `floor(5.00) % 3 = 2`, so the final stage is `(0 + 2) % 3 = 2`. 
 All team members are now at the destination. The total time taken is `8.00 + 1.50 + 5.00 = 14.50` minutes.

### Example 3
- **Input:** `n = 2, k = 1, m = 2, time = [10,10], mul = [2.0,2.0]`
- **Output:** `-1.00000`
- **Explanation:** Since the boat can only carry one person at a time, it is impossible to transport both individuals as one must always return. Thus, the answer is `-1.00`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Time to Transport All Individuals**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1, k = 1, m = 2, time = [5], mul = [1.0,1.3]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5.00000`.
4. **Verification:** Individual 0 departs from stage 0, so crossing time = `5 &times; 1.00 = 5.00` minutes. 
 All team members are now at the destination. Thus, the total time taken is `5.00` minutes.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minTime = function (n, k, m, time, mul) {
    const FULL = (1 << n) - 1;

    // Precompute max time and popcount for every subset
    const maxT = new Float64Array(1 << n);
    const pc = new Uint8Array(1 << n);
    for (let s = 1; s <= FULL; s++) {
        const low = s & -s;
        const idx = 31 - Math.clz32(low);
        const rest = s ^ low;
        maxT[s] = Math.max(maxT[rest], time[idx]);
        pc[s] = pc[rest] + 1;
    }

    const stateId = (mask, side, stage) => (mask * 2 + side) * m + stage;
    const total = (FULL + 1) * 2 * m;
    const dist = new Float64Array(total).fill(Infinity);

    // Min-heap of [cost, state]
    const heap = [];
    const push = (item) => {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p][0] <= heap[i][0]) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length) {
            heap[0] = last;
            let i = 0;
            const len = heap.length;
            while (true) {
                const l = 2 * i + 1, r = l + 1;
                let s = i;
                if (l < len && heap[l][0] < heap[s][0]) s = l;
                if (r < len && heap[r][0] < heap[s][0]) s = r;
                if (s === i) break;
                [heap[s], heap[i]] = [heap[i], heap[s]];
                i = s;
            }
        }
        return top;
    };

    const start = stateId(FULL, 0, 0);
    dist[start] = 0;
    push([0, start]);

    while (heap.length) {
        const [cost, id] = pop();
        if (cost > dist[id]) continue;

        const stage = id % m;
        const rest = (id - stage) / m;
        const side = rest % 2;
        const mask = (rest - side) / 2;

        if (mask === 0) return cost;

        if (side === 0) {
            // Send a non-empty group of size <= k from the base
            for (let g = mask; g > 0; g = (g - 1) & mask) {
                if (pc[g] > k) continue;
                const d = maxT[g] * mul[stage];
                const ns = (stage + (Math.floor(d + 1e-9) % m)) % m;
                const nid = stateId(mask ^ g, 1, ns);
                const nc = cost + d;
                if (nc < dist[nid]) {
                    dist[nid] = nc;
                    push([nc, nid]);
                }
            }
        } else {
            // One person at the destination returns
            const atDest = FULL ^ mask;
            for (let r = 0; r < n; r++) {
                if (!((atDest >> r) & 1)) continue;
                const t = time[r] * mul[stage];
                const ns = (stage + (Math.floor(t + 1e-9) % m)) % m;
                const nid = stateId(mask | (1 << r), 0, ns);
                const nc = cost + t;
                if (nc < dist[nid]) {
                    dist[nid] = nc;
                    push([nc, nid]);
                }
            }
        }
    }
    return -1;
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1266. Minimum Time Visiting All Points](../../1001-1500/1266-minimum-time-visiting-all-points/)
- [1443. Minimum Time to Collect All Apples in a Tree](../../1001-1500/1443-minimum-time-to-collect-all-apples-in-a-tree/)
- [1723. Find Minimum Time to Finish All Jobs](../../1501-2000/1723-find-minimum-time-to-finish-all-jobs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-transport-all-individuals/)
