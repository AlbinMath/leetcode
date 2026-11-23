# LeetCode 1960: Maximum Product of the Length of Two Palindromic Substrings

**LeetCode Problem #1960 — Maximum Product of the Length of Two Palindromic Substrings**
Solve LeetCode Maximum Product of the Length of Two Palindromic Substrings using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product of the Length of Two Palindromic Substrings |
| LeetCode | #1960 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** string `s` and are tasked with finding two **non-intersecting palindromic **substrings of **odd** length such that the product of their lengths is maximized.

More formally, you want to choose four integers `i`, `j`, `k`, `l` such that `0 <= i <= j < k <= l < s.length` and both the substrings `s[i...j]` and `s[k...l]` are palindromes and have odd lengths. `s[i...j]` denotes a substring from index `i` to index `j` **inclusive**.

Return *the **maximum** possible product of the lengths of the two non-intersecting palindromic substrings.*

A **palindrome** is a string that is the same forward and backward. A **substring** is a contiguous sequence of characters in a string.

## Constraints
- `2 <= s.length <= 10^5`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "ababbb"`
- **Output:** `9`
- **Explanation:** Substrings "aba" and "bbb" are palindromes with odd length. product = 3 * 3 = 9.

### Example 2
- **Input:** `s = "zaaaxbbby"`
- **Output:** `9`
- **Explanation:** Substrings "aaa" and "bbb" are palindromes with odd length. product = 3 * 3 = 9.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Product of the Length of Two Palindromic Substrings**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "ababbb"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** Substrings "aba" and "bbb" are palindromes with odd length. product = 3 * 3 = 9.

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
    def maxProduct(self, s: str) -> int:
        n = len(s)

        # Manacher, odd palindromes: d[i] = radius (palindrome length = 2*d[i]-1)
        d = [1] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d[i] = k
            if i + k - 1 > r:
                l, r = i - k + 1, i + k - 1

        # pre[e]: longest odd palindrome ending exactly at e (then prefix-max)
        pre = [1] * n
        c = 0
        for e in range(n):
            while c + d[c] - 1 < e:      # center c can no longer reach e
                c += 1
            pre[e] = 2 * (e - c) + 1
        for i in range(1, n):
            pre[i] = max(pre[i], pre[i - 1])

        # suf[b]: longest odd palindrome starting exactly at b (then suffix-max)
        suf = [1] * n
        c = n - 1
        for b in range(n - 1, -1, -1):
            while c - d[c] + 1 > b:
                c -= 1
            suf[b] = 2 * (c - b) + 1
        for i in range(n - 2, -1, -1):
            suf[i] = max(suf[i], suf[i + 1])

        return max(pre[i] * suf[i + 1] for i in range(n - 1))
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
- [2002. Maximum Product of the Length of Two Palindromic Subsequences](../../2001-2500/2130-maximum-product-of-the-length-of-two-palindromic-subsequences/)
- [1464. Maximum Product of Two Elements in an Array](../../1501-2000/1574-maximum-product-of-two-elements-in-an-array/)
- [1913. Maximum Product Difference Between Two Pairs](../../2001-2500/2042-maximum-product-difference-between-two-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/)
