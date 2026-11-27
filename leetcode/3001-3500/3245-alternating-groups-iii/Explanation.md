# LeetCode 3245: Alternating Groups III

**LeetCode Problem #3245 — Alternating Groups III**
Solve LeetCode Alternating Groups III using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Alternating Groups III |
| LeetCode | #3245 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are some red and blue tiles arranged circularly. You are given an array of integers `colors` and a 2D integers array `queries`.

The color of tile `i` is represented by `colors[i]`:

`colors[i] == 0` means that tile `i` is **red**. 
 `colors[i] == 1` means that tile `i` is **blue**.

An **alternating** group is a contiguous subset of tiles in the circle with **alternating** colors (each tile in the group except the first and last one has a different color from its adjacent tiles in the group).

You have to process queries of two types:

`queries[i] = [1, size_i]`, determine the count of **alternating** groups with size `size_i`. 
 `queries[i] = [2, index_i, color_i]`, change `colors[index_i]` to `color _i `.

Return an array `answer` containing the results of the queries of the first type *in order*.

**Note** that since `colors` represents a **circle**, the **first** and the **last** tiles are considered to be next to each other.

## Constraints
- `4 <= colors.length <= 5 * 10^4`
- `0 <= colors[i] <= 1`
- `1 <= queries.length <= 5 * 10^4`
- `queries[i][0] == 1` or `queries[i][0] == 2`
- For all `i` that:
 
 `queries[i][0] == 1`: `queries[i].length == 2`, `3 <= queries[i][1] <= colors.length - 1`
- `queries[i][0] == 2`: `queries[i].length == 3`, `0 <= queries[i][1] <= colors.length - 1`, `0 <= queries[i][2] <= 1`

## Examples
### Example 1
- **Input:** `colors = [0,1,1,0,1], queries = [[2,1,0],[1,4]]`
- **Output:** `[2]`

### Example 2
- **Input:** `colors = [0,0,1,0,1,1], queries = [[1,3],[2,3,0],[1,5]]`
- **Output:** `[2,0]`
- **Explanation:** First query: 

 Count of the alternating groups with size 3: 

 

 Second query: `colors` will not change. 

 Third query: There is no alternating group with size 5.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Alternating Groups III**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `colors = [0,1,1,0,1], queries = [[2,1,0],[1,4]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2]`.

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
var numberOfAlternatingGroups = function(colors, queries) {
    const n = colors.length;

    // Fenwick tree for the positions of equal-adjacent edges.
    const posBIT = new Array(n + 1).fill(0);

    // Fenwick trees for gap lengths and weighted gap lengths.
    const countBIT = new Array(n + 1).fill(0);
    const sumBIT = new Array(n + 1).fill(0);

    const isBreak = new Array(n).fill(false);
    let breakCount = 0;

    function posAdd(index, delta) {
        for (let i = index + 1; i <= n; i += i & -i) {
            posBIT[i] += delta;
        }
    }

    // Count break positions in [0, end).
    function posPrefix(end) {
        let result = 0;

        for (let i = end; i > 0; i -= i & -i) {
            result += posBIT[i];
        }

        return result;
    }

    // Return the zero-based position of the kth break (1-indexed k).
    function kth(k) {
        let index = 0;
        let step = 1;

        while (step * 2 <= n) step *= 2;

        for (; step > 0; step = Math.floor(step / 2)) {
            const next = index + step;

            if (next <= n && posBIT[next] < k) {
                index = next;
                k -= posBIT[next];
            }
        }

        return index;
    }

    function gapLength(a, b) {
        const d = (b - a + n) % n;
        return d === 0 ? n : d;
    }

    function gapAdd(length, delta) {
        for (let i = length; i <= n; i += i & -i) {
            countBIT[i] += delta;
            sumBIT[i] += length * delta;
        }
    }

    function gapPrefix(bit, index) {
        let result = 0;

        for (let i = index; i > 0; i -= i & -i) {
            result += bit[i];
        }

        return result;
    }

    function addBreak(x) {
        if (isBreak[x]) return;

        if (breakCount === 0) {
            gapAdd(n, 1);
        } else {
            const less = posPrefix(x);
            const p = less === 0 ? kth(breakCount) : kth(less);

            const le = posPrefix(x + 1);
            const s = le === breakCount ? kth(1) : kth(le + 1);

            gapAdd(gapLength(p, s), -1);
            gapAdd(gapLength(p, x), 1);
            gapAdd(gapLength(x, s), 1);
        }

        posAdd(x, 1);
        isBreak[x] = true;
        breakCount++;
    }

    function removeBreak(x) {
        if (!isBreak[x]) return;

        if (breakCount === 1) {
            gapAdd(n, -1);
        } else {
            const less = posPrefix(x);
            const p = less === 0 ? kth(breakCount) : kth(less);

            const s = less + 2 > breakCount
                ? kth(1)
                : kth(less + 2);

            gapAdd(gapLength(p, x), -1);
            gapAdd(gapLength(x, s), -1);
            gapAdd(gapLength(p, s), 1);
        }

        posAdd(x, -1);
        isBreak[x] = false;
        breakCount--;
    }

    // Initialize equal-adjacent edges, including the circular edge.
    for (let i = 0; i < n; i++) {
        if (colors[i] === colors[(i + 1) % n]) {
            addBreak(i);
        }
    }

    const answer = [];

    for (const query of queries) {
        if (query[0] === 1) {
            const k = query[1];

            if (breakCount === 0) {
                answer.push(n);
                continue;
            }

            const smallCount = gapPrefix(countBIT, k - 1);
            const smallSum = gapPrefix(sumBIT, k - 1);

            const totalCount = gapPrefix(countBIT, n);
            const totalSum = gapPrefix(sumBIT, n);

            const count = totalCount - smallCount;
            const sum = totalSum - smallSum;

            answer.push(sum - (k - 1) * count);
        } else {
            const index = query[1];
            const color = query[2];

            if (colors[index] === color) continue;

            const leftEdge = (index - 1 + n) % n;
            const rightEdge = index;

            removeBreak(leftEdge);
            removeBreak(rightEdge);

            colors[index] = color;

            if (colors[leftEdge] === colors[index]) {
                addBreak(leftEdge);
            }

            if (colors[index] === colors[(index + 1) % n]) {
                addBreak(rightEdge);
            }
        }
    }

    return answer;
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
- [3206. Alternating Groups I](../../3001-3500/3206-alternating-groups-i/)
- [3208. Alternating Groups II](../../3001-3500/3208-alternating-groups-ii/)
- [693. Binary Number with Alternating Bits](../../0501-1000/0693-binary-number-with-alternating-bits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/alternating-groups-iii/)
