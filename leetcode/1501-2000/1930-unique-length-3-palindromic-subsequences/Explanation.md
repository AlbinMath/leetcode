# LeetCode 1930: Unique Length-3 Palindromic Subsequences

**LeetCode Problem #1930 — Unique Length-3 Palindromic Subsequences**
Solve LeetCode Unique Length-3 Palindromic Subsequences using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Unique Length-3 Palindromic Subsequences |
| LeetCode | #1930 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s`, return *the number of **unique palindromes of length three** that are a **subsequence** of *`s`.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted **once**.

A **palindrome** is a string that reads the same forwards and backwards.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, `"ace"` is a subsequence of `" a b c d e "`.

## Constraints
- `3 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "aabca"`
- **Output:** `3`
- **Explanation:** The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of " a a b c a ")
- "aaa" (subsequence of " aa bc a ")
- "aca" (subsequence of " a ab ca ")

### Example 2
- **Input:** `s = "adc"`
- **Output:** `0`
- **Explanation:** There are no palindromic subsequences of length 3 in "adc".

### Example 3
- **Input:** `s = "bbcbaba"`
- **Output:** `4`
- **Explanation:** The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of " bb c b aba")
- "bcb" (subsequence of " b b cb aba")
- "bab" (subsequence of " b bcb ab a")
- "aba" (subsequence of "bbcb aba ")

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Unique Length-3 Palindromic Subsequences**, we observe the problem requirements and utilize the **Dynamic Programming** technique. By maintaining a **DP Table / Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **DP Table / Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aabca"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of " a a b c a ")
- "aaa" (subsequence of " aa bc a ")
- "aca" (subsequence of " a ab ca ")

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:

  def countPalindromicSubsequence(self, s: str) -> int:
    first = {}
    last = {}

    for i, ch in enumerate(s):
      if ch not in first:
        first[ch] = i
      last[ch] = i

    ans = 0
    for ch in first:
      if first[ch] < last[ch]:
        ans += len(set(s[first[ch] + 1 : last[ch]]))

    return ans
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [2002. Maximum Product of the Length of Two Palindromic Subsequences](../../2001-2500/2002-maximum-product-of-the-length-of-two-palindromic-subsequences/)
- [1239. Maximum Length of a Concatenated String with Unique Characters](../../1001-1500/1239-maximum-length-of-a-concatenated-string-with-unique-characters/)
- [1771. Maximize Palindrome Length From Subsequences](../../1501-2000/1771-maximize-palindrome-length-from-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/unique-length-3-palindromic-subsequences/)
