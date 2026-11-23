# LeetCode 3543: Maximum Weighted K-Edge Path

**LeetCode Problem #3543 — Maximum Weighted K-Edge Path**
Solve LeetCode Maximum Weighted K-Edge Path using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Weighted K-Edge Path |
| LeetCode | #3543 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n` and a **Directed Acyclic Graph (DAG)** with `n` nodes labeled from 0 to `n - 1`. This is represented by a 2D array `edges`, where `edges[i] = [u_i, v_i, w_i]` indicates a directed edge from node `u_i` to `v_i` with weight `w_i`.

You are also given two integers, `k` and `t`.

Your task is to determine the **maximum** possible sum of edge weights for any path in the graph such that:

The path contains **exactly** `k` edges. 
 The total sum of edge weights in the path is **strictly** less than `t`.

Return the **maximum** possible sum of weights for such a path. If no such path exists, return `-1`.

## Constraints
- `1 <= n <= 300`
- `0 <= edges.length <= 300`
- `edges[i] = [u_i, v_i, w_i]`
- `0 <= u_i, v_i < n`
- `u_i != v_i`
- `1 <= w_i <= 10`
- `0 <= k <= 300`
- `1 <= t <= 600`
- The input graph is **guaranteed** to be a **DAG**.
- There are no duplicate edges.

## Examples
### Example 1
- **Input:** `n = 3, edges = [[0,1,1],[1,2,2]], k = 2, t = 4`
- **Output:** `3`
- **Explanation:** The only path with `k = 2` edges is `0 -> 1 -> 2` with weight `1 + 2 = 3 < t`. 
 Thus, the maximum possible sum of weights less than `t` is 3.

### Example 2
- **Input:** `n = 3, edges = [[0,1,2],[0,2,3]], k = 1, t = 3`
- **Output:** `2`
- **Explanation:** There are two paths with `k = 1` edge:

 
 `0 -> 1` with weight `2 < t`. 
 `0 -> 2` with weight `3 = t`, which is not strictly less than `t`. 
 
 
 Thus, the maximum possible sum of weights less than `t` is 2.

### Example 3
- **Input:** `n = 3, edges = [[0,1,6],[1,2,8]], k = 1, t = 6`
- **Output:** `-1`
- **Explanation:** There are two paths with k = 1 edge:
 
 `0 -> 1` with weight `6 = t`, which is not strictly less than `t`. 
 `1 -> 2` with weight `8 > t`, which is not strictly less than `t`. 
 
 
 Since there is no path with sum of weights strictly less than `t`, the answer is -1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Weighted K-Edge Path**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, edges = [[0,1,1],[1,2,2]], k = 2, t = 4`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The only path with `k = 2` edges is `0 -> 1 -> 2` with weight `1 + 2 = 3 < t`. 
 Thus, the maximum possible sum of weights less than `t` is 3.

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
var maxWeight = function(n, edges, k, t) {
    if (k === 0) return 0;

    // dp[i]: bit s is 1 if a path ending at node i
    // can have total weight s using the current number of edges.
    let dp = new Array(n).fill(1n);

    // Keep only sums strictly less than t.
    const mask = (1n << BigInt(t)) - 1n;

    for (let step = 1; step <= k; step++) {
        const next = new Array(n).fill(0n);

        for (const [u, v, w] of edges) {
            // Shift all reachable sums by edge weight w.
            next[v] |= (dp[u] << BigInt(w)) & mask;
        }

        dp = next;
    }

    // Find the largest reachable sum.
    let answer = -1;

    for (let i = 0; i < n; i++) {
        if (dp[i] === 0n) continue;

        for (let sum = t - 1; sum >= 0; sum--) {
            if ((dp[i] & (1n << BigInt(sum))) !== 0n) {
                answer = Math.max(answer, sum);
                break;
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
- [3515. Shortest Path in a Weighted Tree](../../3501-4000/3829-shortest-path-in-a-weighted-tree/)
- [1191. K-Concatenation Maximum Sum](../../1001-1500/1299-k-concatenation-maximum-sum/)
- [2106. Maximum Fruits Harvested After at Most K Steps](../../2001-2500/2229-maximum-fruits-harvested-after-at-most-k-steps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-weighted-k-edge-path/)
