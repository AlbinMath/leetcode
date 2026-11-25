# LeetCode 3399: Smallest Substring With Identical Characters II

**LeetCode Problem #3399 — Smallest Substring With Identical Characters II**
Solve LeetCode Smallest Substring With Identical Characters II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Substring With Identical Characters II |
| LeetCode | #3399 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a binary string `s` of length `n` and an integer `numOps`.

You are allowed to perform the following operation on `s` **at most** `numOps` times:

Select any index `i` (where `0 <= i < n`) and **flip** `s[i]`. If `s[i] == '1'`, change `s[i]` to `'0'` and vice versa.

You need to **minimize** the length of the **longest** substring of `s` such that all the characters in the substring are **identical**.

Return the **minimum** length after the operations.

## Constraints
- `1 <= n == s.length <= 10^5`
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
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Smallest Substring With Identical Characters II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "000001", numOps = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** By changing `s[2]` to `'1'`, `s` becomes `"001001"`. The longest substrings with identical characters are `s[0..1]` and `s[3..4]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)

        # run lengths
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
                # target 0101... : mismatches where s[i] != i % 2
                c = sum(1 for i, ch in enumerate(s) if int(ch) != i % 2)
                return min(c, n - c) <= numOps
            need = 0
            for L in runs:
                need += L // (m + 1)
                if need > numOps:
                    return False
            return True

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
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3398. Smallest Substring With Identical Characters I](../../3001-3500/3398-smallest-substring-with-identical-characters-i/)
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)
- [395. Longest Substring with At Least K Repeating Characters](../../0001-0500/0395-longest-substring-with-at-least-k-repeating-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/)
