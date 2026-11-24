# LeetCode 3317: Find the Number of Possible Ways for an Event

**LeetCode Problem #3317 — Find the Number of Possible Ways for an Event**
Solve LeetCode Find the Number of Possible Ways for an Event using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Number of Possible Ways for an Event |
| LeetCode | #3317 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given three integers `n`, `x`, and `y`.

An event is being held for `n` performers. When a performer arrives, they are **assigned** to one of the `x` stages. All performers assigned to the **same** stage will perform together as a band, though some stages *might* remain **empty**.

After all performances are completed, the jury will **award** each band a score in the range `[1, y]`.

Return the **total** number of possible ways the event can take place.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Note** that two events are considered to have been held **differently** if **either** of the following conditions is satisfied:

**Any** performer is *assigned* a different stage. 
 **Any** band is *awarded* a different score.

## Constraints
- `1 <= n, x, y <= 1000`

## Examples
### Example 1
- **Input:** `n = 1, x = 2, y = 3`
- **Output:** `6`
- **Explanation:** There are 2 ways to assign a stage to the performer. 
 The jury can award a score of either 1, 2, or 3 to the only band.

### Example 2
- **Input:** `n = 5, x = 2, y = 1`
- **Output:** `32`
- **Explanation:** Each performer will be assigned either stage 1 or stage 2. 
 All bands will be awarded a score of 1.

### Example 3
- **Input:** `n = 3, x = 3, y = 4`
- **Output:** `684`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Number of Possible Ways for an Event**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1, x = 2, y = 3`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** There are 2 ways to assign a stage to the performer. 
 The jury can award a score of either 1, 2, or 3 to the only band.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var numberOfWays = function(n, x, y) {
    const MOD = 1000000007n;
    const stirling = Array(n + 1).fill(0n);
    stirling[0] = 1n;

    for (let i = 1; i <= n; i++) {
        for (let j = i; j >= 1; j--) {
            stirling[j] =
                (stirling[j - 1] + BigInt(j) * stirling[j]) % MOD;
        }
        stirling[0] = 0n;
    }

    let ans = 0n;
    let falling = 1n;
    let scoreWays = 1n;

    for (let bands = 1; bands <= Math.min(n, x); bands++) {
        falling = falling * BigInt(x - bands + 1) % MOD;
        scoreWays = scoreWays * BigInt(y) % MOD;

        let ways = stirling[bands] * falling % MOD;
        ways = ways * scoreWays % MOD;
        ans = (ans + ways) % MOD;
    }

    return Number(ans);
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3025. Find the Number of Ways to Place People I](../../3001-3500/3025-find-the-number-of-ways-to-place-people-i/)
- [3027. Find the Number of Ways to Place People II](../../3001-3500/3027-find-the-number-of-ways-to-place-people-ii/)
- [3154. Find Number of Ways to Reach the K-th Stair](../../3001-3500/3154-find-number-of-ways-to-reach-the-k-th-stair/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/)
