# LeetCode 1770: Maximum Score from Performing Multiplication Operations

**LeetCode Problem #1770 — Maximum Score from Performing Multiplication Operations**
Solve LeetCode Maximum Score from Performing Multiplication Operations using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Score from Performing Multiplication Operations |
| LeetCode | #1770 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two **0-indexed** integer arrays `nums` and `multipliers`** **of size `n` and `m` respectively, where `n >= m`.

You begin with a score of `0`. You want to perform **exactly** `m` operations. On the `i^th` operation (**0-indexed**) you will:

Choose one integer `x` from **either the start or the end **of the array `nums`. 
 Add `multipliers[i] * x` to your score.
 
 Note that `multipliers[0]` corresponds to the first operation, `multipliers[1]` to the second operation, and so on. 
 
 
 Remove `x` from `nums`.

Return *the **maximum** score after performing *`m` *operations.*

## Constraints
- `n == nums.length`
- `m == multipliers.length`
- `1 <= m <= 300`
- `m <= n <= 10^5`` `
- `-1000 <= nums[i], multipliers[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [1,2,3], multipliers = [3,2,1]`
- **Output:** `14`
- **Explanation:** An optimal solution is as follows:
- Choose from the end, [1,2,

### Example 2
- **Input:** `nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]`
- **Output:** `102`
- **Explanation:** An optimal solution is as follows:
- Choose from the start, [

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Score from Performing Multiplication Operations**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3], multipliers = [3,2,1]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `14`.
4. **Verification:** An optimal solution is as follows:
- Choose from the end, [1,2,

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
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        
        dp = [0] * (m + 1)
        
        for op in range(m - 1, -1, -1):
            mult = multipliers[op]
            for left in range(op + 1):
                right_idx = n - 1 - (op - left)
                pick_left = mult * nums[left] + dp[left + 1]
                pick_right = mult * nums[right_idx] + dp[left]
                dp[left] = pick_left if pick_left > pick_right else pick_right
                
        return dp[0]
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
- [3225. Maximum Score From Grid Operations](../../3001-3500/3225-maximum-score-from-grid-operations/)
- [1717. Maximum Score From Removing Substrings](../../1501-2000/1717-maximum-score-from-removing-substrings/)
- [1753. Maximum Score From Removing Stones](../../1501-2000/1753-maximum-score-from-removing-stones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/)
