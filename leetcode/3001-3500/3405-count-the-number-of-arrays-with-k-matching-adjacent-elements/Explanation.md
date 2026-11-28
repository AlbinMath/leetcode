# LeetCode 3405: Count the Number of Arrays with K Matching Adjacent Elements

**LeetCode Problem #3405 — Count the Number of Arrays with K Matching Adjacent Elements**
Solve LeetCode Count the Number of Arrays with K Matching Adjacent Elements using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Arrays with K Matching Adjacent Elements |
| LeetCode | #3405 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given three integers `n`, `m`, `k`. A **good array** `arr` of size `n` is defined as follows:

Each element in `arr` is in the **inclusive** range `[1, m]`. 
 *Exactly* `k` indices `i` (where `1 <= i < n`) satisfy the condition `arr[i - 1] == arr[i]`.

Return the number of **good arrays** that can be formed.

Since the answer may be very large, return it **modulo **`10^9 + 7`.

## Constraints
- `1 <= n <= 10^5`
- `1 <= m <= 10^5`
- `0 <= k <= n - 1`

## Examples
### Example 1
- **Input:** `n = 3, m = 2, k = 1`
- **Output:** `4`
- **Explanation:** There are 4 good arrays. They are `[1, 1, 2]`, `[1, 2, 2]`, `[2, 1, 1]` and `[2, 2, 1]`. 
 Hence, the answer is 4.

### Example 2
- **Input:** `n = 4, m = 2, k = 2`
- **Output:** `6`
- **Explanation:** The good arrays are `[1, 1, 1, 2]`, `[1, 1, 2, 2]`, `[1, 2, 2, 2]`, `[2, 1, 1, 1]`, `[2, 2, 1, 1]` and `[2, 2, 2, 1]`. 
 Hence, the answer is 6.

### Example 3
- **Input:** `n = 5, m = 2, k = 0`
- **Output:** `2`
- **Explanation:** The good arrays are `[1, 2, 1, 2, 1]` and `[2, 1, 2, 1, 2]`. Hence, the answer is 2.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count the Number of Arrays with K Matching Adjacent Elements**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, m = 2, k = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** There are 4 good arrays. They are `[1, 1, 2]`, `[1, 2, 2]`, `[2, 1, 1]` and `[2, 2, 1]`. 
 Hence, the answer is 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number} n
 * @param {number} m
 * @param {number} k
 * @return {number}
 */
var countGoodArrays = function (n, m, k) {
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

    // Factorials up to n - 1
    const fact = new Array(n).fill(1n);
    for (let i = 1; i < n; i++) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }

    // C(n-1, k) = (n-1)! / (k! * (n-1-k)!)
    const comb =
        (fact[n - 1] *
            power(fact[k], MOD - 2n) % MOD *
            power(fact[n - 1 - k], MOD - 2n)) %
        MOD;

    const ways = (BigInt(m) * power(BigInt(m - 1), BigInt(n - k - 1))) % MOD;

    return Number((comb * ways) % MOD);
};
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3759. Count Elements With at Least K Greater Values](../../3501-4000/3759-count-elements-with-at-least-k-greater-values/)
- [4043. Count Rotations With Exactly K Equal Adjacent Pairs](../../4001-4500/4043-count-rotations-with-exactly-k-equal-adjacent-pairs/)
- [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](../../1001-1500/1343-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/)
