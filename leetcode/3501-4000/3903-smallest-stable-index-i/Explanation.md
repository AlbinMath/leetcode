# LeetCode 3903: Smallest Stable Index I

**LeetCode Problem #3903 — Smallest Stable Index I**
Solve LeetCode Smallest Stable Index I using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Stable Index I |
| LeetCode | #3903 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of length `n` and an integer `k`.

For each index `i`, define its **instability score** as `max(nums[0..i]) - min(nums[i..n - 1])`.

In other words:

`max(nums[0..i])` is the **largest** value among the elements from index 0 to index `i`. 
 `min(nums[i..n - 1])` is the **smallest** value among the elements from index `i` to index `n - 1`.

An index `i` is called **stable** if its instability score is **less than or equal to** `k`.

Return the **smallest** stable index. If no such index exists, return -1.

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 10^9`
- `0 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [5,0,1,4], k = 3`
- **Output:** `3`
- **Explanation:** At index 0: The maximum in `[5]` is 5, and the minimum in `[5, 0, 1, 4]` is 0, so the instability score is `5 - 0 = 5`. 
 At index 1: The maximum in `[5, 0]` is 5, and the minimum in `[0, 1, 4]` is 0, so the instability score is `5 - 0 = 5`. 
 At index 2: The maximum in `[5, 0, 1]` is 5, and the minimum in `[1, 4]` is 1, so the instability score is `5 - 1 = 4`. 
 At index 3: The maximum in `[5, 0, 1, 4]` is 5, and the minimum in `[4]` is 4, so the instability score is `5 - 4 = 1`. 
 This is the first index with an instability score less than or equal to `k = 3`. Thus, the answer is 3.

### Example 2
- **Input:** `nums = [3,2,1], k = 1`
- **Output:** `-1`
- **Explanation:** At index 0, the instability score is `3 - 1 = 2`. 
 At index 1, the instability score is `3 - 1 = 2`. 
 At index 2, the instability score is `3 - 1 = 2`. 
 None of these values is less than or equal to `k = 1`, so the answer is -1.

### Example 3
- **Input:** `nums = [0], k = 0`
- **Output:** `0`
- **Explanation:** At index 0, the instability score is `0 - 0 = 0`, which is less than or equal to `k = 0`. Therefore, the answer is 0.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Smallest Stable Index I**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,0,1,4], k = 3`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** At index 0: The maximum in `[5]` is 5, and the minimum in `[5, 0, 1, 4]` is 0, so the instability score is `5 - 0 = 5`. 
 At index 1: The maximum in `[5, 0]` is 5, and the minimum in `[0, 1, 4]` is 0, so the instability score is `5 - 0 = 5`. 
 At index 2: The maximum in `[5, 0, 1]` is 5, and the minimum in `[1, 4]` is 1, so the instability score is `5 - 1 = 4`. 
 At index 3: The maximum in `[5, 0, 1, 4]` is 5, and the minimum in `[4]` is 4, so the instability score is `5 - 4 = 1`. 
 This is the first index with an instability score less than or equal to `k = 3`. Thus, the answer is 3.

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
var firstStableIndex = function(nums, k) {
    let n = nums.length;

    // Suffix minimums
    let suffixMin = new Array(n);
    suffixMin[n - 1] = nums[n - 1];

    for (let i = n - 2; i >= 0; i--) {
        suffixMin[i] = Math.min(nums[i], suffixMin[i + 1]);
    }

    // Prefix maximum
    let prefixMax = nums[0];

    for (let i = 0; i < n; i++) {
        prefixMax = Math.max(prefixMax, nums[i]);

        let instability = prefixMax - suffixMin[i];

        if (instability <= k) {
            return i;
        }
    }

    return -1;
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
- [3904. Smallest Stable Index II](../../3501-4000/3904-smallest-stable-index-ii/)
- [3550. Smallest Index With Digit Sum Equal to Index](../../3501-4000/3550-smallest-index-with-digit-sum-equal-to-index/)
- [3748. Count Stable Subarrays](../../3501-4000/3748-count-stable-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-stable-index-i/)
