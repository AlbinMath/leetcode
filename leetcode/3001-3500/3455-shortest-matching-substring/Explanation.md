# LeetCode 3455: Shortest Matching Substring

**LeetCode Problem #3455 — Shortest Matching Substring**
Solve LeetCode Shortest Matching Substring using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Matching Substring |
| LeetCode | #3455 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` and a pattern string `p`, where `p` contains **exactly two** `'*'` characters.

The `'*'` in `p` matches any sequence of zero or more characters.

Return the length of the **shortest** substring in `s` that matches `p`. If there is no such substring, return -1.

**Note:** The empty substring is considered valid.

## Constraints
- `1 <= s.length <= 10^5`
- `2 <= p.length <= 10^5`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters and exactly two `'*'`.

## Examples
### Example 1
- **Input:** `s = "abaacbaecebce", p = "ba*c*ce"`
- **Output:** `8`
- **Explanation:** The shortest matching substring of `p` in `s` is "

### Example 2
- **Input:** `s = "baccbaadbc", p = "cc*baa*adb"`
- **Output:** `-1`
- **Explanation:** There is no matching substring in `s`.

### Example 3
- **Input:** `s = "a", p = "**"`
- **Output:** `0`
- **Explanation:** The empty substring is the shortest matching substring.

### Example 4
- **Input:** `s = "madlogic", p = "*adlogi*"`
- **Output:** `6`
- **Explanation:** The shortest matching substring of `p` in `s` is "

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Shortest Matching Substring**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abaacbaecebce", p = "ba*c*ce"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** The shortest matching substring of `p` in `s` is "

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
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        n = len(s)
        A, B, C = p.split('*')
        INF = float('inf')

        def z_function(t: str) -> list:
            L = len(t)
            z = [0] * L
            l = r = 0
            for i in range(1, L):
                if i < r:
                    z[i] = min(r - i, z[i - l])
                while i + z[i] < L and t[z[i]] == t[i + z[i]]:
                    z[i] += 1
                if i + z[i] > r:
                    l, r = i, i + z[i]
            return z

        def occurrences(x: str) -> list:
            # occ[i] is True if x occurs in s starting at i, for i in 0..n
            if not x:
                return [True] * (n + 1)
            m = len(x)
            z = z_function(x + '#' + s)
            occ = [False] * (n + 1)
            for i in range(n - m + 1):
                if z[m + 1 + i] >= m:
                    occ[i] = True
            return occ

        occA, occB, occC = occurrences(A), occurrences(B), occurrences(C)
        la, lb, lc = len(A), len(B), len(C)

        # prevA[j]: largest a <= j with occA[a], else -1
        prevA = [-1] * (n + 1)
        for j in range(n + 1):
            prevA[j] = j if occA[j] else (prevA[j - 1] if j else -1)

        # nextC[j]: smallest c >= j with occC[c], else INF
        nextC = [INF] * (n + 2)
        for j in range(n, -1, -1):
            nextC[j] = j if occC[j] else nextC[j + 1]

        ans = INF
        for b in range(n + 1):
            if not occB[b] or b - la < 0 or b + lb > n:
                continue
            a = prevA[b - la]
            if a == -1:
                continue
            c = nextC[b + lb]
            if c == INF:
                continue
            ans = min(ans, c + lc - a)

        return -1 if ans == INF else ans
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
- [3407. Substring Matching Pattern](../../3001-3500/3407-substring-matching-pattern/)
- [3076. Shortest Uncommon Substring in an Array](../../3001-3500/3076-shortest-uncommon-substring-in-an-array/)
- [10. Regular Expression Matching](../../0001-0500/0010-regular-expression-matching/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-matching-substring/)
