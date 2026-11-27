# LeetCode 3628: Maximum Number of Subsequences After One Inserting

**LeetCode Problem #3628 — Maximum Number of Subsequences After One Inserting**
Solve LeetCode Maximum Number of Subsequences After One Inserting using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Subsequences After One Inserting |
| LeetCode | #3628 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` consisting of uppercase English letters.

You are allowed to insert **at most one** uppercase English letter at **any** position (including the beginning or end) of the string.

Return the **maximum** number of `"LCT"` subsequences that can be formed in the resulting string after **at most one insertion**.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of uppercase English letters.

## Examples
### Example 1
- **Input:** `s = "LMCT"`
- **Output:** `2`
- **Explanation:** We can insert a `"L"` at the beginning of the string s to make `"LLMCT"`, which has 2 subsequences, at indices [0, 3, 4] and [1, 3, 4].

### Example 2
- **Input:** `s = "LCCT"`
- **Output:** `4`
- **Explanation:** We can insert a `"L"` at the beginning of the string s to make `"LLCCT"`, which has 4 subsequences, at indices [0, 2, 4], [0, 3, 4], [1, 2, 4] and [1, 3, 4].

### Example 3
- **Input:** `s = "L"`
- **Output:** `0`
- **Explanation:** Since it is not possible to obtain the subsequence `"LCT"` by inserting a single letter, the result is 0.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Number of Subsequences After One Inserting**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "LMCT"`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can insert a `"L"` at the beginning of the string s to make `"LLMCT"`, which has 2 subsequences, at indices [0, 3, 4] and [1, 3, 4].

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
    def numOfSubsequences(self, s: str) -> int:
        total_T = s.count('T')
        l = lc = lct = 0
        for ch in s:
            if ch == 'L':
                l += 1
            elif ch == 'C':
                lc += l
            elif ch == 'T':
                lct += lc
        LC_total = lc

        c = ct = 0
        for ch in reversed(s):
            if ch == 'T':
                pass
            elif ch == 'C':
                c += 1
        cnt_c = 0
        CT_total = 0
        for ch in s:
            if ch == 'C':
                cnt_c += 1
            elif ch == 'T':
                CT_total += cnt_c
        best_c = 0
        l_before = 0
        t_after = total_T
        for ch in s:
            best_c = max(best_c, l_before * t_after)  # gap before this char
            if ch == 'L':
                l_before += 1
            elif ch == 'T':
                t_after -= 1
        best_c = max(best_c, l_before * t_after)  # gap at the end

        return lct + max(CT_total, LC_total, best_c)
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
- [4058. Maximum Pulse Value After One Subarray Rotation](../../4001-4500/4058-maximum-pulse-value-after-one-subarray-rotation/)
- [4066. Maximum Equal Adjacent Pairs After at Most One Replacement](../../4001-4500/4066-maximum-equal-adjacent-pairs-after-at-most-one-replacement/)
- [792. Number of Matching Subsequences](../../0501-1000/0792-number-of-matching-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/)
