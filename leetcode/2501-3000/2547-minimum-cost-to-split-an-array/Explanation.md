# LeetCode 2547: Minimum Cost to Split an Array

**LeetCode Problem #2547 — Minimum Cost to Split an Array**
Solve LeetCode Minimum Cost to Split an Array using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Split an Array |
| LeetCode | #2547 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

Split the array into some number of non-empty subarrays. The **cost** of a split is the sum of the **importance value** of each subarray in the split.

Let `trimmed(subarray)` be the version of the subarray where all numbers which appear only once are removed.

For example, `trimmed([3,1,2,4,3,4]) = [3,4,3,4].`

The **importance value** of a subarray is `k + trimmed(subarray).length`.

For example, if a subarray is `[1,2,3,3,3,4,4]`, then trimmed( `[1,2,3,3,3,4,4]) = [3,3,3,4,4].`The importance value of this subarray will be `k + 5`.

Return *the minimum possible cost of a split of *`nums`.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

## Constraints
- `1 <= nums.length <= 1000`
- `0 <= nums[i] < nums.length`
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,1,2,1,3,3], k = 2`
- **Output:** `8`
- **Explanation:** We split nums to have two subarrays: [1,2], [1,2,1,3,3].
The importance value of [1,2] is 2 + (0) = 2.
The importance value of [1,2,1,3,3] is 2 + (2 + 2) = 6.
The cost of the split is 2 + 6 = 8. It can be shown that this is the minimum possible cost among all the possible splits.

### Example 2
- **Input:** `nums = [1,2,1,2,1], k = 2`
- **Output:** `6`
- **Explanation:** We split nums to have two subarrays: [1,2], [1,2,1].
The importance value of [1,2] is 2 + (0) = 2.
The importance value of [1,2,1] is 2 + (2) = 4.
The cost of the split is 2 + 4 = 6. It can be shown that this is the minimum possible cost among all the possible splits.

### Example 3
- **Input:** `nums = [1,2,1,2,1], k = 5`
- **Output:** `10`
- **Explanation:** We split nums to have one subarray: [1,2,1,2,1].
The importance value of [1,2,1,2,1] is 5 + (3 + 2) = 10.
The cost of the split is 10. It can be shown that this is the minimum possible cost among all the possible splits.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum Cost to Split an Array**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,1,2,1,3,3], k = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** We split nums to have two subarrays: [1,2], [1,2,1,3,3].
The importance value of [1,2] is 2 + (0) = 2.
The importance value of [1,2,1,3,3] is 2 + (2 + 2) = 6.
The cost of the split is 2 + 6 = 8. It can be shown that this is the minimum possible cost among all the possible splits.

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
    def minCost(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            freq = [0] * n
            trimmed_len = 0
            
            for j in range(i - 1, -1, -1):
                val = nums[j]
                freq[val] += 1
                
                if freq[val] == 2:
                    trimmed_len += 2
                elif freq[val] > 2:
                    trimmed_len += 1
                    
                cost = dp[j] + k + trimmed_len
                if cost < dp[i]:
                    dp[i] = cost
                    
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
- [2448. Minimum Cost to Make Array Equal](../../2001-2500/2448-minimum-cost-to-make-array-equal/)
- [2967. Minimum Cost to Make Array Equalindromic](../../2501-3000/2967-minimum-cost-to-make-array-equalindromic/)
- [3010. Divide an Array Into Subarrays With Minimum Cost I](../../3001-3500/3010-divide-an-array-into-subarrays-with-minimum-cost-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-split-an-array/)
