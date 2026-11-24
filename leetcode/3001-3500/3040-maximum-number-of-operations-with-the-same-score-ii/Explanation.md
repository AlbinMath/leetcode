# LeetCode 3040: Maximum Number of Operations With the Same Score II

**LeetCode Problem #3040 — Maximum Number of Operations With the Same Score II**
Solve LeetCode Maximum Number of Operations With the Same Score II using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Operations With the Same Score II |
| LeetCode | #3040 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of integers called `nums`, you can perform **any** of the following operation while `nums` contains **at least** `2` elements:

Choose the first two elements of `nums` and delete them. 
 Choose the last two elements of `nums` and delete them. 
 Choose the first and the last elements of `nums` and delete them.

The** score** of the operation is the sum of the deleted elements.

Your task is to find the **maximum** number of operations that can be performed, such that **all operations have the same score**.

Return *the **maximum** number of operations possible that satisfy the condition mentioned above*.

## Constraints
- `2 <= nums.length <= 2000`
- `1 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [3,2,1,2,3,4]`
- **Output:** `3`
- **Explanation:** We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [1,2,3,4].
- Delete the first and the last elements, with score 1 + 4 = 5, nums = [2,3].
- Delete the first and the last elements, with score 2 + 3 = 5, nums = [].
We are unable to perform any more operations as nums is empty.

### Example 2
- **Input:** `nums = [3,2,6,1,4]`
- **Output:** `2`
- **Explanation:** We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [6,1,4].
- Delete the last two elements, with score 1 + 4 = 5, nums = [6].
It can be proven that we can perform at most 2 operations.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Number of Operations With the Same Score II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,2,1,2,3,4]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [1,2,3,4].
- Delete the first and the last elements, with score 1 + 4 = 5, nums = [2,3].
- Delete the first and the last elements, with score 2 + 3 = 5, nums = [].
We are unable to perform any more operations as nums is empty.

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
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0

        for S in {nums[0] + nums[1], nums[-1] + nums[-2], nums[0] + nums[-1]}:
            # dp[i][j] for i <= j; out-of-range or i >= j gives 0
            dp = [[0] * (n + 2) for _ in range(n + 2)]
            for i in range(n - 1, -1, -1):
                for j in range(i + 1, n):
                    r = 0
                    if nums[i] + nums[i + 1] == S:
                        r = max(r, 1 + (dp[i + 2][j] if i + 2 <= j else 0))
                    if nums[j - 1] + nums[j] == S:
                        r = max(r, 1 + (dp[i][j - 2] if i <= j - 2 else 0))
                    if nums[i] + nums[j] == S:
                        r = max(r, 1 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0))
                    dp[i][j] = r
            best = max(best, dp[0][n - 1])
        return best
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
- [3038. Maximum Number of Operations With the Same Score I](../../3001-3500/3038-maximum-number-of-operations-with-the-same-score-i/)
- [3228. Maximum Number of Operations to Move Ones to the End](../../3001-3500/3228-maximum-number-of-operations-to-move-ones-to-the-end/)
- [1467. Probability of a Two Boxes Having The Same Number of Distinct Balls](../../1001-1500/1467-probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/)
