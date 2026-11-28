# LeetCode 2565: Subsequence With the Minimum Score

**LeetCode Problem #2565 — Subsequence With the Minimum Score**
Solve LeetCode Subsequence With the Minimum Score using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Subsequence With the Minimum Score |
| LeetCode | #2565 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `s` and `t`.

You are allowed to remove any number of characters from the string `t`.

The score of the string is `0` if no characters are removed from the string `t`, otherwise:

Let `left` be the minimum index among all removed characters. 
 Let `right` be the maximum index among all removed characters.

Then the score of the string is `right - left + 1`.

Return *the minimum possible score to make *`t`* a subsequence of *`s`*.*

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `" a b c d e "` while `"aec"` is not).

## Constraints
- `1 <= s.length, t.length <= 10^5`
- `s` and `t` consist of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abacaba", t = "bzaa"`
- **Output:** `1`
- **Explanation:** In this example, we remove the character "z" at index 1 (0-indexed).
The string t becomes "baa" which is a subsequence of the string "abacaba" and the score is 1 - 1 + 1 = 1.
It can be proven that 1 is the minimum score that we can achieve.

### Example 2
- **Input:** `s = "cde", t = "xyz"`
- **Output:** `3`
- **Explanation:** In this example, we remove characters "x", "y" and "z" at indices 0, 1, and 2 (0-indexed).
The string t becomes "" which is a subsequence of the string "cde" and the score is 2 - 0 + 1 = 3.
It can be proven that 3 is the minimum score that we can achieve.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Subsequence With the Minimum Score**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abacaba", t = "bzaa"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** In this example, we remove the character "z" at index 1 (0-indexed).
The string t becomes "baa" which is a subsequence of the string "abacaba" and the score is 1 - 1 + 1 = 1.
It can be proven that 1 is the minimum score that we can achieve.

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
    def minimumScore(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        # suf[j]: largest start index in s matching t[j:] as a subsequence
        # suf[m] = n  (empty suffix)
        suf = [-1] * (m + 1)
        suf[m] = n
        k = n - 1
        for j in range(m - 1, -1, -1):
            while k >= 0 and s[k] != t[j]:
                k -= 1
            if k < 0:
                break               # suf[j..0] stay -1
            suf[j] = k
            k -= 1

        ans = m                      # remove everything
        j = 0                        # smallest j with suf[j] > prefix end
        p = -1                       # s-index where t[0:i] ends (-1 if i == 0)

        for i in range(m + 1):       # i = length of kept prefix
            if i > 0:
                # extend prefix by t[i-1]
                p += 1
                while p < n and s[p] != t[i - 1]:
                    p += 1
                if p == n:
                    break            # prefix no longer fits in s

            j = max(j, i)
            while j <= m and suf[j] <= p:
                j += 1
            # suf[m] = n > p always, so j <= m here
            ans = min(ans, j - i)

        return ans
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
- [1403. Minimum Subsequence in Non-Increasing Order](../../1001-1500/1403-minimum-subsequence-in-non-increasing-order/)
- [1713. Minimum Operations to Make a Subsequence](../../1501-2000/1713-minimum-operations-to-make-a-subsequence/)
- [2542. Maximum Subsequence Score](../../2501-3000/2542-maximum-subsequence-score/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/subsequence-with-the-minimum-score/)
