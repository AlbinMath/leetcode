# LeetCode 1262: Greatest Sum Divisible by Three

**LeetCode Problem #1262 — Greatest Sum Divisible by Three**
Solve LeetCode Greatest Sum Divisible by Three using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Greatest Sum Divisible by Three |
| LeetCode | #1262 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer array `nums`, return *the **maximum possible sum **of elements of the array such that it is divisible by three*.

## Constraints
- `1 <= nums.length <= 4 * 10^4`
- `1 <= nums[i] <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [3,6,5,1,8]`
- **Output:** `18`
- **Explanation:** Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

### Example 2
- **Input:** `nums = [4]`
- **Output:** `0`
- **Explanation:** Since 4 is not divisible by 3, do not pick any number.

### Example 3
- **Input:** `nums = [1,2,3,4,4]`
- **Output:** `12`
- **Explanation:** Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Greatest Sum Divisible by Three**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,6,5,1,8]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `18`.
4. **Verification:** Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

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
    def maxSumDivThree(self, nums: List[int]) -> int:
        NEG = float('-inf')
        dp = [0, NEG, NEG]
        for x in nums:
            new = dp[:]
            for r in range(3):
                if dp[r] != NEG:
                    nr = (r + x) % 3
                    new[nr] = max(new[nr], dp[r] + x)
            dp = new
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
- [3780. Maximum Sum of Three Numbers Divisible by Three](../../3501-4000/3780-maximum-sum-of-three-numbers-divisible-by-three/)
- [1013. Partition Array Into Three Parts With Equal Sum](../../1001-1500/1013-partition-array-into-three-parts-with-equal-sum/)
- [1780. Check if Number is a Sum of Powers of Three](../../1501-2000/1780-check-if-number-is-a-sum-of-powers-of-three/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/greatest-sum-divisible-by-three/)
