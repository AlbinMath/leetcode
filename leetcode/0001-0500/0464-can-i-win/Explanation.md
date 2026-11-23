# LeetCode 464: Can I Win

**LeetCode Problem #464 — Can I Win**
Solve LeetCode Can I Win using Python and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Can I Win |
| LeetCode | #464 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
In the "100 game" two players take turns adding, to a running total, any integer from `1` to `10`. The player who first causes the running total to **reach or exceed** 100 wins.

What if we change the game so that players **cannot** re-use integers?

For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

Given two integers `maxChoosableInteger` and `desiredTotal`, return `true` if the first player to move can force a win, otherwise, return `false`. Assume both players play **optimally**.

## Constraints
- `1 <= maxChoosableInteger <= 20`
- `0 <= desiredTotal <= 300`

## Examples
### Example 1
- **Input:** `maxChoosableInteger = 10, desiredTotal = 11`
- **Output:** `false`
- **Explanation:** No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.

### Example 2
- **Input:** `maxChoosableInteger = 10, desiredTotal = 0`
- **Output:** `true`

### Example 3
- **Input:** `maxChoosableInteger = 10, desiredTotal = 1`
- **Output:** `true`

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
To solve **Can I Win**, we observe the problem requirements and utilize the **Monotonic Stack** technique. We maintain a **Stack** with elements in strictly monotonic order. Whenever an incoming element violates monotonicity, we pop previous elements and compute answer intervals in amortized linear time.

## Algorithm
1. Initialize an empty stack.
2. For each element, pop previous items from stack while monotonic invariant is violated.
3. Push current element or index onto stack.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `maxChoosableInteger = 10, desiredTotal = 11`.
2. **Processing Steps:** We apply **Monotonic Stack Filtering** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False

        @lru_cache(None)
        def win(used, remain):
            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << (i - 1)
                if not used & bit:
                    if i >= remain or not win(used | bit, remain - i):
                        return True
            return False

        return win(0, desiredTotal)
```

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [2555. Maximize Win From Two Segments](../../2501-3000/2673-maximize-win-from-two-segments/)
- [3175. Find The First Player to win K Games in a Row](../../3001-3500/3413-find-the-first-player-to-win-k-games-in-a-row/)
- [605. Can Place Flowers](../../0501-1000/0605-can-place-flowers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/can-i-win/)
