# LeetCode 2945: Find Maximum Non-decreasing Array Length

**LeetCode Problem #2945 — Find Maximum Non-decreasing Array Length**
Solve LeetCode Find Maximum Non-decreasing Array Length using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Maximum Non-decreasing Array Length |
| LeetCode | #2945 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** integer array `nums`.

You can perform any number of operations, where each operation involves selecting a **subarray** of the array and replacing it with the **sum** of its elements. For example, if the given array is `[1,3,5,6]` and you select subarray `[3,5]` the array will convert to `[1,8,6]`.

Return *the ****maximum**** length of a ****non-decreasing**** array that can be made after applying operations.*

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [5,2,2]`
- **Output:** `1`
- **Explanation:** This array with length 3 is not non-decreasing.
We have two ways to make the array length two.
First, choosing subarray [2,2] converts the array to [5,4].
Second, choosing subarray [5,2] converts the array to [7,2].
In these two ways the array is not non-decreasing.
And if we choose subarray [5,2,2] and replace it with [9] it becomes non-decreasing. 
So the answer is 1.

### Example 2
- **Input:** `nums = [1,2,3,4]`
- **Output:** `4`
- **Explanation:** The array is non-decreasing. So the answer is 4.

### Example 3
- **Input:** `nums = [4,3,2,6]`
- **Output:** `3`
- **Explanation:** Replacing [3,2] with [5] converts the given array to [4,5,6] that is non-decreasing.
Because the given array is not non-decreasing, the maximum possible answer is 3.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Find Maximum Non-decreasing Array Length**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,2,2]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** This array with length 3 is not non-decreasing.
We have two ways to make the array length two.
First, choosing subarray [2,2] converts the array to [5,4].
Second, choosing subarray [5,2] converts the array to [7,2].
In these two ways the array is not non-decreasing.
And if we choose subarray [5,2,2] and replace it with [9] it becomes non-decreasing. 
So the answer is 1.

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
 * @return {number}
 */
var findMaximumLength = function (nums) {
    const n = nums.length;
    const P = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) P[i + 1] = P[i] + nums[i];

    const dp = new Array(n + 1).fill(0);
    const key = new Array(n + 1).fill(0); // key[j] = P[j] + last[j]
    const dq = new Array(n + 1);
    let head = 0, tail = 0;
    dq[tail++] = 0;

    for (let i = 1; i <= n; i++) {
        while (tail - head >= 2 && key[dq[head + 1]] <= P[i]) head++;
        const j = dq[head];
        dp[i] = dp[j] + 1;
        key[i] = P[i] + (P[i] - P[j]);
        while (head < tail && key[dq[tail - 1]] >= key[i]) tail--;
        dq[tail++] = i;
    }
    return dp[n];
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
- [3755. Find Maximum Balanced XOR Subarray Length](../../3501-4000/3755-find-maximum-balanced-xor-subarray-length/)
- [3287. Find the Maximum Sequence Value of Array](../../3001-3500/3287-find-the-maximum-sequence-value-of-array/)
- [3334. Find the Maximum Factor Score of Array](../../3001-3500/3334-find-the-maximum-factor-score-of-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-maximum-non-decreasing-array-length/)
