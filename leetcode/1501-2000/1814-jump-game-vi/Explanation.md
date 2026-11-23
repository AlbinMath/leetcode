# LeetCode 1696: Jump Game VI

**LeetCode Problem #1696 — Jump Game VI**
Solve LeetCode Jump Game VI using JavaScript and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Jump Game VI |
| LeetCode | #1696 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` and an integer `k`.

You are initially standing at index `0`. In one move, you can jump at most `k` steps forward without going outside the boundaries of the array. That is, you can jump from index `i` to any index in the range `[i + 1, min(n - 1, i + k)]` **inclusive**.

You want to reach the last index of the array (index `n - 1`). Your **score** is the **sum** of all `nums[j]` for each index `j` you visited in the array.

Return *the **maximum score** you can get*.

## Constraints
- `1 <= nums.length, k <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [ 1 , -1 ,-2, 4 ,-7, 3 ], k = 2`
- **Output:** `7`
- **Explanation:** You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.

### Example 2
- **Input:** `nums = [ 10 ,-5,-2, 4 ,0, 3 ], k = 3`
- **Output:** `17`
- **Explanation:** You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.

### Example 3
- **Input:** `nums = [1,-5,-20,4,-1,3,-6,-3], k = 2`
- **Output:** `0`

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Jump Game VI**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [ 1 , -1 ,-2, 4 ,-7, 3 ], k = 2`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

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
var maxResult = function (nums, k) {
    const n = nums.length;
    const dp = new Array(n);
    const dq = new Array(n);
    let head = 0, tail = 0; // deque occupies dq[head..tail-1]

    dp[0] = nums[0];
    dq[tail++] = 0;

    for (let i = 1; i < n; i++) {
        while (dq[head] < i - k) head++;      // drop indices outside the window
        dp[i] = nums[i] + dp[dq[head]];
        while (head < tail && dp[dq[tail - 1]] <= dp[i]) tail--;
        dq[tail++] = i;
    }
    return dp[n - 1];
};
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [45. Jump Game II](../../0001-0500/0045-jump-game-ii/)
- [55. Jump Game](../../0001-0500/0055-jump-game/)
- [1306. Jump Game III](../../1001-1500/1428-jump-game-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/jump-game-vi/)
