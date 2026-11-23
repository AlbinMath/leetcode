# LeetCode 1033: Moving Stones Until Consecutive

**LeetCode Problem #1033 — Moving Stones Until Consecutive**
Solve LeetCode Moving Stones Until Consecutive using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Moving Stones Until Consecutive |
| LeetCode | #1033 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are three stones in different positions on the X-axis. You are given three integers `a`, `b`, and `c`, the positions of the stones.

In one move, you pick up a stone at an endpoint (i.e., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints. Formally, let's say the stones are currently at positions `x`, `y`, and `z` with `x < y < z`. You pick up the stone at either position `x` or position `z`, and move that stone to an integer position `k`, with `x < k < z` and `k != y`.

The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).

Return *an integer array *`answer`* of length *`2`* where*:

`answer[0]` *is the minimum number of moves you can play, and* 
 `answer[1]` *is the maximum number of moves you can play*.

## Constraints
- `1 <= a, b, c <= 100`
- `a`, `b`, and `c` have different values.

## Examples
### Example 1
- **Input:** `a = 1, b = 2, c = 5`
- **Output:** `[1,2]`
- **Explanation:** Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.

### Example 2
- **Input:** `a = 4, b = 3, c = 2`
- **Output:** `[0,0]`
- **Explanation:** We cannot make any moves.

### Example 3
- **Input:** `a = 3, b = 5, c = 1`
- **Output:** `[1,2]`
- **Explanation:** Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Moving Stones Until Consecutive**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `a = 1, b = 2, c = 5`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2]`.
4. **Verification:** Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.

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
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, y, z = sorted((a, b, c))
        if z - x == 2:
            return [0, 0]
        mn = 1 if (y - x <= 2 or z - y <= 2) else 2
        return [mn, z - x - 2]
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
- [1040. Moving Stones Until Consecutive II](../../1001-1500/1113-moving-stones-until-consecutive-ii/)
- [771. Jewels and Stones](../../0501-1000/0782-jewels-and-stones/)
- [947. Most Stones Removed with Same Row or Column](../../0501-1000/0984-most-stones-removed-with-same-row-or-column/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/moving-stones-until-consecutive/)
