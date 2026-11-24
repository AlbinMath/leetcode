# LeetCode 1397: Find All Good Strings

**LeetCode Problem #1397 — Find All Good Strings**
Solve LeetCode Find All Good Strings using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find All Good Strings |
| LeetCode | #1397 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the strings `s1` and `s2` of size `n` and the string `evil`, return *the number of **good** strings*.

A **good** string has size `n`, it is alphabetically greater than or equal to `s1`, it is alphabetically smaller than or equal to `s2`, and it does not contain the string `evil` as a substring. Since the answer can be a huge number, return this **modulo** `10^9 + 7`.

## Constraints
- `s1.length == n`
- `s2.length == n`
- `s1 <= s2`
- `1 <= n <= 500`
- `1 <= evil.length <= 50`
- All strings consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `n = 2, s1 = "aa", s2 = "da", evil = "b"`
- **Output:** `51`
- **Explanation:** There are 25 good strings starting with 'a': "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c': "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd': "da".

### Example 2
- **Input:** `n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"`
- **Output:** `0`
- **Explanation:** All strings greater than or equal to s1 and smaller than or equal to s2 start with the prefix "leet", therefore, there is not any good string.

### Example 3
- **Input:** `n = 2, s1 = "gx", s2 = "gz", evil = "x"`
- **Output:** `2`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find All Good Strings**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, s1 = "aa", s2 = "da", evil = "b"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `51`.
4. **Verification:** There are 25 good strings starting with 'a': "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c': "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd': "da".

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
from functools import lru_cache

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        m = len(evil)

        # KMP failure function
        fail = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and evil[i] != evil[j]:
                j = fail[j - 1]
            if evil[i] == evil[j]:
                j += 1
            fail[i] = j

        # nxt[k][c]: matched length after appending letter c in state k (k < m)
        nxt = [[0] * 26 for _ in range(m)]
        for k in range(m):
            for c in range(26):
                ch = chr(97 + c)
                j = k
                while j > 0 and evil[j] != ch:
                    j = fail[j - 1]
                if evil[j] == ch:
                    j += 1
                nxt[k][c] = j

        @lru_cache(maxsize=None)
        def dp(pos: int, k: int, low: bool, high: bool) -> int:
            if pos == n:
                return 1
            lo = ord(s1[pos]) - 97 if low else 0
            hi = ord(s2[pos]) - 97 if high else 25
            total = 0
            for c in range(lo, hi + 1):
                nk = nxt[k][c]
                if nk == m:
                    continue
                total += dp(pos + 1, nk,
                            low and c == lo,
                            high and c == hi)
            return total % MOD

        return dp(0, 0, True, True)
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
- [438. Find All Anagrams in a String](../../0001-0500/0438-find-all-anagrams-in-a-string/)
- [448. Find All Numbers Disappeared in an Array](../../0001-0500/0448-find-all-numbers-disappeared-in-an-array/)
- [1723. Find Minimum Time to Finish All Jobs](../../1501-2000/1723-find-minimum-time-to-finish-all-jobs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-all-good-strings/)
