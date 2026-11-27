# LeetCode 4002: Count Valid Sequences

**LeetCode Problem #4002 — Count Valid Sequences**
Solve LeetCode Count Valid Sequences using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Valid Sequences |
| LeetCode | #4002 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two **positive** integers `n` and `k`.

A **valid sequence** is a sequence of `k` positive integers such that:

The **sum** of all integers in the sequence is equal to `n`. 
 The **product** of all integers in the sequence is **even**.

Return the number of valid sequences. Since the answer may be very large, return it **modulo** `10^9​​​​​​​ + 7`.

Two sequences are considered **different** if they differ at any index. For example, `[1, 1, 2]` and `[1, 2, 1]` are considered different sequences.

## Constraints
- `1 <= n <= 5 * 10^5`
- `1 <= k <= n`

## Examples
### Example 1
- **Input:** `n = 5, k = 3`
- **Output:** `3`
- **Explanation:** The sequences of length `k = 3` whose sum is 5 are: 

 
 
 
 Sequence 
 Product 
 Parity 
 
 
 `[1, 1, 3]` 
 `1 * 1 * 3 = 3` 
 Odd 
 
 
 `[1, 2, 2]` 
 `1 * 2 * 2 = 4` 
 Even 
 
 
 `[2, 1, 2]` 
 `2 * 1 * 2 = 4` 
 Even 
 
 
 `[2, 2, 1]` 
 `2 * 2 * 1 = 4` 
 Even 
 
 
 `[1, 3, 1]` 
 `1 * 3 * 1 = 3` 
 Odd 
 
 
 `[3, 1, 1]` 
 `3 * 1 * 1 = 3` 
 Odd 
 
 
 

 There are 3 sequences with an even product, thus the answer is 3.

### Example 2
- **Input:** `n = 3, k = 2`
- **Output:** `2`
- **Explanation:** The sequences of length `k = 2` whose sum is 3 are: 

 
 
 
 Sequence 
 Product 
 Parity 
 
 
 `[1, 2]` 
 `1 * 2 = 2` 
 Even 
 
 
 `[2, 1]` 
 `2 * 1 = 2` 
 Even 
 
 
 

 There are 2 sequences with an even product, thus the answer is 2.

### Example 3
- **Input:** `n = 5, k = 5`
- **Output:** `0`
- **Explanation:** The only possible sequence of length `k = 5` whose sum is 5 is `[1, 1, 1, 1, 1]`, which has an odd product. Thus, the answer is 0.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Valid Sequences**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, k = 3`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The sequences of length `k = 3` whose sum is 5 are: 

 
 
 
 Sequence 
 Product 
 Parity 
 
 
 `[1, 1, 3]` 
 `1 * 1 * 3 = 3` 
 Odd 
 
 
 `[1, 2, 2]` 
 `1 * 2 * 2 = 4` 
 Even 
 
 
 `[2, 1, 2]` 
 `2 * 1 * 2 = 4` 
 Even 
 
 
 `[2, 2, 1]` 
 `2 * 2 * 1 = 4` 
 Even 
 
 
 `[1, 3, 1]` 
 `1 * 3 * 1 = 3` 
 Odd 
 
 
 `[3, 1, 1]` 
 `3 * 1 * 1 = 3` 
 Odd 
 
 
 

 There are 3 sequences with an even product, thus the answer is 3.

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
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var countValidSequences = function (n, k) {
    const MOD = 1000000007n;

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

    // factorials up to n
    const fact = new Array(n + 1);
    fact[0] = 1n;
    for (let i = 1; i <= n; i++) fact[i] = (fact[i - 1] * BigInt(i)) % MOD;

    const invFact = new Array(n + 1);
    invFact[n] = power(fact[n], MOD - 2n);
    for (let i = n; i >= 1; i--) invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;

    const comb = (a, b) => {
        if (b < 0 || b > a || a < 0) return 0n;
        return (((fact[a] * invFact[b]) % MOD) * invFact[a - b]) % MOD;
    };

    const total = comb(n - 1, k - 1);

    let allOdd = 0n;
    const diff = n - k;
    if (diff >= 0 && diff % 2 === 0) {
        allOdd = comb(diff / 2 + k - 1, k - 1);
    }

    return Number(((total - allOdd) % MOD + MOD) % MOD);
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
- [1359. Count All Valid Pickup and Delivery Options](../../1001-1500/1359-count-all-valid-pickup-and-delivery-options/)
- [2145. Count the Hidden Sequences](../../2001-2500/2145-count-the-hidden-sequences/)
- [2867. Count Valid Paths in a Tree](../../2501-3000/2867-count-valid-paths-in-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-valid-sequences/)
