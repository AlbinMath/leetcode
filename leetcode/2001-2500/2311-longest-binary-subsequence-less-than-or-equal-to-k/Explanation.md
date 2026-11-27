# LeetCode 2311: Longest Binary Subsequence Less Than or Equal to K

**LeetCode Problem #2311 — Longest Binary Subsequence Less Than or Equal to K**
Solve LeetCode Longest Binary Subsequence Less Than or Equal to K using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Binary Subsequence Less Than or Equal to K |
| LeetCode | #2311 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a binary string `s` and a positive integer `k`.

Return *the length of the **longest** subsequence of *`s`* that makes up a **binary** number less than or equal to* `k`.

The subsequence can contain **leading zeroes**. 
 The empty string is considered to be equal to `0`. 
 A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

## Constraints
- `1 <= s.length <= 1000`
- `s[i]` is either `'0'` or `'1'`.
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `s = "1001010", k = 5`
- **Output:** `5`
- **Explanation:** The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
The length of this subsequence is 5, so 5 is returned.

### Example 2
- **Input:** `s = "00101001", k = 1`
- **Output:** `6`
- **Explanation:** "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
The length of this subsequence is 6, so 6 is returned.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Longest Binary Subsequence Less Than or Equal to K**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "1001010", k = 5`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
The length of this subsequence is 5, so 5 is returned.

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
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0
        value = 0
        bit = 1
        for c in reversed(s):
            if c == '0':
                count += 1
            elif bit <= k and value + bit <= k:
                value += bit
                count += 1
            if bit <= k:
                bit <<= 1
        return count
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
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](../../1001-1500/1438-longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)
- [3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K](../../3001-3500/3007-maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/)
- [3835. Count Subarrays With Cost Less Than or Equal to K](../../3501-4000/3835-count-subarrays-with-cost-less-than-or-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/)
