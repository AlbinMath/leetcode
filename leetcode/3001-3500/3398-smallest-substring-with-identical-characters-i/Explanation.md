# LeetCode 3398: Smallest Substring With Identical Characters I

**LeetCode Problem #3398 — Smallest Substring With Identical Characters I**
Solve LeetCode Smallest Substring With Identical Characters I using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Substring With Identical Characters I |
| LeetCode | #3398 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a binary string `s` of length `n` and an integer `numOps`.

You are allowed to perform the following operation on `s` **at most** `numOps` times:

Select any index `i` (where `0 <= i < n`) and **flip** `s[i]`. If `s[i] == '1'`, change `s[i]` to `'0'` and vice versa.

You need to **minimize** the length of the **longest** substring of `s` such that all the characters in the substring are **identical**.

Return the **minimum** length after the operations.

## Constraints
- `1 <= n == s.length <= 1000`
- `s` consists only of `'0'` and `'1'`.
- `0 <= numOps <= n`

## Examples
### Example 1
- **Input:** `s = "000001", numOps = 1`
- **Output:** `2`
- **Explanation:** By changing `s[2]` to `'1'`, `s` becomes `"001001"`. The longest substrings with identical characters are `s[0..1]` and `s[3..4]`.

### Example 2
- **Input:** `s = "0000", numOps = 2`
- **Output:** `1`
- **Explanation:** By changing `s[0]` and `s[2]` to `'1'`, `s` becomes `"1010"`.

### Example 3
- **Input:** `s = "0101", numOps = 0`
- **Output:** `1`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Smallest Substring With Identical Characters I**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "000001", numOps = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** By changing `s[2]` to `'1'`, `s` becomes `"001001"`. The longest substrings with identical characters are `s[0..1]` and `s[3..4]`.

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
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)

        # runs of identical characters
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append(j - i)
            i = j

        def ok(m: int) -> bool:
            if m == 1:
                mism = sum(ch != str(i & 1) for i, ch in enumerate(s))
                return min(mism, n - mism) <= numOps
            return sum(L // (m + 1) for L in runs) <= numOps

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
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
- [3399. Smallest Substring With Identical Characters II](../../3001-3500/3399-smallest-substring-with-identical-characters-ii/)
- [1081. Smallest Subsequence of Distinct Characters](../../1001-1500/1081-smallest-subsequence-of-distinct-characters/)
- [3816. Lexicographically Smallest String After Deleting Duplicate Characters](../../3501-4000/3816-lexicographically-smallest-string-after-deleting-duplicate-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-substring-with-identical-characters-i/)
