# LeetCode 3530: Maximum Profit from Valid Topological Order in DAG

**LeetCode Problem #3530 — Maximum Profit from Valid Topological Order in DAG**
Solve LeetCode Maximum Profit from Valid Topological Order in DAG using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Profit from Valid Topological Order in DAG |
| LeetCode | #3530 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **Directed Acyclic Graph (DAG)** with `n` nodes labeled from `0` to `n - 1`, represented by a 2D array `edges`, where `edges[i] = [u_i, v_i]` indicates a directed edge from node `u_i` to `v_i`. Each node has an associated **score** given in an array `score`, where `score[i]` represents the score of node `i`.

You must process the nodes in a **valid topological order**. Each node is assigned a **1-based position** in the processing order.

The **profit** is calculated by summing up the product of each node's score and its position in the ordering.

Return the **maximum **possible profit achievable with an optimal topological order.

A **topological order** of a DAG is a linear ordering of its nodes such that for every directed edge `u &rarr; v`, node `u` comes before `v` in the ordering.

## Constraints
- `1 <= n == score.length <= 22`
- `1 <= score[i] <= 10^5`
- `0 <= edges.length <= n * (n - 1) / 2`
- `edges[i] == [u_i, v_i]` denotes a directed edge from `u_i` to `v_i`.
- `0 <= u_i, v_i < n`
- `u_i != v_i`
- The input graph is **guaranteed** to be a **DAG**.
- There are no duplicate edges.

## Examples
### Example 1
- **Input:** `n = 2, edges = [[0,1]], score = [2,3]`
- **Output:** `8`
- **Explanation:** Node 1 depends on node 0, so a valid order is `[0, 1]`. 

 
 
 
 Node 
 Processing Order 
 Score 
 Multiplier 
 Profit Calculation 
 
 
 
 
 0 
 1st 
 2 
 1 
 2 &times; 1 = 2 
 
 
 1 
 2nd 
 3 
 2 
 3 &times; 2 = 6 
 
 
 

 The maximum total profit achievable over all valid topological orders is `2 + 6 = 8`.

### Example 2
- **Input:** `n = 3, edges = [[0,1],[0,2]], score = [1,6,3]`
- **Output:** `25`
- **Explanation:** Nodes 1 and 2 depend on node 0, so the most optimal valid order is `[0, 2, 1]`. 

 
 
 
 Node 
 Processing Order 
 Score 
 Multiplier 
 Profit Calculation 
 
 
 
 
 0 
 1st 
 1 
 1 
 1 &times; 1 = 1 
 
 
 2 
 2nd 
 3 
 2 
 3 &times; 2 = 6 
 
 
 1 
 3rd 
 6 
 3 
 6 &times; 3 = 18 
 
 
 

 The maximum total profit achievable over all valid topological orders is `1 + 6 + 18 = 25`.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Profit from Valid Topological Order in DAG**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, edges = [[0,1]], score = [2,3]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** Node 1 depends on node 0, so a valid order is `[0, 1]`. 

 
 
 
 Node 
 Processing Order 
 Score 
 Multiplier 
 Profit Calculation 
 
 
 
 
 0 
 1st 
 2 
 1 
 2 &times; 1 = 2 
 
 
 1 
 2nd 
 3 
 2 
 3 &times; 2 = 6 
 
 
 

 The maximum total profit achievable over all valid topological orders is `2 + 6 = 8`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} score
 * @return {number}
 */
var maxProfit = function (n, edges, score) {
    const pre = new Int32Array(n);
    for (const [u, v] of edges) pre[v] |= 1 << u;

    const size = 1 << n;
    const dp = new Int32Array(size).fill(-1);
    const pc = new Uint8Array(size);
    for (let m = 1; m < size; m++) pc[m] = pc[m >> 1] + (m & 1);

    dp[0] = 0;
    for (let mask = 0; mask < size; mask++) {
        if (dp[mask] < 0) continue;
        const pos = pc[mask] + 1;
        for (let v = 0; v < n; v++) {
            if ((mask >> v) & 1) continue;
            if ((pre[v] & mask) !== pre[v]) continue;
            const nm = mask | (1 << v);
            const val = dp[mask] + score[v] * pos;
            if (val > dp[nm]) dp[nm] = val;
        }
    }
    return dp[size - 1];
};
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1298-maximum-candies-you-can-get-from-boxes/)
- [1423. Maximum Points You Can Obtain from Cards](../../1001-1500/1423-maximum-points-you-can-obtain-from-cards/)
- [1707. Maximum XOR With an Element From Array](../../1501-2000/1707-maximum-xor-with-an-element-from-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/)
