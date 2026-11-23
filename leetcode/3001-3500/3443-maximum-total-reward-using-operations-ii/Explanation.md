# LeetCode 3181: Maximum Total Reward Using Operations II

**LeetCode Problem #3181 — Maximum Total Reward Using Operations II**
Solve LeetCode Maximum Total Reward Using Operations II using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Total Reward Using Operations II |
| LeetCode | #3181 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `rewardValues` of length `n`, representing the values of rewards.

Initially, your total reward `x` is 0, and all indices are **unmarked**. You are allowed to perform the following operation **any** number of times:

Choose an **unmarked** index `i` from the range `[0, n - 1]`. 
 If `rewardValues[i]` is **greater** than your current total reward `x`, then add `rewardValues[i]` to `x` (i.e., `x = x + rewardValues[i]`), and **mark** the index `i`.

Return an integer denoting the **maximum ***total reward* you can collect by performing the operations optimally.

## Constraints
- `1 <= rewardValues.length <= 5 * 10^4`
- `1 <= rewardValues[i] <= 5 * 10^4`

## Examples
### Example 1
- **Input:** `rewardValues = [1,1,3,3]`
- **Output:** `4`
- **Explanation:** During the operations, we can choose to mark the indices 0 and 2 in order, and the total reward will be 4, which is the maximum.

### Example 2
- **Input:** `rewardValues = [1,6,4,3,2]`
- **Output:** `11`
- **Explanation:** Mark the indices 0, 2, and 1 in order. The total reward will then be 11, which is the maximum.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Total Reward Using Operations II**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `rewardValues = [1,1,3,3]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** During the operations, we can choose to mark the indices 0 and 2 in order, and the total reward will be 4, which is the maximum.

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
class Solution(object):
    def maxTotalReward(self, rewardValues):
        dp = 1  # total reward 0 is reachable
        for v in sorted(set(rewardValues)):
            dp |= (dp & ((1 << v) - 1)) << v
        return dp.bit_length() - 1
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
- [3180. Maximum Total Reward Using Operations I](../../3001-3500/3442-maximum-total-reward-using-operations-i/)
- [2234. Maximum Total Beauty of the Gardens](../../2001-2500/2330-maximum-total-beauty-of-the-gardens/)
- [2285. Maximum Total Importance of Roads](../../2001-2500/2379-maximum-total-importance-of-roads/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-total-reward-using-operations-ii/)
