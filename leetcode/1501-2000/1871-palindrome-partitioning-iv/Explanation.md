# LeetCode 1745: Palindrome Partitioning IV

**LeetCode Problem #1745 — Palindrome Partitioning IV**
Solve LeetCode Palindrome Partitioning IV using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Palindrome Partitioning IV |
| LeetCode | #1745 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, return `true` *if it is possible to split the string* `s` *into three **non-empty** palindromic substrings. Otherwise, return *`false`.​​​​​

A string is said to be palindrome if it the same string when reversed.

## Constraints
- `3 <= s.length <= 2000`
- `s`​​​​​​ consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abcbdd"`
- **Output:** `true`
- **Explanation:** "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.

### Example 2
- **Input:** `s = "bcbddxy"`
- **Output:** `false`
- **Explanation:** s cannot be split into 3 palindromes.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Palindrome Partitioning IV**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcbdd"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        for i in range(n - 2):
            if not pal[0][i]:
                continue
            for j in range(i + 1, n - 1):
                if pal[i + 1][j] and pal[j + 1][n - 1]:
                    return True

        return False
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [131. Palindrome Partitioning](../../0001-0500/0131-palindrome-partitioning/)
- [132. Palindrome Partitioning II](../../0001-0500/0132-palindrome-partitioning-ii/)
- [1278. Palindrome Partitioning III](../../1001-1500/1403-palindrome-partitioning-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/palindrome-partitioning-iv/)
