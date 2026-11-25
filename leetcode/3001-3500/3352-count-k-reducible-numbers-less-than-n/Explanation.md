# LeetCode 3352: Count K-Reducible Numbers Less Than N

**LeetCode Problem #3352 — Count K-Reducible Numbers Less Than N**
Solve LeetCode Count K-Reducible Numbers Less Than N using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count K-Reducible Numbers Less Than N |
| LeetCode | #3352 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **binary** string `s` representing a number `n` in its binary form.

You are also given an integer `k`.

An integer `x` is called **k-reducible** if performing the following operation **at most** `k` times reduces it to 1:

Replace `x` with the **count** of set bits in its binary representation.

For example, the binary representation of 6 is `"110"`. Applying the operation once reduces it to 2 (since `"110"` has two set bits). Applying the operation again to 2 (binary `"10"`) reduces it to 1 (since `"10"` has one set bit).

Return an integer denoting the number of positive integers **less** than `n` that are **k-reducible**.

Since the answer may be too large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= s.length <= 800`
- `s` has no leading zeros.
- `s` consists only of the characters `'0'` and `'1'`.
- `1 <= k <= 5`

## Examples
### Example 1
- **Input:** `s = "111", k = 1`
- **Output:** `3`
- **Explanation:** `n = 7`. The 1-reducible integers less than 7 are 1, 2, and 4.

### Example 2
- **Input:** `s = "1000", k = 2`
- **Output:** `6`
- **Explanation:** `n = 8`. The 2-reducible integers less than 8 are 1, 2, 3, 4, 5, and 6.

### Example 3
- **Input:** `s = "1", k = 3`
- **Output:** `0`
- **Explanation:** There are no positive integers less than `n = 1`, so the answer is 0.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count K-Reducible Numbers Less Than N**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "111", k = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** `n = 7`. The 1-reducible integers less than 7 are 1, 2, and 4.

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
var countKReducibleNumbers = function(s, k) {
    const MOD = 1000000007;
    const n = s.length;

    // steps[i] = operations needed to reduce i to 1
    const steps = Array(n + 1).fill(0);
    for (let i = 2; i <= n; i++) {
        steps[i] = steps[i.toString(2).replace(/0/g, '').length] + 1;
    }

    // If popcount(x) = 1, x needs exactly one operation.
    const good = Array(n + 1).fill(false);
    for (let i = 1; i <= n; i++) {
        good[i] = (i === 1) || (steps[i] + 1 <= k);
    }

    // Binomial coefficients
    const C = Array.from({ length: n + 1 }, () =>
        Array(n + 1).fill(0)
    );
    C[0][0] = 1;

    for (let i = 1; i <= n; i++) {
        C[i][0] = C[i][i] = 1;
        for (let j = 1; j < i; j++) {
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
    }

    let ans = 0;

    // Count numbers smaller than s by their number of set bits.
    for (let ones = 1; ones <= n; ones++) {
        if (!good[ones]) continue;

        let remaining = ones;

        for (let i = 0; i < n; i++) {
            if (s[i] === '1') {
                const left = n - i - 1;

                if (remaining >= 0 && remaining <= left) {
                    ans = (ans + C[left][remaining]) % MOD;
                }

                remaining--;
                if (remaining < 0) break;
            }
        }
    }

    // The number n itself is never counted because only branches
    // where a 1 in s is changed to 0 are counted.

    return ans;
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
- [2302. Count Subarrays With Score Less Than K](../../2001-2500/2302-count-subarrays-with-score-less-than-k/)
- [3070. Count Submatrices with Top-Left Element and Sum Less Than k](../../3001-3500/3070-count-submatrices-with-top-left-element-and-sum-less-than-k/)
- [3835. Count Subarrays With Cost Less Than or Equal to K](../../3501-4000/3835-count-subarrays-with-cost-less-than-or-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/)
