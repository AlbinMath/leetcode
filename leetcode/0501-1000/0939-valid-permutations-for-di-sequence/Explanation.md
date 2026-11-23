# LeetCode 903: Valid Permutations for DI Sequence

**LeetCode Problem #903 — Valid Permutations for DI Sequence**
Solve LeetCode Valid Permutations for DI Sequence using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Permutations for DI Sequence |
| LeetCode | #903 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` of length `n` where `s[i]` is either:

`'D'` means decreasing, or 
 `'I'` means increasing.

A permutation `perm` of `n + 1` integers of all the integers in the range `[0, n]` is called a **valid permutation** if for all valid `i`:

If `s[i] == 'D'`, then `perm[i] > perm[i + 1]`, and 
 If `s[i] == 'I'`, then `perm[i] < perm[i + 1]`.

Return *the number of **valid permutations** *`perm`. Since the answer may be large, return it **modulo** `10^9 + 7`.

## Constraints
- `n == s.length`
- `1 <= n <= 200`
- `s[i]` is either `'I'` or `'D'`.

## Examples
### Example 1
- **Input:** `s = "DID"`
- **Output:** `5`
- **Explanation:** The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)

### Example 2
- **Input:** `s = "D"`
- **Output:** `1`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Valid Permutations for DI Sequence**, we observe the problem requirements and utilize the **Backtracking** technique. We decompose the problem into overlapping subproblems using a **Recursion Tree**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "DID"`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [1]  # one element, rank 0

        for i in range(1, n + 1):
            # prefix[k] = sum(dp[0..k-1])
            prefix = [0]
            for v in dp:
                prefix.append((prefix[-1] + v) % MOD)

            new = [0] * (i + 1)
            for j in range(i + 1):
                if s[i - 1] == 'I':
                    new[j] = prefix[j]                   # old ranks 0..j-1
                else:
                    new[j] = (prefix[i] - prefix[j]) % MOD  # old ranks j..i-1
            dp = new

        return sum(dp) % MOD
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1718. Construct the Lexicographically Largest Valid Sequence](../../1501-2000/1819-construct-the-lexicographically-largest-valid-sequence/)
- [3302. Find the Lexicographically Smallest Valid Sequence](../../3501-4000/3584-find-the-lexicographically-smallest-valid-sequence/)
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-permutations-for-di-sequence/)
