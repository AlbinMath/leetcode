# LeetCode 3426: Manhattan Distances of All Arrangements of Pieces

**LeetCode Problem #3426 — Manhattan Distances of All Arrangements of Pieces**
Solve LeetCode Manhattan Distances of All Arrangements of Pieces using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Manhattan Distances of All Arrangements of Pieces |
| LeetCode | #3426 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given three integers ` m `, ` n `, and `k`.

There is a rectangular grid of size `m &times; n` containing `k` identical pieces. Return the sum of Manhattan distances between every pair of pieces over all **valid arrangements** of pieces.

A **valid arrangement** is a placement of all `k` pieces on the grid with **at most** one piece per cell.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

The Manhattan Distance between two cells `(x_i, y_i)` and `(x_j, y_j)` is `|x_i - x_j| + |y_i - y_j|`.

## Constraints
- `1 <= m, n <= 10^5`
- `2 <= m * n <= 10^5`
- ` 2 <= k <= m * n `

## Examples
### Example 1
- **Input:** `m = 2, n = 2, k = 2`
- **Output:** `8`
- **Explanation:** The valid arrangements of pieces on the board are: 

 

 
 In the first 4 arrangements, the Manhattan distance between the two pieces is 1. 
 In the last 2 arrangements, the Manhattan distance between the two pieces is 2. 
 

 Thus, the total Manhattan distance across all valid arrangements is `1 + 1 + 1 + 1 + 2 + 2 = 8`.

### Example 2
- **Input:** `m = 1, n = 4, k = 3`
- **Output:** `20`
- **Explanation:** The valid arrangements of pieces on the board are: 

 

 
 The first and last arrangements have a total Manhattan distance of `1 + 1 + 2 = 4`. 
 The middle two arrangements have a total Manhattan distance of `1 + 2 + 3 = 6`. 
 

 The total Manhattan distance between all pairs of pieces across all arrangements is `4 + 6 + 6 + 4 = 20`.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Manhattan Distances of All Arrangements of Pieces**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `m = 2, n = 2, k = 2`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** The valid arrangements of pieces on the board are: 

 

 
 In the first 4 arrangements, the Manhattan distance between the two pieces is 1. 
 In the last 2 arrangements, the Manhattan distance between the two pieces is 2. 
 

 Thus, the total Manhattan distance across all valid arrangements is `1 + 1 + 1 + 1 + 2 + 2 = 8`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var distanceSum = function (m, n, k) {
    const MOD = 1000000007n;
    const N = m * n;

    const power = (base, exp) => {
        let result = 1n;
        base %= MOD;
        while (exp > 0n) {
            if (exp & 1n) result = (result * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1n;
        }
        return result;
    };

    // Factorials up to N - 2
    const top = N - 2;
    const fact = new Array(top + 1).fill(1n);
    for (let i = 1; i <= top; i++) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }

    // C(N-2, k-2)
    const a = top, b = k - 2;
    const comb =
        (fact[a] *
            power(fact[b], MOD - 2n) % MOD *
            power(fact[a - b], MOD - 2n)) %
        MOD;

    // Sum over d of d * (len - d)
    const lineSum = (len) => {
        let s = 0n;
        for (let d = 1; d < len; d++) {
            s += BigInt(d) * BigInt(len - d);
        }
        return s % MOD;
    };

    const M = BigInt(m), Nn = BigInt(n);
    const pairSum =
        (Nn * Nn % MOD * lineSum(m) + M * M % MOD * lineSum(n)) % MOD;

    return Number(comb * pairSum % MOD);
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3102. Minimize Manhattan Distances](../../3001-3500/3344-minimize-manhattan-distances/)
- [1175. Prime Arrangements](../../1001-1500/1279-prime-arrangements/)
- [2038. Remove Colored Pieces if Both Neighbors are the Same Color](../../2001-2500/2149-remove-colored-pieces-if-both-neighbors-are-the-same-color/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/)
