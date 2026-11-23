# LeetCode 3389: Minimum Operations to Make Character Frequencies Equal

**LeetCode Problem #3389 — Minimum Operations to Make Character Frequencies Equal**
Solve LeetCode Minimum Operations to Make Character Frequencies Equal using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Make Character Frequencies Equal |
| LeetCode | #3389 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s`.

A string `t` is called **good** if all characters of `t` occur the same number of times.

You can perform the following operations **any number of times**:

Delete a character from `s`. 
 Insert a character in `s`. 
 Change a character in `s` to its next letter in the alphabet.

**Note** that you cannot change `'z'` to `'a'` using the third operation.

Return* *the **minimum** number of operations required to make `s` **good**.

## Constraints
- `3 <= s.length <= 2 * 10^4`
- `s` contains only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "acab"`
- **Output:** `1`
- **Explanation:** We can make `s` good by deleting one occurrence of character `'a'`.

### Example 2
- **Input:** `s = "wddw"`
- **Output:** `0`
- **Explanation:** We do not need to perform any operations since `s` is initially good.

### Example 3
- **Input:** `s = "aaabc"`
- **Output:** `2`
- **Explanation:** We can make `s` good by applying these operations: 

 
 Change one occurrence of `'a'` to `'b'` 
 Insert one occurrence of `'c'` into `s`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum Operations to Make Character Frequencies Equal**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "acab"`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** We can make `s` good by deleting one occurrence of character `'a'`.

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
    def makeStringGood(self, s: str) -> int:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        INF = float('inf')
        best = INF

        for f in range(1, n + 1):
            dp = [0, INF]
            prev_surplus = [0, 0]  # before the first letter nothing is carried

            for c in cnt:
                new_dp = [INF, INF]
                new_surplus = [c, max(0, c - f)]
                for t in (0, 1):
                    for pt in (0, 1):
                        if dp[pt] == INF:
                            continue
                        x = prev_surplus[pt]
                        if t == 0:
                            cost = c  # all c characters are deleted or moved on
                        else:
                            cost = max(0, c - f)  # surplus
                            if c < f:
                                cost += max(0, f - c - x)  # insertions
                        v = dp[pt] + cost
                        if v < new_dp[t]:
                            new_dp[t] = v
                dp = new_dp
                prev_surplus = new_surplus
            best = min(best, dp[0], dp[1])

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
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2753-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../3001-3500/3249-minimum-number-of-operations-to-make-array-xor-equal-to-k/)
- [2998. Minimum Number of Operations to Make X and Y Equal](../../3001-3500/3239-minimum-number-of-operations-to-make-x-and-y-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/)
