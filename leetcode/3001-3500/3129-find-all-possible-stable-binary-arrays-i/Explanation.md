# LeetCode 3129: Find All Possible Stable Binary Arrays I

**LeetCode Problem #3129 — Find All Possible Stable Binary Arrays I**
Solve LeetCode Find All Possible Stable Binary Arrays I using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find All Possible Stable Binary Arrays I |
| LeetCode | #3129 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given 3 positive integers `num_zeros`, `num_ones`, and `limit`.

A binary array `arr` is called **stable** if:

The number of occurrences of 0 in `arr` is **exactly **`num_zeros`. 
 The number of occurrences of 1 in `arr` is **exactly** `num_ones`. 
 Each subarray of `arr` with a size greater than `limit` must contain **at least** one occurrence of **both** 0 and 1.

Return an integer denoting the *total* number of **stable** binary arrays.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= zero, one, limit <= 200`

## Examples
### Example 1
- **Input:** `zero = 1, one = 1, limit = 2`
- **Output:** `2`
- **Explanation:** The two possible stable binary arrays are `[1,0]` and `[0,1]`, as both arrays have a single 0 and a single 1, and no subarray has a length greater than 2.

### Example 2
- **Input:** `zero = 1, one = 2, limit = 1`
- **Output:** `1`
- **Explanation:** The only possible stable binary array is `[1,0,1]`. 

 Note that the binary arrays `[1,1,0]` and `[0,1,1]` have subarrays of length 2 with identical elements, hence, they are not stable.

### Example 3
- **Input:** `zero = 3, one = 3, limit = 2`
- **Output:** `14`
- **Explanation:** All the possible stable binary arrays are `[0,0,1,0,1,1]`, `[0,0,1,1,0,1]`, `[0,1,0,0,1,1]`, `[0,1,0,1,0,1]`, `[0,1,0,1,1,0]`, `[0,1,1,0,0,1]`, `[0,1,1,0,1,0]`, `[1,0,0,1,0,1]`, `[1,0,0,1,1,0]`, `[1,0,1,0,0,1]`, `[1,0,1,0,1,0]`, `[1,0,1,1,0,0]`, `[1,1,0,0,1,0]`, and `[1,1,0,1,0,0]`.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find All Possible Stable Binary Arrays I**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We decompose the problem into overlapping subproblems using a **Integer Bitmask**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `zero = 1, one = 1, limit = 2`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The two possible stable binary arrays are `[1,0]` and `[0,1]`, as both arrays have a single 0 and a single 1, and no subarray has a length greater than 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var numberOfStableArrays = function(zero, one, limit) {
    const MOD = 1000000007;
    const dp0 = Array.from(
        { length: zero + 1 },
        () => new Array(one + 1).fill(0)
    );

    const dp1 = Array.from(
        { length: zero + 1 },
        () => new Array(one + 1).fill(0)
    );
    for (let i = 1; i <= Math.min(zero, limit); i++) {
        dp0[i][0] = 1;
    }
    for (let j = 1; j <= Math.min(one, limit); j++) {
        dp1[0][j] = 1;
    }
    for (let i = 1; i <= zero; i++) {
        for (let j = 1; j <= one; j++) {
            dp0[i][j] = (
                dp0[i - 1][j] +
                dp1[i - 1][j]
            ) % MOD;

            if (i - limit - 1 >= 0) {
                dp0[i][j] = (
                    dp0[i][j] -
                    dp1[i - limit - 1][j] +
                    MOD
                ) % MOD;
            }
            dp1[i][j] = (
                dp0[i][j - 1] +
                dp1[i][j - 1]
            ) % MOD;

            if (j - limit - 1 >= 0) {
                dp1[i][j] = (
                    dp1[i][j] -
                    dp0[i][j - limit - 1] +
                    MOD
                ) % MOD;
            }
        }
    }

    return (dp0[zero][one] + dp1[zero][one]) % MOD;
};
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3130. Find All Possible Stable Binary Arrays II](../../3001-3500/3130-find-all-possible-stable-binary-arrays-ii/)
- [894. All Possible Full Binary Trees](../../0501-1000/0894-all-possible-full-binary-trees/)
- [2115. Find All Possible Recipes from Given Supplies](../../2001-2500/2115-find-all-possible-recipes-from-given-supplies/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/)
