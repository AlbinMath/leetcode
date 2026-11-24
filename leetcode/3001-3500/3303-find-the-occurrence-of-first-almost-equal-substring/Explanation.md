# LeetCode 3303: Find the Occurrence of First Almost Equal Substring

**LeetCode Problem #3303 — Find the Occurrence of First Almost Equal Substring**
Solve LeetCode Find the Occurrence of First Almost Equal Substring using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Occurrence of First Almost Equal Substring |
| LeetCode | #3303 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `s` and `pattern`.

A string `x` is called **almost equal** to `y` if you can change **at most** one character in `x` to make it *identical* to `y`.

Return the **smallest** *starting index* of a substring in `s` that is **almost equal** to `pattern`. If no such index exists, return `-1`.

A **substring** is a contiguous non-empty sequence of characters within a string.

## Constraints
- `1 <= pattern.length < s.length <= 10^5`
- `s` and `pattern` consist only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abcdefg", pattern = "bcdffg"`
- **Output:** `1`
- **Explanation:** The substring `s[1..6] == "bcdefg"` can be converted to `"bcdffg"` by changing `s[4]` to `"f"`.

### Example 2
- **Input:** `s = "ababbababa", pattern = "bacaba"`
- **Output:** `4`
- **Explanation:** The substring `s[4..9] == "bababa"` can be converted to `"bacaba"` by changing `s[6]` to `"c"`.

### Example 3
- **Input:** `s = "abcd", pattern = "dba"`
- **Output:** `-1`

### Example 4
- **Input:** `s = "dde", pattern = "d"`
- **Output:** `0`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find the Occurrence of First Almost Equal Substring**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcdefg", pattern = "bcdffg"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The substring `s[1..6] == "bcdefg"` can be converted to `"bcdffg"` by changing `s[4]` to `"f"`.

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
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def z_function(t: str) -> list:
            n = len(t)
            z = [0] * n
            l = r = 0
            for i in range(1, n):
                if i < r:
                    z[i] = min(r - i, z[i - l])
                while i + z[i] < n and t[z[i]] == t[i + z[i]]:
                    z[i] += 1
                if i + z[i] > r:
                    l, r = i, i + z[i]
            return z

        n, m = len(s), len(pattern)
        z1 = z_function(pattern + '#' + s)
        z2 = z_function(pattern[::-1] + '#' + s[::-1])

        for i in range(n - m + 1):
            pre = z1[m + 1 + i]
            suf = z2[n + 1 - i]
            if pre + suf >= m - 1:
                return i
        return -1
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
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [1624. Largest Substring Between Two Equal Characters](../../1501-2000/1624-largest-substring-between-two-equal-characters/)
- [2831. Find the Longest Equal Subarray](../../2501-3000/2831-find-the-longest-equal-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/)
