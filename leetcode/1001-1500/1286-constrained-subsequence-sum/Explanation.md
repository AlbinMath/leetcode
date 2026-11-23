# LeetCode 1425: Constrained Subsequence Sum

**LeetCode Problem #1425 — Constrained Subsequence Sum**
Solve LeetCode Constrained Subsequence Sum using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Constrained Subsequence Sum |
| LeetCode | #1425 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer array `nums` and an integer `k`, return the maximum sum of a **non-empty** subsequence of that array such that for every two **consecutive** integers in the subsequence, `nums[i]` and `nums[j]`, where `i < j`, the condition `j - i <= k` is satisfied.

A *subsequence* of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

## Constraints
- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [10,2,-10,5,20], k = 2`
- **Output:** `37`

### Example 2
- **Input:** `nums = [-1,-2,-3], k = 1`
- **Output:** `-1`

### Example 3
- **Input:** `nums = [10,-2,-10,-5,20], k = 2`
- **Output:** `23`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Constrained Subsequence Sum**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [10,2,-10,5,20], k = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `37`.

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
var constrainedSubsetSum = function (nums, k) {
    const n = nums.length;
    const dp = new Array(n);
    const dq = new Array(n);
    let head = 0, tail = 0; // deque occupies dq[head..tail-1]
    let ans = -Infinity;

    for (let i = 0; i < n; i++) {
        if (head < tail && dq[head] < i - k) head++;

        const best = head < tail ? Math.max(0, dp[dq[head]]) : 0;
        dp[i] = nums[i] + best;
        ans = Math.max(ans, dp[i]);

        while (head < tail && dp[dq[tail - 1]] <= dp[i]) tail--;
        dq[tail++] = i;
    }
    return ans;
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
- [1755. Closest Subsequence Sum](../../1501-2000/1881-closest-subsequence-sum/)
- [2099. Find Subsequence of Length K With the Largest Sum](../../2001-2500/2204-find-subsequence-of-length-k-with-the-largest-sum/)
- [2835. Minimum Operations to Form Subsequence With Target Sum](../../3001-3500/3025-minimum-operations-to-form-subsequence-with-target-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/constrained-subsequence-sum/)
