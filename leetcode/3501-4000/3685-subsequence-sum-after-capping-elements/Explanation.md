# LeetCode 3685: Subsequence Sum After Capping Elements

**LeetCode Problem #3685 — Subsequence Sum After Capping Elements**
Solve LeetCode Subsequence Sum After Capping Elements using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Subsequence Sum After Capping Elements |
| LeetCode | #3685 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of size `n` and a positive integer `k`.

An array **capped** by value `x` is obtained by replacing every element `nums[i]` with `min(nums[i], x)`.

For each integer x from 1 to n , determine whether it is possible to choose a ** subsequence ** from the array capped by `x` such that the sum of the chosen elements is **exactly** k .

Return a **0-indexed** boolean array answer of size n , where answer[i] is true if it is possible when using x = i + 1 , and false otherwise.

## Constraints
- `1 <= n == nums.length <= 4000`
- `1 <= nums[i] <= n`
- `1 <= k <= 4000`

## Examples
### Example 1
- **Input:** `nums = [4,3,2,4], k = 5`
- **Output:** `[false,false,true,true]`
- **Explanation:** For `x = 1`, the capped array is `[1, 1, 1, 1]`. Possible sums are `1, 2, 3, 4`, so it is impossible to form a sum of `5`. 
 For `x = 2`, the capped array is `[2, 2, 2, 2]`. Possible sums are `2, 4, 6, 8`, so it is impossible to form a sum of `5`. 
 For `x = 3`, the capped array is `[3, 3, 2, 3]`. A subsequence `[2, 3]` sums to `5`, so it is possible. 
 For `x = 4`, the capped array is `[4, 3, 2, 4]`. A subsequence `[3, 2]` sums to `5`, so it is possible.

### Example 2
- **Input:** `nums = [1,2,3,4,5], k = 3`
- **Output:** `[true,true,true,true,true]`
- **Explanation:** For every value of `x`, it is always possible to select a subsequence from the capped array that sums exactly to `3`.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Subsequence Sum After Capping Elements**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,3,2,4], k = 5`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[false,false,true,true]`.
4. **Verification:** For `x = 1`, the capped array is `[1, 1, 1, 1]`. Possible sums are `1, 2, 3, 4`, so it is impossible to form a sum of `5`. 
 For `x = 2`, the capped array is `[2, 2, 2, 2]`. Possible sums are `2, 4, 6, 8`, so it is impossible to form a sum of `5`. 
 For `x = 3`, the capped array is `[3, 3, 2, 3]`. A subsequence `[2, 3]` sums to `5`, so it is possible. 
 For `x = 4`, the capped array is `[4, 3, 2, 4]`. A subsequence `[3, 2]` sums to `5`, so it is possible.

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
var subsequenceSumAfterCapping = function(nums, k) {
    const n = nums.length;
    const freq = new Array(n + 1).fill(0);
    for (const num of nums) {
        freq[num]++;
    }
    const dp = new Array(k + 1).fill(false);
    dp[0] = true;
    const answer = new Array(n).fill(false);
    let largeCount = n;
    for (let x = 1; x <= n; x++) {
        const maxTake = Math.min(largeCount, Math.floor(k / x));
        for (let t = 0; t <= maxTake; t++) {
            const remaining = k - t * x;
            if (dp[remaining]) {
                answer[x - 1] = true;
                break;
            }
        }
        largeCount -= freq[x];
        for (let j = 0; j < freq[x]; j++) {
            for (let sum = k; sum >= x; sum--) {
                if (dp[sum - x]) {
                    dp[sum] = true;
                }
            }
        }
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
- [3165. Maximum Sum of Subsequence With Non-adjacent Elements](../../3001-3500/3165-maximum-sum-of-subsequence-with-non-adjacent-elements/)
- [1619. Mean of Array After Removing Some Elements](../../1501-2000/1619-mean-of-array-after-removing-some-elements/)
- [1748. Sum of Unique Elements](../../1501-2000/1748-sum-of-unique-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/subsequence-sum-after-capping-elements/)
