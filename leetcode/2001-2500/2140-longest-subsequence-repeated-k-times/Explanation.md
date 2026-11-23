# LeetCode 2014: Longest Subsequence Repeated k Times

**LeetCode Problem #2014 — Longest Subsequence Repeated k Times**
Solve LeetCode Longest Subsequence Repeated k Times using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Subsequence Repeated k Times |
| LeetCode | #2014 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` of length `n`, and an integer `k`. You are tasked to find the **longest subsequence repeated** `k` times in string `s`.

A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

A subsequence `seq` is **repeated** `k` times in the string `s` if `seq * k` is a subsequence of `s`, where `seq * k` represents a string constructed by concatenating `seq` `k` times.

For example, `"bba"` is repeated `2` times in the string `"bababcba"`, because the string `"bbabba"`, constructed by concatenating `"bba"` `2` times, is a subsequence of the string `"** b **a** bab **c** ba **"`.

Return *the **longest subsequence repeated** *`k`* times in string *`s`*. If multiple such subsequences are found, return the **lexicographically largest** one. If there is no such subsequence, return an **empty** string*.

## Constraints
- `n == s.length`
- `2 <= k <= 2000`
- `2 <= n < min(2001, k * 8)`
- `s` consists of lowercase English letters.

## Examples
### Example 2
- **Input:** `s = "bb", k = 2`
- **Output:** `"b"`
- **Explanation:** The longest subsequence repeated 2 times is "b".

### Example 3
- **Input:** `s = "ab", k = 2`
- **Output:** `""`
- **Explanation:** There is no subsequence repeated 2 times. Empty string is returned.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Longest Subsequence Repeated k Times**, we observe the problem requirements and utilize the **Dynamic Programming** technique. By maintaining a **DP Table / Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **DP Table / Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "bb", k = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"b"`.
4. **Verification:** The longest subsequence repeated 2 times is "b".

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
from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        cnt = Counter(s)
        letters = sorted((c for c in cnt if cnt[c] >= k), reverse=True)

        def ok(seq: str) -> bool:
            # is seq * k a subsequence of s?
            i, rep, m = 0, 0, len(seq)
            for ch in s:
                if ch == seq[i]:
                    i += 1
                    if i == m:
                        i = 0
                        rep += 1
                        if rep == k:
                            return True
            return False

        best = ""
        q = deque([""])
        while q:
            cur = q.popleft()
            for c in letters:
                nxt = cur + c
                if ok(nxt):
                    if len(nxt) > len(best) or (len(nxt) == len(best) and nxt > best):
                        best = nxt
                    q.append(nxt)
        return best
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
- [1566. Detect Pattern of Length M Repeated K or More Times](../../1501-2000/1689-detect-pattern-of-length-m-repeated-k-or-more-times/)
- [2311. Longest Binary Subsequence Less Than or Equal to K](../../2001-2500/2395-longest-binary-subsequence-less-than-or-equal-to-k/)
- [1156. Swap For Longest Repeated Character Substring](../../1001-1500/1261-swap-for-longest-repeated-character-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-subsequence-repeated-k-times/)
