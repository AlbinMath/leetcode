# LeetCode 1420: Build Array Where You Can Find The Maximum Exactly K Comparisons

**LeetCode Problem #1420 — Build Array Where You Can Find The Maximum Exactly K Comparisons**
Solve LeetCode Build Array Where You Can Find The Maximum Exactly K Comparisons using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Build Array Where You Can Find The Maximum Exactly K Comparisons |
| LeetCode | #1420 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given three integers `n`, `m` and `k`. Consider the following algorithm to find the maximum element of an array of positive integers:

You should build the array arr which has the following properties:

`arr` has exactly `n` integers. 
 `1 <= arr[i] <= m` where `(0 <= i < n)`. 
 After applying the mentioned algorithm to `arr`, the value `search_cost` is equal to `k`.

Return *the number of ways* to build the array `arr` under the mentioned conditions. As the answer may grow large, the answer **must be** computed modulo `10^9 + 7`.

## Constraints
- `1 <= n <= 50`
- `1 <= m <= 100`
- `0 <= k <= n`

## Examples
### Example 1
- **Input:** `n = 2, m = 3, k = 1`
- **Output:** `6`
- **Explanation:** The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]

### Example 2
- **Input:** `n = 5, m = 2, k = 3`
- **Output:** `0`
- **Explanation:** There are no possible arrays that satisfy the mentioned conditions.

### Example 3
- **Input:** `n = 9, m = 1, k = 1`
- **Output:** `1`
- **Explanation:** The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Build Array Where You Can Find The Maximum Exactly K Comparisons**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, m = 3, k = 1`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]

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
var numOfArrays = function(n, m, k) {
    const MOD = 1000000007;

    if (k > n || k > m || k === 0) return 0;
    let dp = Array.from({ length: m + 1 }, () =>
        Array(k + 1).fill(0)
    );
    for (let j = 1; j <= m; j++) {
        dp[j][1] = 1;
    }
    for (let len = 2; len <= n; len++) {
        let next = Array.from({ length: m + 1 }, () =>
            Array(k + 1).fill(0)
        );

        for (let cost = 1; cost <= k; cost++) {
            let prefix = 0;

            for (let maxVal = 1; maxVal <= m; maxVal++) {
                if (maxVal > 1) {
                    prefix = (prefix + dp[maxVal - 1][cost - 1]) % MOD;
                }
                next[maxVal][cost] =
                    (dp[maxVal][cost] * maxVal + prefix) % MOD;
            }
        }

        dp = next;
    }
    let answer = 0;

    for (let maxVal = 1; maxVal <= m; maxVal++) {
        answer = (answer + dp[maxVal][k]) % MOD;
    }

    return answer;
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
- [2917. Find the K-or of an Array](../../2501-3000/2917-find-the-k-or-of-an-array/)
- [2940. Find Building Where Alice and Bob Can Meet](../../2501-3000/2940-find-building-where-alice-and-bob-can-meet/)
- [2945. Find Maximum Non-decreasing Array Length](../../2501-3000/2945-find-maximum-non-decreasing-array-length/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)
