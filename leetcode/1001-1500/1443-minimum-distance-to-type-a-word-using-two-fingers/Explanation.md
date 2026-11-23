# LeetCode 1320: Minimum Distance to Type a Word Using Two Fingers

**LeetCode Problem #1320 — Minimum Distance to Type a Word Using Two Fingers**
Solve LeetCode Minimum Distance to Type a Word Using Two Fingers using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Distance to Type a Word Using Two Fingers |
| LeetCode | #1320 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You have a keyboard layout as shown above in the **X-Y** plane, where each English uppercase letter is located at some coordinate.

For example, the letter `'A'` is located at coordinate `(0, 0)`, the letter `'B'` is located at coordinate `(0, 1)`, the letter `'P'` is located at coordinate `(2, 3)` and the letter `'Z'` is located at coordinate `(4, 1)`.

Given the string `word`, return *the minimum total **distance** to type such string using only two fingers*.

The **distance** between coordinates `(x_1, y_1)` and `(x_2, y_2)` is `|x_1 - x_2| + |y_1 - y_2|`.

**Note** that the initial positions of your two fingers are considered free so do not count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.

## Constraints
- `2 <= word.length <= 300`
- `word` consists of uppercase English letters.

## Examples
### Example 1
- **Input:** `word = "CAKE"`
- **Output:** `3`
- **Explanation:** Using two fingers, one optimal way to type "CAKE" is: 
Finger 1 on letter 'C' -> cost = 0 
Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
Finger 2 on letter 'K' -> cost = 0 
Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
Total distance = 3

### Example 2
- **Input:** `word = "HAPPY"`
- **Output:** `6`
- **Explanation:** Using two fingers, one optimal way to type "HAPPY" is:
Finger 1 on letter 'H' -> cost = 0
Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
Finger 2 on letter 'P' -> cost = 0
Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
Total distance = 6

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum Distance to Type a Word Using Two Fingers**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "CAKE"`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Using two fingers, one optimal way to type "CAKE" is: 
Finger 1 on letter 'C' -> cost = 0 
Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
Finger 2 on letter 'K' -> cost = 0 
Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
Total distance = 3

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
    def minimumDistance(self, word: str) -> int:
        def dist(a: int, b: int) -> int:
            if a == 26 or b == 26:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        INF = float('inf')
        # dp[o]: min cost, last-typed finger on previous letter, other finger on o (26 = unplaced)
        dp = [INF] * 27
        dp[26] = 0
        prev = ord(word[0]) - 65

        for ch in word[1:]:
            cur = ord(ch) - 65
            ndp = [INF] * 27
            for o in range(27):
                if dp[o] == INF:
                    continue
                # same finger moves prev -> cur
                ndp[o] = min(ndp[o], dp[o] + dist(prev, cur))
                # other finger moves o -> cur; the finger on prev becomes "other"
                ndp[prev] = min(ndp[prev], dp[o] + dist(o, cur))
            dp = ndp
            prev = cur

        return min(dp)
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
- [1974. Minimum Time to Type Word Using Special Typewriter](../../2001-2500/2088-minimum-time-to-type-word-using-special-typewriter/)
- [3014. Minimum Number of Pushes to Type Word I](../../3001-3500/3275-minimum-number-of-pushes-to-type-word-i/)
- [3016. Minimum Number of Pushes to Type Word II](../../3001-3500/3276-minimum-number-of-pushes-to-type-word-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/)
