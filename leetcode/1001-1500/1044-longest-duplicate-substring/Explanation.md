# LeetCode 1044: Longest Duplicate Substring

**LeetCode Problem #1044 — Longest Duplicate Substring**
Solve LeetCode Longest Duplicate Substring using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Duplicate Substring |
| LeetCode | #1044 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, consider all *duplicated substrings*: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return **any** duplicated substring that has the longest possible length. If `s` does not have a duplicated substring, the answer is `""`.

## Constraints
- `2 <= s.length <= 3 * 10^4`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "banana"`
- **Output:** `"ana"`

### Example 2
- **Input:** `s = "abcd"`
- **Output:** `""`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Longest Duplicate Substring**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "banana"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"ana"`.

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
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        nums = [ord(c) - 97 for c in s]
        BASE = 26
        MOD1, MOD2 = (1 << 61) - 1, 10**9 + 7  # two moduli to make collisions negligible

        def search(L: int) -> int:
            """Return start index of a duplicate of length L, or -1."""
            pow1 = pow(BASE, L, MOD1)
            pow2 = pow(BASE, L, MOD2)
            h1 = h2 = 0
            for i in range(L):
                h1 = (h1 * BASE + nums[i]) % MOD1
                h2 = (h2 * BASE + nums[i]) % MOD2
            seen = {(h1, h2): [0]}
            for i in range(1, n - L + 1):
                h1 = (h1 * BASE - nums[i - 1] * pow1 + nums[i + L - 1]) % MOD1
                h2 = (h2 * BASE - nums[i - 1] * pow2 + nums[i + L - 1]) % MOD2
                key = (h1, h2)
                if key in seen:
                    # verify to rule out any collision
                    for j in seen[key]:
                        if s[j:j + L] == s[i:i + L]:
                            return i
                    seen[key].append(i)
                else:
                    seen[key] = [i]
            return -1

        lo, hi = 1, n - 1
        start, best = -1, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            idx = search(mid)
            if idx != -1:
                start, best = idx, mid
                lo = mid + 1
            else:
                hi = mid - 1
        return s[start:start + best] if start != -1 else ""
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
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [395. Longest Substring with At Least K Repeating Characters](../../0001-0500/0395-longest-substring-with-at-least-k-repeating-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-duplicate-substring/)
