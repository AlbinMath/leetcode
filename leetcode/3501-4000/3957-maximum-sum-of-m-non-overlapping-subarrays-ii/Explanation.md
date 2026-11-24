# LeetCode 3957: Maximum Sum of M Non-Overlapping Subarrays II

**LeetCode Problem #3957 — Maximum Sum of M Non-Overlapping Subarrays II**
Solve LeetCode Maximum Sum of M Non-Overlapping Subarrays II using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Sum of M Non-Overlapping Subarrays II |
| LeetCode | #3957 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of length `n`, and three integers `m`, `l`, and `r`.

Your task is to select **at least** one and **at most** `m` **non-overlapping subarrays ** from `nums` such that:

Each selected **subarray** has a length between `[l, r]` (inclusive). 
 The total sum of all selected **subarrays** is **maximized**.

Return the **maximum** total sum you can achieve.

## Constraints
- `1 <= n == nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5​​​​​​​`
- `1 <= m <= n`
- `1 <= l <= r <= n`

## Examples
### Example 1
- **Input:** `nums = [4,1,-5,2], m = 2, l = 1, r = 3`
- **Output:** `7`
- **Explanation:** One optimal strategy is to: 

 
 Select the subarray `[4, 1]` with sum `4 + 1 = 5` and the subarray `[2]` with sum 2. Both subarrays have length between `[l, r]`. 
 The total sum of these subarrays is `5 + 2 = 7`, which is the maximum achievable sum with at most `m = 2` subarrays.

### Example 2
- **Input:** `nums = [1,0,3,4], m = 2, l = 1, r = 2`
- **Output:** `8`
- **Explanation:** One optimal strategy is to: 

 
 Select the subarray `[1]` with sum `1` and the subarray `[3, 4]` with sum `3 + 4 = 7`. Both subarrays have length between `[l, r]`. 
 The total sum of these subarrays is `1 + 7 = 8`, which is the maximum achievable sum with at most `m = 2` subarrays.

### Example 3
- **Input:** `nums = [-1,7,-4], m = 1, l = 2, r = 3`
- **Output:** `6`
- **Explanation:** Select the subarray `[-1, 7]` from `nums` which has length between `[l, r]`. 
 The total sum of this subarray is `-1 + 7 = 6`, which is the maximum achievable sum with at most `m = 1` subarray.

### Example 4
- **Input:** `nums = [-3,-4,-1], m = 2, l = 1, r = 2`
- **Output:** `-1`
- **Explanation:** All subarrays of `nums` have negative sums. The optimal strategy is to select the subarray `[-1]`, which has length between `[l, r]`. 
 The total sum of this subarray is -1, which is the maximum achievable sum with at most `m = 2` subarrays.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Sum of M Non-Overlapping Subarrays II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,1,-5,2], m = 2, l = 1, r = 3`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** One optimal strategy is to: 

 
 Select the subarray `[4, 1]` with sum `4 + 1 = 5` and the subarray `[2]` with sum 2. Both subarrays have length between `[l, r]`. 
 The total sum of these subarrays is `5 + 2 = 7`, which is the maximum achievable sum with at most `m = 2` subarrays.

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
 * @param {number[]} nums
 * @param {number} m
 * @param {number} l
 * @param {number} r
 * @return {number}
 */
var maximumSum = function (nums, m, l, r) {
    const n = nums.length;
    const P = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) P[i + 1] = P[i] + nums[i];

    // f(1): best single subarray with length in [l, r]
    let f1 = -Infinity;
    {
        const dq = new Array(n + 1);
        let h = 0, t = 0;
        for (let i = l; i <= n; i++) {
            const s = i - l;
            while (h < t && P[dq[t - 1]] >= P[s]) t--;
            dq[t++] = s;
            while (dq[h] < i - r) h++;
            f1 = Math.max(f1, P[i] - P[dq[h]]);
        }
    }
    if (f1 <= 0) return f1;

    const dpV = new Float64Array(n + 1);
    const dpC = new Int32Array(n + 1);
    const kv = new Float64Array(n + 1);
    const dq = new Int32Array(n + 1);

    // returns [best value of sum - lambda*count, min count achieving it]
    const run = (lambda) => {
        let h = 0, t = 0;
        dpV[0] = 0; dpC[0] = 0;
        for (let i = 1; i <= n; i++) {
            const s = i - l;
            if (s >= 0) {
                kv[s] = dpV[s] - P[s];
                while (t > h) {
                    const b = dq[t - 1];
                    if (kv[s] > kv[b] || (kv[s] === kv[b] && dpC[s] <= dpC[b])) t--;
                    else break;
                }
                dq[t++] = s;
            }
            while (h < t && dq[h] < i - r) h++;

            dpV[i] = dpV[i - 1];
            dpC[i] = dpC[i - 1];
            if (h < t) {
                const f = dq[h];
                const cv = kv[f] + P[i] - lambda;
                const cc = dpC[f] + 1;
                if (cv > dpV[i] || (cv === dpV[i] && cc < dpC[i])) {
                    dpV[i] = cv;
                    dpC[i] = cc;
                }
            }
        }
        return [dpV[n], dpC[n]];
    };

    let lo = 0, hi = 1e10 + 1; // at hi, no subarray is worth taking (count 0)
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (run(mid)[1] <= m) hi = mid;
        else lo = mid + 1;
    }
    const [v] = run(lo);
    return v + lo * m;
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
- [3956. Maximum Sum of M Non-Overlapping Subarrays I](../../3501-4000/3956-maximum-sum-of-m-non-overlapping-subarrays-i/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](../../1001-1500/1031-maximum-sum-of-two-non-overlapping-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/)
