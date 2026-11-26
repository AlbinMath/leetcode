# LeetCode 3077: Maximum Strength of K Disjoint Subarrays

**LeetCode Problem #3077 — Maximum Strength of K Disjoint Subarrays**
Solve LeetCode Maximum Strength of K Disjoint Subarrays using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Strength of K Disjoint Subarrays |
| LeetCode | #3077 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of integers `nums` with length `n`, and a positive **odd** integer `k`.

Select exactly `k` disjoint subarrays `sub_1, sub_2, ..., sub_k` from `nums` such that the last element of `sub_i` appears before the first element of `sub_{i+1}` for all `1 <= i <= k-1`. The goal is to maximize their combined strength.

The strength of the selected subarrays is defined as:

`strength = k * sum(sub_1)- (k - 1) * sum(sub_2) + (k - 2) * sum(sub_3) - ... - 2 * sum(sub_{k-1}) + sum(sub_k)`

where `sum(sub_i)` is the sum of the elements in the `i`-th subarray.

Return the **maximum** possible strength that can be obtained from selecting exactly `k` disjoint subarrays from `nums`.

**Note** that the chosen subarrays **don't** need to cover the entire array.

## Constraints
- `1 <= n <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `1 <= k <= n`
- `1 <= n * k <= 10^6`
- `k` is odd.

## Examples
### Example 1
- **Input:** `nums = [1,2,3,-1,2], k = 3`
- **Output:** `22`
- **Explanation:** The best possible way to select 3 subarrays is: nums[0..2], nums[3..3], and nums[4..4]. The strength is calculated as follows: 

 `strength = 3 * (1 + 2 + 3) - 2 * (-1) + 2 = 22`

### Example 2
- **Input:** `nums = [12,-2,-2,-2,-2], k = 5`
- **Output:** `64`
- **Explanation:** The only possible way to select 5 disjoint subarrays is: nums[0..0], nums[1..1], nums[2..2], nums[3..3], and nums[4..4]. The strength is calculated as follows: 

 `strength = 5 * 12 - 4 * (-2) + 3 * (-2) - 2 * (-2) + (-2) = 64`

### Example 3
- **Input:** `nums = [-1,-2,-3], k = 1`
- **Output:** `-1`
- **Explanation:** The best possible way to select 1 subarray is: nums[0..0]. The strength is -1.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Strength of K Disjoint Subarrays**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,-1,2], k = 3`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `22`.
4. **Verification:** The best possible way to select 3 subarrays is: nums[0..2], nums[3..3], and nums[4..4]. The strength is calculated as follows: 

 `strength = 3 * (1 + 2 + 3) - 2 * (-1) + 2 = 22`

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
var maximumStrength = function(nums, k) {
    const dp = new Array(k + 1).fill(-Infinity);
    const ending = new Array(k + 1).fill(-Infinity);
    dp[0] = 0;

    for (let num of nums) {
        for (let j = k; j >= 1; j--) {

            const weight = (j % 2 === 1 ? 1 : -1) * (k - j + 1);
            ending[j] = Math.max(
                ending[j],
                dp[j - 1]
            ) + weight * num;
            dp[j] = Math.max(dp[j], ending[j]);
        }
    }

    return dp[k];
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
- [2461. Maximum Sum of Distinct Subarrays With Length K](../../2001-2500/2461-maximum-sum-of-distinct-subarrays-with-length-k/)
- [3430. Maximum and Minimum Sums of at Most Size K Subarrays](../../3001-3500/3430-maximum-and-minimum-sums-of-at-most-size-k-subarrays/)
- [992. Subarrays with K Different Integers](../../0501-1000/0992-subarrays-with-k-different-integers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/)
