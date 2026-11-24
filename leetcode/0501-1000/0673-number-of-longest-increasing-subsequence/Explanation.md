# LeetCode 673: Number of Longest Increasing Subsequence

**LeetCode Problem #673 — Number of Longest Increasing Subsequence**
Solve LeetCode Number of Longest Increasing Subsequence using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Longest Increasing Subsequence |
| LeetCode | #673 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer array `nums`, return *the number of longest increasing subsequences.*

**Notice** that the sequence has to be **strictly** increasing.

## Constraints
- `1 <= nums.length <= 2000`
- `-10^6 <= nums[i] <= 10^6`
- The answer is guaranteed to fit inside a 32-bit integer.

## Examples
### Example 1
- **Input:** `nums = [1,3,5,4,7]`
- **Output:** `2`
- **Explanation:** The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

### Example 2
- **Input:** `nums = [2,2,2,2,2]`
- **Output:** `5`
- **Explanation:** The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Number of Longest Increasing Subsequence**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,5,4,7]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

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
var findNumberOfLIS = function(nums) {
    const n = nums.length;

    const length = new Array(n).fill(1);
    const count = new Array(n).fill(1);

    let maxLength = 1;
    let result = 0;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                if (length[j] + 1 > length[i]) {
                    length[i] = length[j] + 1;
                    count[i] = count[j];
                } else if (length[j] + 1 === length[i]) {
                    count[i] += count[j];
                }
            }
        }

        maxLength = Math.max(maxLength, length[i]);
    }

    for (let i = 0; i < n; i++) {
        if (length[i] === maxLength) {
            result += count[i];
        }
    }

    return result;
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
- [300. Longest Increasing Subsequence](../../0001-0500/0300-longest-increasing-subsequence/)
- [674. Longest Continuous Increasing Subsequence](../../0501-1000/0674-longest-continuous-increasing-subsequence/)
- [2407. Longest Increasing Subsequence II](../../2001-2500/2407-longest-increasing-subsequence-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)
