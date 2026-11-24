# LeetCode 818: Race Car

**LeetCode Problem #818 — Race Car**
Solve LeetCode Race Car using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Race Car |
| LeetCode | #818 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Your car starts at position `0` and speed `+1` on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions `'A'` (accelerate) and `'R'` (reverse):

When you get an instruction `'A'`, your car does the following:

`position += speed` 
 `speed *= 2` 
 
 
 When you get an instruction `'R'`, your car does the following:
 
 If your speed is positive then `speed = -1` 
 otherwise `speed = 1` 
 
 Your position stays the same.

For example, after commands `"AAR"`, your car goes to positions `0 --> 1 --> 3 --> 3`, and your speed goes to `1 --> 2 --> 4 --> -1`.

Given a target position `target`, return *the length of the shortest sequence of instructions to get there*.

## Constraints
- `1 <= target <= 10^4`

## Examples
### Example 1
- **Input:** `target = 3`
- **Output:** `2`
- **Explanation:** The shortest instruction sequence is "AA".
Your position goes from 0 --> 1 --> 3.

### Example 2
- **Input:** `target = 6`
- **Output:** `5`
- **Explanation:** The shortest instruction sequence is "AAARA".
Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Race Car**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `target = 3`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The shortest instruction sequence is "AA".
Your position goes from 0 --> 1 --> 3.

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
    def racecar(self, target: int) -> int:
        dp = [0] * (target + 1)
        for t in range(1, target + 1):
            n = t.bit_length()
            if (1 << n) - 1 == t:
                dp[t] = n
                continue
            # overshoot, then reverse
            dp[t] = n + 1 + dp[(1 << n) - 1 - t]
            # undershoot at n-1 accelerations, reverse, back up m, reverse again
            for m in range(n - 1):
                dist = t - ((1 << (n - 1)) - 1) + ((1 << m) - 1)
                dp[t] = min(dp[t], (n - 1) + 1 + m + 1 + dp[dist])
        return dp[target]
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
- [853. Car Fleet](../../0501-1000/0853-car-fleet/)
- [1094. Car Pooling](../../1001-1500/1094-car-pooling/)
- [1776. Car Fleet II](../../1501-2000/1776-car-fleet-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/race-car/)
