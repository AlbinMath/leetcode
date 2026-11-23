# LeetCode 2528: Maximize the Minimum Powered City

**LeetCode Problem #2528 — Maximize the Minimum Powered City**
Solve LeetCode Maximize the Minimum Powered City using JavaScript and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize the Minimum Powered City |
| LeetCode | #2528 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** integer array `stations` of length `n`, where `stations[i]` represents the number of power stations in the `i^th` city.

Each power station can provide power to every city in a fixed **range**. In other words, if the range is denoted by `r`, then a power station at city `i` can provide power to all cities `j` such that `|i - j| <= r` and `0 <= i, j <= n - 1`.

Note that `|x|` denotes **absolute** value. For example, `|7 - 5| = 2` and `|3 - 10| = 7`.

The **power** of a city is the total number of power stations it is being provided power from.

The government has sanctioned building `k` more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.

Given the two integers `r` and `k`, return *the **maximum possible minimum power** of a city, if the additional power stations are built optimally.*

**Note** that you can build the `k` power stations in multiple cities.

## Constraints
- `n == stations.length`
- `1 <= n <= 10^5`
- `0 <= stations[i] <= 10^5`
- `0 <= r <= n - 1`
- `0 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `stations = [1,2,4,5,0], r = 1, k = 2`
- **Output:** `5`
- **Explanation:** One of the optimal ways is to install both the power stations at city 1. 
So stations will become [1,4,4,5,0].
- City 0 is provided by 1 + 4 = 5 power stations.
- City 1 is provided by 1 + 4 + 4 = 9 power stations.
- City 2 is provided by 4 + 4 + 5 = 13 power stations.
- City 3 is provided by 5 + 4 = 9 power stations.
- City 4 is provided by 5 + 0 = 5 power stations.
So the minimum power of a city is 5.
Since it is not possible to obtain a larger power, we return 5.

### Example 2
- **Input:** `stations = [4,4,4,4], r = 0, k = 3`
- **Output:** `4`
- **Explanation:** It can be proved that we cannot make the minimum power of a city greater than 4.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize the Minimum Powered City**, we observe the problem requirements and utilize the **Sliding Window** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `stations = [1,2,4,5,0], r = 1, k = 2`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** One of the optimal ways is to install both the power stations at city 1. 
So stations will become [1,4,4,5,0].
- City 0 is provided by 1 + 4 = 5 power stations.
- City 1 is provided by 1 + 4 + 4 = 9 power stations.
- City 2 is provided by 4 + 4 + 5 = 13 power stations.
- City 3 is provided by 5 + 4 = 9 power stations.
- City 4 is provided by 5 + 0 = 5 power stations.
So the minimum power of a city is 5.
Since it is not possible to obtain a larger power, we return 5.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[]} stations
 * @param {number} r
 * @param {number} k
 * @return {number}
 */
var maxPower = function (stations, r, k) {
    const n = stations.length;

    // initial power of each city via prefix sums
    const pre = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pre[i + 1] = pre[i] + stations[i];
    const power = new Array(n);
    let mn = Infinity;
    for (let i = 0; i < n; i++) {
        const lo = Math.max(0, i - r);
        const hi = Math.min(n - 1, i + r);
        power[i] = pre[hi + 1] - pre[lo];
        if (power[i] < mn) mn = power[i];
    }

    const check = (x) => {
        const end = new Array(n + 1).fill(0); // end[i]: amount that stops covering at i
        let added = 0, used = 0;
        for (let i = 0; i < n; i++) {
            added -= end[i];
            const cur = power[i] + added;
            if (cur < x) {
                const need = x - cur;
                used += need;
                if (used > k) return false;
                added += need;
                const stop = i + 2 * r + 1;
                if (stop < n) end[stop] += need;
            }
        }
        return true;
    };

    let lo = mn, hi = mn + k;
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (check(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2934. Minimum Operations to Maximize Last Elements in Arrays](../../3001-3500/3190-minimum-operations-to-maximize-last-elements-in-arrays/)
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1047-maximize-sum-of-array-after-k-negations/)
- [1659. Maximize Grid Happiness](../../1501-2000/1778-maximize-grid-happiness/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-the-minimum-powered-city/)
