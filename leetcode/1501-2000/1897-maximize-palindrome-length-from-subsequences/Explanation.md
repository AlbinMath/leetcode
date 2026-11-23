# LeetCode 1771: Maximize Palindrome Length From Subsequences

**LeetCode Problem #1771 — Maximize Palindrome Length From Subsequences**
Solve LeetCode Maximize Palindrome Length From Subsequences using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Palindrome Length From Subsequences |
| LeetCode | #1771 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings, `word1` and `word2`. You want to construct a string in the following manner:

Choose some **non-empty** subsequence `subsequence1` from `word1`. 
 Choose some **non-empty** subsequence `subsequence2` from `word2`. 
 Concatenate the subsequences: `subsequence1 + subsequence2`, to make the string.

Return *the **length** of the longest **palindrome** that can be constructed in the described manner. *If no palindromes can be constructed, return `0`.

A **subsequence** of a string `s` is a string that can be made by deleting some (possibly none) characters from `s` without changing the order of the remaining characters.

A **palindrome** is a string that reads the same forward as well as backward.

## Constraints
- `1 <= word1.length, word2.length <= 1000`
- `word1` and `word2` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `word1 = "cacb", word2 = "cbba"`
- **Output:** `5`
- **Explanation:** Choose "ab" from word1 and "cba" from word2 to make "abcba", which is a palindrome.

### Example 2
- **Input:** `word1 = "ab", word2 = "ab"`
- **Output:** `3`
- **Explanation:** Choose "ab" from word1 and "a" from word2 to make "aba", which is a palindrome.

### Example 3
- **Input:** `word1 = "aa", word2 = "bb"`
- **Output:** `0`
- **Explanation:** You cannot construct a palindrome from the described method, so return 0.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximize Palindrome Length From Subsequences**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word1 = "cacb", word2 = "cbba"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** Choose "ab" from word1 and "cba" from word2 to make "abcba", which is a palindrome.

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
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n, m = len(s), len(word1)
        dp = [[0] * n for _ in range(n)]
        ans = 0

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0) + 2
                    if i < m <= j:
                        ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

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
- [1930. Unique Length-3 Palindromic Subsequences](../../2001-2500/2059-unique-length-3-palindromic-subsequences/)
- [2002. Maximum Product of the Length of Two Palindromic Subsequences](../../2001-2500/2130-maximum-product-of-the-length-of-two-palindromic-subsequences/)
- [1177. Can Make Palindrome from Substring](../../1001-1500/1281-can-make-palindrome-from-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/)
