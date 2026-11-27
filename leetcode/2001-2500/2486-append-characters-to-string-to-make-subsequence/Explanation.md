# LeetCode 2486: Append Characters to String to Make Subsequence

**LeetCode Problem #2486 — Append Characters to String to Make Subsequence**
Solve LeetCode Append Characters to String to Make Subsequence using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Append Characters to String to Make Subsequence |
| LeetCode | #2486 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two strings `s` and `t` consisting of only lowercase English letters.

Return *the minimum number of characters that need to be appended to the end of *`s`* so that *`t`* becomes a **subsequence** of *`s`.

A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

## Constraints
- `1 <= s.length, t.length <= 10^5`
- `s` and `t` consist only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "coaching", t = "coding"`
- **Output:** `4`
- **Explanation:** Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("

### Example 2
- **Input:** `s = "abcde", t = "a"`
- **Output:** `0`
- **Explanation:** t is already a subsequence of s ("

### Example 3
- **Input:** `s = "z", t = "abcde"`
- **Output:** `5`
- **Explanation:** Append the characters "abcde" to the end of s so that s = "zabcde".
Now, t is a subsequence of s ("z

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Append Characters to String to Make Subsequence**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "coaching", t = "coding"`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("

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
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        m = len(t)
        for ch in s:
            if j < m and ch == t[j]:
                j += 1
        return m - j
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
- [1957. Delete Characters to Make Fancy String](../../1501-2000/1957-delete-characters-to-make-fancy-string/)
- [2287. Rearrange Characters to Make Target String](../../2001-2500/2287-rearrange-characters-to-make-target-string/)
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0828-count-unique-characters-of-all-substrings-of-a-given-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/)
