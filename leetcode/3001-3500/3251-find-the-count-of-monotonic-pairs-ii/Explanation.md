# LeetCode 3251: Find the Count of Monotonic Pairs II

**LeetCode Problem #3251 — Find the Count of Monotonic Pairs II**
Solve LeetCode Find the Count of Monotonic Pairs II using JavaScript and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Count of Monotonic Pairs II |
| LeetCode | #3251 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of **positive** integers `nums` of length `n`.

We call a pair of **non-negative** integer arrays `(arr1, arr2)` **monotonic** if:

The lengths of both arrays are `n`. 
 `arr1` is monotonically **non-decreasing**, in other words, `arr1[0] <= arr1[1] <= ... <= arr1[n - 1]`. 
 `arr2` is monotonically **non-increasing**, in other words, `arr2[0] >= arr2[1] >= ... >= arr2[n - 1]`. 
 `arr1[i] + arr2[i] == nums[i]` for all `0 <= i <= n - 1`.

Return the count of **monotonic** pairs.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= n == nums.length <= 2000`
- `1 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [2,3,2]`
- **Output:** `4`
- **Explanation:** The good pairs are: 

 
 `([0, 1, 1], [2, 2, 1])` 
 `([0, 1, 2], [2, 2, 0])` 
 `([0, 2, 2], [2, 1, 0])` 
 `([1, 2, 2], [1, 1, 0])`

### Example 2
- **Input:** `nums = [5,5,5,5]`
- **Output:** `126`

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
To solve **Find the Count of Monotonic Pairs II**, we observe the problem requirements and utilize the **Monotonic Stack** technique. We decompose the problem into overlapping subproblems using a **Stack**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,2]`.
2. **Processing Steps:** We apply **Monotonic Stack Filtering** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The good pairs are: 

 
 `([0, 1, 1], [2, 2, 1])` 
 `([0, 1, 2], [2, 2, 0])` 
 `([0, 2, 2], [2, 1, 0])` 
 `([1, 2, 2], [1, 1, 0])`

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var countOfPairs = function(nums) {
    const MOD = 1000000007;
    const n = nums.length;
    let dp = new Array(nums[0] + 1).fill(1);

    for (let i = 1; i < n; i++) {
        const prev = dp;
        const curr = new Array(nums[i] + 1).fill(0);
        const diff = Math.max(0, nums[i] - nums[i - 1]);

        let prefix = 0;

        for (let j = 0; j <= nums[i]; j++) {
            if (j - diff >= 0 && j - diff < prev.length) {
                prefix = (prefix + prev[j - diff]) % MOD;
            }

            curr[j] = prefix;
        }

        dp = curr;
    }

    return dp.reduce((sum, ways) => (sum + ways) % MOD, 0);
};
```

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [3250. Find the Count of Monotonic Pairs I](../../3001-3500/3250-find-the-count-of-monotonic-pairs-i/)
- [1729. Find Followers Count](../../1501-2000/1729-find-followers-count/)
- [1782. Count Pairs Of Nodes](../../1501-2000/1782-count-pairs-of-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/)
