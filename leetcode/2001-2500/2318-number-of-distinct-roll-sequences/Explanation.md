# LeetCode 2318: Number of Distinct Roll Sequences

**LeetCode Problem #2318 — Number of Distinct Roll Sequences**
Solve LeetCode Number of Distinct Roll Sequences using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Distinct Roll Sequences |
| LeetCode | #2318 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n`. You roll a fair 6-sided dice `n` times. Determine the total number of **distinct** sequences of rolls possible such that the following conditions are satisfied:

The **greatest common divisor** of any **adjacent** values in the sequence is equal to `1`. 
 There is **at least** a gap of `2` rolls between **equal** valued rolls. More formally, if the value of the `i^th` roll is **equal** to the value of the `j^th` roll, then `abs(i - j) > 2`.

Return *the** total number** of distinct sequences possible*. Since the answer may be very large, return it **modulo** `10^9 + 7`.

Two sequences are considered distinct if at least one element is different.

## Constraints
- `1 <= n <= 10^4`

## Examples
### Example 1
- **Input:** `n = 4`
- **Output:** `184`
- **Explanation:** Some of the possible sequences are (1, 2, 3, 4), (6, 1, 2, 3), (1, 2, 3, 1), etc.
Some invalid sequences are (1, 2, 1, 3), (1, 2, 3, 6).
(1, 2, 1, 3) is invalid since the first and third roll have an equal value and abs(1 - 3) = 2 (i and j are 1-indexed).
(1, 2, 3, 6) is invalid since the greatest common divisor of 3 and 6 = 3.
There are a total of 184 distinct sequences possible, so we return 184.

### Example 2
- **Input:** `n = 2`
- **Output:** `22`
- **Explanation:** Some of the possible sequences are (1, 2), (2, 1), (3, 2).
Some invalid sequences are (3, 6), (2, 4) since the greatest common divisor is not equal to 1.
There are a total of 22 distinct sequences possible, so we return 22.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Number of Distinct Roll Sequences**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `184`.
4. **Verification:** Some of the possible sequences are (1, 2, 3, 4), (6, 1, 2, 3), (1, 2, 3, 1), etc.
Some invalid sequences are (1, 2, 1, 3), (1, 2, 3, 6).
(1, 2, 1, 3) is invalid since the first and third roll have an equal value and abs(1 - 3) = 2 (i and j are 1-indexed).
(1, 2, 3, 6) is invalid since the greatest common divisor of 3 and 6 = 3.
There are a total of 184 distinct sequences possible, so we return 184.

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
from math import gcd

class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 6

        dp = [[0] * 7 for _ in range(7)]
        for a in range(1, 7):
            for b in range(1, 7):
                if a != b and gcd(a, b) == 1:
                    dp[a][b] = 1

        for _ in range(n - 2):
            new = [[0] * 7 for _ in range(7)]
            for a in range(1, 7):
                for b in range(1, 7):
                    ways = dp[a][b]
                    if not ways:
                        continue
                    for c in range(1, 7):
                        if c != a and c != b and gcd(b, c) == 1:
                            new[b][c] = (new[b][c] + ways) % MOD
            dp = new

        return sum(sum(row) for row in dp) % MOD
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
- [1467. Probability of a Two Boxes Having The Same Number of Distinct Balls](../../1001-1500/1467-probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)
- [2442. Count Number of Distinct Integers After Reverse Operations](../../2001-2500/2442-count-number-of-distinct-integers-after-reverse-operations/)
- [2465. Number of Distinct Averages](../../2001-2500/2465-number-of-distinct-averages/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-distinct-roll-sequences/)
