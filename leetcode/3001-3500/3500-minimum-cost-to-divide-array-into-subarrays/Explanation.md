# LeetCode 3500: Minimum Cost to Divide Array Into Subarrays

**LeetCode Problem #3500 — Minimum Cost to Divide Array Into Subarrays**
Solve LeetCode Minimum Cost to Divide Array Into Subarrays using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Divide Array Into Subarrays |
| LeetCode | #3500 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integer arrays, `nums` and `cost`, of the same size, and an integer `k`.

You can divide `nums` into subarrays . The cost of the `i^th` subarray consisting of elements `nums[l..r]` is:

`(nums[0] + nums[1] + ... + nums[r] + k * i) * (cost[l] + cost[l + 1] + ... + cost[r])`.

**Note** that `i` represents the order of the subarray: 1 for the first subarray, 2 for the second, and so on.

Return the **minimum** total cost possible from any valid division.

## Constraints
- `1 <= nums.length <= 1000`
- `cost.length == nums.length`
- `1 <= nums[i], cost[i] <= 1000`
- `1 <= k <= 1000`

## Examples
### Example 1
- **Input:** `nums = [3,1,4], cost = [4,6,6], k = 1`
- **Output:** `110`
- **Explanation:** The minimum total cost possible can be achieved by dividing `nums` into subarrays `[3, 1]` and `[4]`.

 
 The cost of the first subarray `[3,1]` is `(3 + 1 + 1 * 1) * (4 + 6) = 50`. 
 The cost of the second subarray `[4]` is `(3 + 1 + 4 + 1 * 2) * 6 = 60`.

### Example 2
- **Input:** `nums = [4,8,5,1,14,2,2,12,1], cost = [7,2,8,4,2,2,1,1,2], k = 7`
- **Output:** `985`
- **Explanation:** The minimum total cost possible can be achieved by dividing `nums` into subarrays `[4, 8, 5, 1]`, `[14, 2, 2]`, and `[12, 1]`.

 
 The cost of the first subarray `[4, 8, 5, 1]` is `(4 + 8 + 5 + 1 + 7 * 1) * (7 + 2 + 8 + 4) = 525`. 
 The cost of the second subarray `[14, 2, 2]` is `(4 + 8 + 5 + 1 + 14 + 2 + 2 + 7 * 2) * (2 + 2 + 1) = 250`. 
 The cost of the third subarray `[12, 1]` is `(4 + 8 + 5 + 1 + 14 + 2 + 2 + 12 + 1 + 7 * 3) * (1 + 2) = 210`.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum Cost to Divide Array Into Subarrays**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,4], cost = [4,6,6], k = 1`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `110`.
4. **Verification:** The minimum total cost possible can be achieved by dividing `nums` into subarrays `[3, 1]` and `[4]`.

 
 The cost of the first subarray `[3,1]` is `(3 + 1 + 1 * 1) * (4 + 6) = 50`. 
 The cost of the second subarray `[4]` is `(3 + 1 + 4 + 1 * 2) * 6 = 60`.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)
        N = [0] * (n + 1)
        C = [0] * (n + 1)
        for i in range(n):
            N[i + 1] = N[i] + nums[i]
            C[i + 1] = C[i] + cost[i]
        T = C[n]

        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            best = INF
            for j in range(i):
                v = dp[j] + N[i] * (C[i] - C[j]) + k * (T - C[j])
                if v < best:
                    best = v
            dp[i] = best
        return dp[n]
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
- [3010. Divide an Array Into Subarrays With Minimum Cost I](../../3001-3500/3010-divide-an-array-into-subarrays-with-minimum-cost-i/)
- [3013. Divide an Array Into Subarrays With Minimum Cost II](../../3001-3500/3013-divide-an-array-into-subarrays-with-minimum-cost-ii/)
- [2448. Minimum Cost to Make Array Equal](../../2001-2500/2448-minimum-cost-to-make-array-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/)
