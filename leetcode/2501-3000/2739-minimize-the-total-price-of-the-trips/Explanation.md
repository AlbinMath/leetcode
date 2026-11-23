# LeetCode 2646: Minimize the Total Price of the Trips

**LeetCode Problem #2646 — Minimize the Total Price of the Trips**
Solve LeetCode Minimize the Total Price of the Trips using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimize the Total Price of the Trips |
| LeetCode | #2646 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There exists an undirected and unrooted tree with `n` nodes indexed from `0` to `n - 1`. You are given the integer `n` and a 2D integer array `edges` of length `n - 1`, where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree.

Each node has an associated price. You are given an integer array `price`, where `price[i]` is the price of the `i^th` node.

The **price sum** of a given path is the sum of the prices of all nodes lying on that path.

Additionally, you are given a 2D integer array `trips`, where `trips[i] = [start_i, end_i]` indicates that you start the `i^th` trip from the node `start_i` and travel to the node `end_i` by any path you like.

Before performing your first trip, you can choose some **non-adjacent** nodes and halve the prices.

Return *the minimum total price sum to perform all the given trips*.

## Constraints
- `1 <= n <= 50`
- `edges.length == n - 1`
- `0 <= a_i, b_i <= n - 1`
- `edges` represents a valid tree.
- `price.length == n`
- `price[i]` is an even integer.
- `1 <= price[i] <= 1000`
- `1 <= trips.length <= 100`
- `0 <= start_i, end_i <= n - 1`

## Examples
### Example 1
- **Input:** `n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]`
- **Output:** `23`
- **Explanation:** The diagram above denotes the tree after rooting it at node 2. The first part shows the initial tree and the second part shows the tree after choosing nodes 0, 2, and 3, and making their price half.
For the 1^st trip, we choose path [0,1,3]. The price sum of that path is 1 + 2 + 3 = 6.
For the 2^nd trip, we choose path [2,1]. The price sum of that path is 2 + 5 = 7.
For the 3^rd trip, we choose path [2,1,3]. The price sum of that path is 5 + 2 + 3 = 10.
The total price sum of all trips is 6 + 7 + 10 = 23.
It can be proven, that 23 is the minimum answer that we can achieve.

### Example 2
- **Input:** `n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]`
- **Output:** `1`
- **Explanation:** The diagram above denotes the tree after rooting it at node 0. The first part shows the initial tree and the second part shows the tree after choosing node 0, and making its price half.
For the 1^st trip, we choose path [0]. The price sum of that path is 1.
The total price sum of all trips is 1. It can be proven, that 1 is the minimum answer that we can achieve.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimize the Total Price of the Trips**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `23`.
4. **Verification:** The diagram above denotes the tree after rooting it at node 2. The first part shows the initial tree and the second part shows the tree after choosing nodes 0, 2, and 3, and making their price half.
For the 1^st trip, we choose path [0,1,3]. The price sum of that path is 1 + 2 + 3 = 6.
For the 2^nd trip, we choose path [2,1]. The price sum of that path is 2 + 5 = 7.
For the 3^rd trip, we choose path [2,1,3]. The price sum of that path is 5 + 2 + 3 = 10.
The total price sum of all trips is 6 + 7 + 10 = 23.
It can be proven, that 23 is the minimum answer that we can achieve.

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
var minimumTotalPrice = function(n, edges, price, trips) {
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    // Step 1: Count visits to every node.
    const count = new Array(n).fill(0);

    function findPath(u, parent, target) {
        if (u === target) {
            count[u]++;
            return true;
        }

        for (const v of graph[u]) {
            if (v === parent) continue;

            if (findPath(v, u, target)) {
                count[u]++;
                return true;
            }
        }

        return false;
    }

    for (const [start, end] of trips) {
        findPath(start, -1, end);
    }

    // Step 2: Tree DP.
    // dp[u][0] = minimum cost when u is not halved.
    // dp[u][1] = minimum cost when u is halved.

    function dfs(u, parent) {
        let full = count[u] * price[u];
        let half = count[u] * (price[u] / 2);

        for (const v of graph[u]) {
            if (v === parent) continue;

            const [childFull, childHalf] = dfs(v, u);

            // If u is not halved, child can be either.
            full += Math.min(childFull, childHalf);

            // If u is halved, child cannot be halved.
            half += childFull;
        }

        return [full, half];
    }

    const [full, half] = dfs(0, -1);

    return Math.min(full, half);
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
- [1164. Product Price at a Given Date](../../1001-1500/1278-product-price-at-a-given-date/)
- [1251. Average Selling Price](../../1001-1500/1390-average-selling-price/)
- [2034. Stock Price Fluctuation ](../../2001-2500/2161-stock-price-fluctuation-/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimize-the-total-price-of-the-trips/)
