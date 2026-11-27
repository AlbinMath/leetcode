# LeetCode 2172: Maximum AND Sum of Array

**LeetCode Problem #2172 — Maximum AND Sum of Array**
Solve LeetCode Maximum AND Sum of Array using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum AND Sum of Array |
| LeetCode | #2172 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of length `n` and an integer `numSlots` such that `2 * numSlots >= n`. There are `numSlots` slots numbered from `1` to `numSlots`.

You have to place all `n` integers into the slots such that each slot contains at **most** two numbers. The **AND sum** of a given placement is the sum of the **bitwise** `AND` of every number with its respective slot number.

For example, the **AND sum** of placing the numbers `[1, 3]` into slot `1` and `[4, 6]` into slot `2` is equal to `(1 AND 1 ) + (3 AND 1 ) + (4 AND 2 ) + (6 AND 2 ) = 1 + 1 + 0 + 2 = 4`.

Return *the maximum possible **AND sum** of *`nums`* given *`numSlots`* slots.*

## Constraints
- `n == nums.length`
- `1 <= numSlots <= 9`
- `1 <= n <= 2 * numSlots`
- `1 <= nums[i] <= 15`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5,6], numSlots = 3`
- **Output:** `9`
- **Explanation:** One possible placement is [1, 4] into slot 1 , [2, 6] into slot 2 , and [3, 5] into slot 3 . 
This gives the maximum AND sum of (1 AND 1 ) + (4 AND 1 ) + (2 AND 2 ) + (6 AND 2 ) + (3 AND 3 ) + (5 AND 3 ) = 1 + 0 + 2 + 2 + 3 + 1 = 9.

### Example 2
- **Input:** `nums = [1,3,10,4,7,1], numSlots = 9`
- **Output:** `24`
- **Explanation:** One possible placement is [1, 1] into slot 1 , [3] into slot 3 , [4] into slot 4 , [7] into slot 7 , and [10] into slot 9 .
This gives the maximum AND sum of (1 AND 1 ) + (1 AND 1 ) + (3 AND 3 ) + (4 AND 4 ) + (7 AND 7 ) + (10 AND 9 ) = 1 + 1 + 3 + 4 + 7 + 8 = 24.
Note that slots 2, 5, 6, and 8 are empty which is permitted.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum AND Sum of Array**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5,6], numSlots = 3`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** One possible placement is [1, 4] into slot 1 , [2, 6] into slot 2 , and [3, 5] into slot 3 . 
This gives the maximum AND sum of (1 AND 1 ) + (4 AND 1 ) + (2 AND 2 ) + (6 AND 2 ) + (3 AND 3 ) + (5 AND 3 ) = 1 + 0 + 2 + 2 + 3 + 1 = 9.

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
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        seats = 2 * numSlots
        dp = [-1] * (1 << seats)
        dp[0] = 0
        ans = 0
        for mask in range(1 << seats):
            if dp[mask] < 0:
                continue
            i = bin(mask).count("1")  # next number to place
            if i == n:
                ans = max(ans, dp[mask])
                continue
            for s in range(seats):
                if not mask & (1 << s):
                    slot = s // 2 + 1
                    nxt = mask | (1 << s)
                    val = dp[mask] + (nums[i] & slot)
                    if val > dp[nxt]:
                        dp[nxt] = val
        return ans
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
- [1043. Partition Array for Maximum Sum](../../1001-1500/1043-partition-array-for-maximum-sum/)
- [1877. Minimize Maximum Pair Sum in Array](../../1501-2000/1877-minimize-maximum-pair-sum-in-array/)
- [167. Two Sum II - Input Array Is Sorted](../../0001-0500/0167-two-sum-ii-input-array-is-sorted/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-and-sum-of-array/)
