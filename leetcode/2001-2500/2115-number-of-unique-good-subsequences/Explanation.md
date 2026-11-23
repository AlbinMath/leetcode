# LeetCode 1987: Number of Unique Good Subsequences

**LeetCode Problem #1987 — Number of Unique Good Subsequences**
Solve LeetCode Number of Unique Good Subsequences using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Unique Good Subsequences |
| LeetCode | #1987 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a binary string `binary`. A **subsequence** of `binary` is considered **good** if it is **not empty** and has **no leading zeros** (with the exception of `"0"`).

Find the number of **unique good subsequences** of `binary`.

For example, if `binary = "001"`, then all the **good** subsequences are `["0", "0", "1"]`, so the **unique** good subsequences are `"0"` and `"1"`. Note that subsequences `"00"`, `"01"`, and `"001"` are not good because they have leading zeros.

Return *the number of **unique good subsequences** of *`binary`. Since the answer may be very large, return it **modulo** `10^9 + 7`.

A **subsequence** is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

## Constraints
- `1 <= binary.length <= 10^5`
- `binary` consists of only `'0'`s and `'1'`s.

## Examples
### Example 1
- **Input:** `binary = "001"`
- **Output:** `2`
- **Explanation:** The good subsequences of binary are ["0", "0", "1"].
The unique good subsequences are "0" and "1".

### Example 2
- **Input:** `binary = "11"`
- **Output:** `2`
- **Explanation:** The good subsequences of binary are ["1", "1", "11"].
The unique good subsequences are "1" and "11".

### Example 3
- **Input:** `binary = "101"`
- **Output:** `5`
- **Explanation:** The good subsequences of binary are ["1", "0", "1", "10", "11", "101"]. 
The unique good subsequences are "0", "1", "10", "11", and "101".

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Number of Unique Good Subsequences**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `binary = "001"`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The good subsequences of binary are ["0", "0", "1"].
The unique good subsequences are "0" and "1".

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
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9 + 7
        ends_with_0 = 0
        ends_with_1 = 0
        has_zero = 0
        
        for ch in binary:
            if ch == '0':
                ends_with_0 = (ends_with_0 + ends_with_1) % MOD
                has_zero = 1
            else:
                ends_with_1 = (ends_with_0 + ends_with_1 + 1) % MOD
                
        return (ends_with_0 + ends_with_1 + has_zero) % MOD
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
- [1207. Unique Number of Occurrences](../../1001-1500/1319-unique-number-of-occurrences/)
- [1593. Split a String Into the Max Number of Unique Substrings](../../1501-2000/1715-split-a-string-into-the-max-number-of-unique-substrings/)
- [1930. Unique Length-3 Palindromic Subsequences](../../2001-2500/2059-unique-length-3-palindromic-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-unique-good-subsequences/)
