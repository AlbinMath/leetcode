# LeetCode 2767: Partition String Into Minimum Beautiful Substrings

**LeetCode Problem #2767 — Partition String Into Minimum Beautiful Substrings**
Solve LeetCode Partition String Into Minimum Beautiful Substrings using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition String Into Minimum Beautiful Substrings |
| LeetCode | #2767 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a binary string `s`, partition the string into one or more **substrings** such that each substring is **beautiful**.

A string is **beautiful** if:

It doesn't contain leading zeros. 
 It's the **binary** representation of a number that is a power of `5`.

Return *the **minimum** number of substrings in such partition. *If it is impossible to partition the string `s` into beautiful substrings, return `-1`.

A **substring** is a contiguous sequence of characters in a string.

## Constraints
- `1 <= s.length <= 15`
- `s[i]` is either `'0'` or `'1'`.

## Examples
### Example 1
- **Input:** `s = "1011"`
- **Output:** `2`
- **Explanation:** We can paritition the given string into ["101", "1"].
- The string "101" does not contain leading zeros and is the binary representation of integer 5^1 = 5.
- The string "1" does not contain leading zeros and is the binary representation of integer 5^0 = 1.
It can be shown that 2 is the minimum number of beautiful substrings that s can be partitioned into.

### Example 2
- **Input:** `s = "111"`
- **Output:** `3`
- **Explanation:** We can paritition the given string into ["1", "1", "1"].
- The string "1" does not contain leading zeros and is the binary representation of integer 5^0 = 1.
It can be shown that 3 is the minimum number of beautiful substrings that s can be partitioned into.

### Example 3
- **Input:** `s = "0"`
- **Output:** `-1`
- **Explanation:** We can not partition the given string into beautiful substrings.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Partition String Into Minimum Beautiful Substrings**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "1011"`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can paritition the given string into ["101", "1"].
- The string "101" does not contain leading zeros and is the binary representation of integer 5^1 = 5.
- The string "1" does not contain leading zeros and is the binary representation of integer 5^0 = 1.
It can be shown that 2 is the minimum number of beautiful substrings that s can be partitioned into.

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
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        pows = set()
        v = 1
        while v < (1 << n):
            pows.add(bin(v)[2:])
            v *= 5

        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] != INF and s[j:i] in pows:
                    dp[i] = min(dp[i], dp[j] + 1)
        return -1 if dp[n] == INF else dp[n]
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
- [3864. Minimum Cost to Partition a Binary String](../../3501-4000/3864-minimum-cost-to-partition-a-binary-string/)
- [1593. Split a String Into the Max Number of Unique Substrings](../../1501-2000/1593-split-a-string-into-the-max-number-of-unique-substrings/)
- [2696. Minimum String Length After Removing Substrings](../../2501-3000/2696-minimum-string-length-after-removing-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/)
