# LeetCode 1900: The Earliest and Latest Rounds Where Players Compete

**LeetCode Problem #1900 — The Earliest and Latest Rounds Where Players Compete**
Solve LeetCode The Earliest and Latest Rounds Where Players Compete using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The Earliest and Latest Rounds Where Players Compete |
| LeetCode | #1900 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is a tournament where `n` players are participating. The players are standing in a single row and are numbered from `1` to `n` based on their **initial** standing position (player `1` is the first player in the row, player `2` is the second player in the row, etc.).

The tournament consists of multiple rounds (starting from round number `1`). In each round, the `i^th` player from the front of the row competes against the `i^th` player from the end of the row, and the winner advances to the next round. When the number of players is odd for the current round, the player in the middle automatically advances to the next round.

For example, if the row consists of players `1, 2, 4, 6, 7`

Player `1` competes against player `7`. 
 Player `2` competes against player `6`. 
 Player `4` automatically advances to the next round.

After each round is over, the winners are lined back up in the row based on the **original ordering** assigned to them initially (ascending order).

The players numbered `firstPlayer` and `secondPlayer` are the best in the tournament. They can win against any other player before they compete against each other. If any two other players compete against each other, either of them might win, and thus you may **choose** the outcome of this round.

Given the integers `n`, `firstPlayer`, and `secondPlayer`, return *an integer array containing two values, the **earliest** possible round number and the **latest** possible round number in which these two players will compete against each other, respectively*.

## Constraints
- `2 <= n <= 28`
- `1 <= firstPlayer < secondPlayer <= n`

## Examples
### Example 1
- **Input:** `n = 11, firstPlayer = 2, secondPlayer = 4`
- **Output:** `[3,4]`
- **Explanation:** One possible scenario which leads to the earliest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 2, 3, 4, 5, 6, 11
Third round: 2, 3, 4
One possible scenario which leads to the latest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 1, 2, 3, 4, 5, 6
Third round: 1, 2, 4
Fourth round: 2, 4

### Example 2
- **Input:** `n = 5, firstPlayer = 1, secondPlayer = 5`
- **Output:** `[1,1]`
- **Explanation:** The players numbered 1 and 5 compete in the first round.
There is no way to make them compete in any other round.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **The Earliest and Latest Rounds Where Players Compete**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 11, firstPlayer = 2, secondPlayer = 4`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,4]`.
4. **Verification:** One possible scenario which leads to the earliest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 2, 3, 4, 5, 6, 11
Third round: 2, 3, 4
One possible scenario which leads to the latest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 1, 2, 3, 4, 5, 6
Third round: 1, 2, 4
Fourth round: 2, 4

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
from functools import lru_cache
from typing import List

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache(maxsize=None)
        def go(n, a, b):
            if a + b == n + 1:
                return (1, 1)
            if a + b > n + 1:
                a, b = n + 1 - b, n + 1 - a
            m = (n + 1) // 2
            lo, hi = float('inf'), 0
            if 2 * b <= n + 1:
                for x in range(a):
                    na = x + 1
                    for y in range(b - a):
                        nb = na + y + 1
                        r = go(m, na, nb)
                        lo = min(lo, r[0] + 1)
                        hi = max(hi, r[1] + 1)
            else:
                c = n + 1 - b
                add = (b - c) // 2          # (k + 1) // 2 with k = b - c - 1
                for x in range(a):
                    na = x + 1
                    for y in range(c - a):
                        nb = na + y + add + 1
                        r = go(m, na, nb)
                        lo = min(lo, r[0] + 1)
                        hi = max(hi, r[1] + 1)
            return (lo, hi)

        a, b = sorted((firstPlayer, secondPlayer))
        return list(go(n, a, b))
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
- [1904. The Number of Full Rounds You Have Played](../../1501-2000/1904-the-number-of-full-rounds-you-have-played/)
- [2244. Minimum Rounds to Complete All Tasks](../../2001-2500/2244-minimum-rounds-to-complete-all-tasks/)
- [1562. Find Latest Group of Size M](../../1501-2000/1562-find-latest-group-of-size-m/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/)
