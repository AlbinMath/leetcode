# LeetCode 3539: Find Sum of Array Product of Magical Sequences

**LeetCode Problem #3539 — Find Sum of Array Product of Magical Sequences**
Solve LeetCode Find Sum of Array Product of Magical Sequences using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Sum of Array Product of Magical Sequences |
| LeetCode | #3539 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integers, `m` and `k`, and an integer array `nums`.

A sequence of integers `seq` is called **magical** if:

`seq` has a size of `m`. 
 `0 <= seq[i] < nums.length` 
 The **binary representation** of `2^seq[0] + 2^seq[1] + ... + 2^seq[m - 1]` has `k` **set bits**.

The **array product** of this sequence is defined as `prod(seq) = (nums[seq[0]] * nums[seq[1]] * ... * nums[seq[m - 1]])`.

Return the **sum** of the **array products** for all valid **magical** sequences.

Since the answer may be large, return it **modulo** `10^9 + 7`.

A **set bit** refers to a bit in the binary representation of a number that has a value of 1.

## Constraints
- `1 <= k <= m <= 30`
- `1 <= nums.length <= 50`
- `1 <= nums[i] <= 10^8`

## Examples
### Example 1
- **Input:** `m = 5, k = 5, nums = [1,10,100,10000,1000000]`
- **Output:** `991600007`
- **Explanation:** All permutations of `[0, 1, 2, 3, 4]` are magical sequences, each with an array product of 10^13.

### Example 2
- **Input:** `m = 2, k = 2, nums = [5,4,3,2,1]`
- **Output:** `170`
- **Explanation:** The magical sequences are `[0, 1]`, `[0, 2]`, `[0, 3]`, `[0, 4]`, `[1, 0]`, `[1, 2]`, `[1, 3]`, `[1, 4]`, `[2, 0]`, `[2, 1]`, `[2, 3]`, `[2, 4]`, `[3, 0]`, `[3, 1]`, `[3, 2]`, `[3, 4]`, `[4, 0]`, `[4, 1]`, `[4, 2]`, and `[4, 3]`.

### Example 3
- **Input:** `m = 1, k = 1, nums = [28]`
- **Output:** `28`
- **Explanation:** The only magical sequence is `[0]`.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Find Sum of Array Product of Magical Sequences**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We decompose the problem into overlapping subproblems using a **Integer Bitmask**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `m = 5, k = 5, nums = [1,10,100,10000,1000000]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `991600007`.
4. **Verification:** All permutations of `[0, 1, 2, 3, 4]` are magical sequences, each with an array product of 10^13.

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
 * @param {number} m
 * @param {number} k
 * @param {number[]} nums
 * @return {number}
 */
var magicalSum = function (m, k, nums) {
    const MOD = 1000000007;
    const MODn = 1000000007n;
    const len = nums.length;

    const mul = (a, b) =>
        (((a * (b >>> 16)) % MOD) * 65536 + a * (b & 65535)) % MOD;

    const power = (base, exp) => {
        let r = 1n;
        base %= MODn;
        while (exp > 0n) {
            if (exp & 1n) r = (r * base) % MODn;
            base = (base * base) % MODn;
            exp >>= 1n;
        }
        return r;
    };

    // factorials and inverse factorials up to m
    const fact = [1n];
    for (let i = 1; i <= m; i++) fact.push((fact[i - 1] * BigInt(i)) % MODn);
    const invFact = fact.map((f) => power(f, MODn - 2n));

    // coef[i][c] = nums[i]^c / c!
    const coef = [];
    for (let i = 0; i < len; i++) {
        const row = [];
        let p = 1n;
        const base = BigInt(nums[i]) % MODn;
        for (let c = 0; c <= m; c++) {
            row.push(Number((p * invFact[c]) % MODn));
            p = (p * base) % MODn;
        }
        coef.push(row);
    }

    const C = m + 1; // carry never exceeds m
    const K = k + 1;
    const idx = (j, c, o) => (j * C + c) * K + o;
    const size = (m + 1) * C * K;

    let dp = new Array(size).fill(0);
    dp[idx(0, 0, 0)] = 1;

    for (let i = 0; i < len; i++) {
        const nd = new Array(size).fill(0);
        const row = coef[i];
        for (let j = 0; j <= m; j++) {
            for (let c = 0; c <= j; c++) {
                for (let o = 0; o <= k; o++) {
                    const cur = dp[idx(j, c, o)];
                    if (cur === 0) continue;
                    for (let cnt = 0; j + cnt <= m; cnt++) {
                        const t = c + cnt;
                        const no = o + (t & 1);
                        if (no > k) continue;
                        const nc = t >> 1;
                        const id = idx(j + cnt, nc, no);
                        nd[id] = (nd[id] + mul(cur, row[cnt])) % MOD;
                    }
                }
            }
        }
        dp = nd;
    }

    const popcount = (x) => {
        let r = 0;
        while (x) {
            r += x & 1;
            x >>= 1;
        }
        return r;
    };

    let total = 0;
    for (let c = 0; c <= m; c++) {
        for (let o = 0; o <= k; o++) {
            if (o + popcount(c) === k) {
                total = (total + dp[idx(m, c, o)]) % MOD;
            }
        }
    }
    return Number((BigInt(total) * fact[m]) % MODn);
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
- [2221. Find Triangular Sum of an Array](../../2001-2500/2324-find-triangular-sum-of-an-array/)
- [238. Product of Array Except Self](../../0001-0500/0238-product-of-array-except-self/)
- [1281. Subtract the Product and Sum of Digits of an Integer](../../1001-1500/1406-subtract-the-product-and-sum-of-digits-of-an-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/)
