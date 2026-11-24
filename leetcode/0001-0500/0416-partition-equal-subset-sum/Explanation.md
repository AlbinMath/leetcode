# LeetCode 416: Partition Equal Subset Sum

**LeetCode Problem #416 — Partition Equal Subset Sum**
Solve LeetCode Partition Equal Subset Sum using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition Equal Subset Sum |
| LeetCode | #416 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer array `nums`, return `true` *if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or *`false`* otherwise*.

## Constraints
- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,5,11,5]`
- **Output:** `true`
- **Explanation:** The array can be partitioned as [1, 5, 5] and [11].

### Example 2
- **Input:** `nums = [1,2,3,5]`
- **Output:** `false`
- **Explanation:** The array cannot be partitioned into equal sum subsets.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Partition Equal Subset Sum**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,5,11,5]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The array can be partitioned as [1, 5, 5] and [11].

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
var canPartition = function(nums) {
    const total = nums.reduce((sum, num) => sum + num, 0);

    // An odd sum cannot be divided equally
    if (total % 2 !== 0) {
        return false;
    }

    const target = total / 2;
    const dp = Array(target + 1).fill(false);

    dp[0] = true;

    for (const num of nums) {
        // Iterate backward to use each number only once
        for (let sum = target; sum >= num; sum--) {
            dp[sum] = dp[sum] || dp[sum - num];
        }

        if (dp[target]) {
            return true;
        }
    }

    return dp[target];
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
- [698. Partition to K Equal Sum Subsets](../../0501-1000/0698-partition-to-k-equal-sum-subsets/)
- [3546. Equal Sum Grid Partition I](../../3501-4000/3546-equal-sum-grid-partition-i/)
- [3548. Equal Sum Grid Partition II](../../3501-4000/3548-equal-sum-grid-partition-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/)
