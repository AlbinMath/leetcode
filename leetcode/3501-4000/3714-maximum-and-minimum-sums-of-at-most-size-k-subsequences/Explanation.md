# LeetCode 3428: Maximum and Minimum Sums of at Most Size K Subsequences

**LeetCode Problem #3428 — Maximum and Minimum Sums of at Most Size K Subsequences**
Solve LeetCode Maximum and Minimum Sums of at Most Size K Subsequences using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum and Minimum Sums of at Most Size K Subsequences |
| LeetCode | #3428 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and a positive integer `k`. Return the sum of the **maximum** and **minimum** elements of all ** subsequences ** of `nums` with **at most** `k` elements.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- ` 1 <= k <= min(70, nums.length) `

## Examples
### Example 1
- **Input:** `nums = [1,2,3], k = 2`
- **Output:** `24`
- **Explanation:** The subsequences of `nums` with at most 2 elements are: 

 
 
 
 Subsequence 
 Minimum 
 Maximum 
 Sum 
 
 
 `[1]` 
 1 
 1 
 2 
 
 
 `[2]` 
 2 
 2 
 4 
 
 
 `[3]` 
 3 
 3 
 6 
 
 
 `[1, 2]` 
 1 
 2 
 3 
 
 
 `[1, 3]` 
 1 
 3 
 4 
 
 
 `[2, 3]` 
 2 
 3 
 5

### Example 2
- **Input:** `nums = [5,0,6], k = 1`
- **Output:** `2 2`
- **Explanation:** For subsequences with exactly 1 element, the minimum and maximum values are the element itself. Therefore, the total is `5 + 5 + 0 + 0 + 6 + 6 = 22`.

### Example 3
- **Input:** `nums = [1,1,1], k = 2`
- **Output:** `12`
- **Explanation:** The subsequences `[1, 1]` and `[1]` each appear 3 times. For all of them, the minimum and maximum are both 1. Thus, the total is 12.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum and Minimum Sums of at Most Size K Subsequences**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3], k = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `24`.
4. **Verification:** The subsequences of `nums` with at most 2 elements are: 

 
 
 
 Subsequence 
 Minimum 
 Maximum 
 Sum 
 
 
 `[1]` 
 1 
 1 
 2 
 
 
 `[2]` 
 2 
 2 
 4 
 
 
 `[3]` 
 3 
 3 
 6 
 
 
 `[1, 2]` 
 1 
 2 
 3 
 
 
 `[1, 3]` 
 1 
 3 
 4 
 
 
 `[2, 3]` 
 2 
 3 
 5

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
 * @param {number} k
 * @return {number}
 */
var minMaxSums = function (nums, k) {
    const MOD = 1000000007n;
    const n = nums.length;
    nums.sort((a, b) => a - b);

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

    // Factorials and inverse factorials up to n
    const fact = new Array(n + 1).fill(1n);
    for (let i = 1; i <= n; i++) fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    const invFact = new Array(n + 1).fill(1n);
    invFact[n] = power(fact[n], MOD - 2n);
    for (let i = n; i > 0; i--) invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;

    const comb = (a, b) => {
        if (b < 0 || b > a) return 0n;
        return (((fact[a] * invFact[b]) % MOD) * invFact[a - b]) % MOD;
    };

    // sum_{j=0}^{k-1} C(x, j)
    const countUpTo = (x) => {
        let s = 0n;
        for (let j = 0; j < k && j <= x; j++) s += comb(x, j);
        return s % MOD;
    };

    let ans = 0n;
    for (let i = 0; i < n; i++) {
        const cnt = (countUpTo(i) + countUpTo(n - 1 - i)) % MOD;
        ans = (ans + BigInt(nums[i]) * cnt) % MOD;
    }
    return Number(ans);
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
- [3430. Maximum and Minimum Sums of at Most Size K Subarrays](../../3501-4000/3725-maximum-and-minimum-sums-of-at-most-size-k-subarrays/)
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../../1501-2000/1629-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
- [2106. Maximum Fruits Harvested After at Most K Steps](../../2001-2500/2229-maximum-fruits-harvested-after-at-most-k-steps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/)
