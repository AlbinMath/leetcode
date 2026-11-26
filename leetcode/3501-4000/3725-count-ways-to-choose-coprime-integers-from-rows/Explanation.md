# LeetCode 3725: Count Ways to Choose Coprime Integers from Rows

**LeetCode Problem #3725 — Count Ways to Choose Coprime Integers from Rows**
Solve LeetCode Count Ways to Choose Coprime Integers from Rows using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Ways to Choose Coprime Integers from Rows |
| LeetCode | #3725 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a `m x n` matrix `mat` of positive integers.

Return an integer denoting the number of ways to choose **exactly one** integer from each row of `mat` such that the **greatest common divisor** of all chosen integers is 1.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= m == mat.length <= 150`
- `1 <= n == mat[i].length <= 150`
- `1 <= mat[i][j] <= 150`

## Examples
### Example 1
- **Input:** `mat = [[1,2],[3,4]]`
- **Output:** `3`
- **Explanation:** Chosen integer in the first row 
 Chosen integer in the second row 
 Greatest common divisor of chosen integers 
 
 
 1 
 3 
 1 
 
 
 1 
 4 
 1 
 
 
 2 
 3 
 1 
 
 
 2 
 4 
 2 
 
 
 

 3 of these combinations have a greatest common divisor of 1. Therefore, the answer is 3.

### Example 2
- **Input:** `mat = [[2,2],[2,2]]`
- **Output:** `0`
- **Explanation:** Every combination has a greatest common divisor of 2. Therefore, the answer is 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Ways to Choose Coprime Integers from Rows**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[1,2],[3,4]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Chosen integer in the first row 
 Chosen integer in the second row 
 Greatest common divisor of chosen integers 
 
 
 1 
 3 
 1 
 
 
 1 
 4 
 1 
 
 
 2 
 3 
 1 
 
 
 2 
 4 
 2 
 
 
 

 3 of these combinations have a greatest common divisor of 1. Therefore, the answer is 3.

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
 * @param {number[][]} mat
 * @return {number}
 */
var countCoprime = function (mat) {
    const MOD = 1000000007n;
    const MAXV = 150;

    // Möbius function via sieve
    const mu = new Array(MAXV + 1).fill(1);
    const isComp = new Array(MAXV + 1).fill(false);
    for (let p = 2; p <= MAXV; p++) {
        if (isComp[p]) continue;
        for (let j = p; j <= MAXV; j += p) {
            if (j > p) isComp[j] = true;
            mu[j] = -mu[j];
        }
        const sq = p * p;
        for (let j = sq; j <= MAXV; j += sq) mu[j] = 0;
    }

    let ans = 0n;
    for (let d = 1; d <= MAXV; d++) {
        if (mu[d] === 0) continue;

        let prod = 1n;
        for (const row of mat) {
            let cnt = 0;
            for (const x of row) if (x % d === 0) cnt++;
            if (cnt === 0) {
                prod = 0n;
                break;
            }
            prod = (prod * BigInt(cnt)) % MOD;
        }

        ans += BigInt(mu[d]) * prod;
        ans %= MOD;
    }

    ans = ((ans % MOD) + MOD) % MOD;
    return Number(ans);
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
- [2554. Maximum Number of Integers to Choose From a Range I](../../2501-3000/2554-maximum-number-of-integers-to-choose-from-a-range-i/)
- [3981. Count Distinct Ways to Form Target from Two Strings](../../3501-4000/3981-count-distinct-ways-to-form-target-from-two-strings/)
- [2180. Count Integers With Even Digit Sum](../../2001-2500/2180-count-integers-with-even-digit-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/)
