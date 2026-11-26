# LeetCode 1959: Minimum Total Space Wasted With K Resizing Operations

**LeetCode Problem #1959 — Minimum Total Space Wasted With K Resizing Operations**
Solve LeetCode Minimum Total Space Wasted With K Resizing Operations using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Total Space Wasted With K Resizing Operations |
| LeetCode | #1959 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are currently designing a dynamic array. You are given a **0-indexed** integer array `nums`, where `nums[i]` is the number of elements that will be in the array at time `i`. In addition, you are given an integer `k`, the **maximum** number of times you can **resize** the array (to** any** size).

The size of the array at time `t`, `size_t`, must be at least `nums[t]` because there needs to be enough space in the array to hold all the elements. The **space wasted** at time `t` is defined as `size_t - nums[t]`, and the **total** space wasted is the **sum** of the space wasted across every time `t` where `0 <= t < nums.length`.

Return *the **minimum** **total space wasted** if you can resize the array at most* `k` *times*.

**Note:** The array can have **any size** at the start and does** not **count towards the number of resizing operations.

## Constraints
- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 10^6`
- `0 <= k <= nums.length - 1`

## Examples
### Example 1
- **Input:** `nums = [10,20], k = 0`
- **Output:** `10`
- **Explanation:** size = [20,20].
We can set the initial size to be 20.
The total wasted space is (20 - 10) + (20 - 20) = 10.

### Example 2
- **Input:** `nums = [10,20,30], k = 1`
- **Output:** `10`
- **Explanation:** size = [20,20,30].
We can set the initial size to be 20 and resize to 30 at time 2. 
The total wasted space is (20 - 10) + (20 - 20) + (30 - 30) = 10.

### Example 3
- **Input:** `nums = [10,20,15,30,20], k = 2`
- **Output:** `15`
- **Explanation:** size = [10,20,20,30,30].
We can set the initial size to 10, resize to 20 at time 1, and resize to 30 at time 3.
The total wasted space is (10 - 10) + (20 - 20) + (20 - 15) + (30 - 30) + (30 - 20) = 15.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum Total Space Wasted With K Resizing Operations**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [10,20], k = 0`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** size = [20,20].
We can set the initial size to be 20.
The total wasted space is (20 - 10) + (20 - 20) = 10.

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
var minSpaceWastedKResizing = function(nums, k) {
    const n = nums.length;
    const INF = Infinity;
    let prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    let cost = Array.from(
        { length: n },
        () => new Array(n).fill(0)
    );
    for (let i = 0; i < n; i++) {
        let maxVal = 0;
        for (let j = i; j < n; j++) {
            maxVal = Math.max(maxVal, nums[j]);
            let sum = prefix[j + 1] - prefix[i];
            cost[i][j] = (j - i + 1) * maxVal - sum;
        }
    }
    let dp = Array.from(
        { length: n + 1 },
        () => new Array(k + 2).fill(INF)
    );
    dp[0][0] = 0;
    for (let i = 1; i <= n; i++) {
        for (let g = 1; g <= Math.min(i, k + 1); g++) {
            for (let j = g - 1; j < i; j++) {
                dp[i][g] = Math.min(
                    dp[i][g],
                    dp[j][g - 1] + cost[j][i - 1]
                );
            }
        }
    }
    let answer = INF;
    for (let g = 1; g <= k + 1; g++) {
        answer = Math.min(answer, dp[n][g]);
    }
    return answer;
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
- [2111. Minimum Operations to Make the Array K-Increasing](../../2001-2500/2111-minimum-operations-to-make-the-array-k-increasing/)
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../2501-3000/2997-minimum-number-of-operations-to-make-array-xor-equal-to-k/)
- [3137. Minimum Number of Operations to Make Word K-Periodic](../../3001-3500/3137-minimum-number-of-operations-to-make-word-k-periodic/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/)
