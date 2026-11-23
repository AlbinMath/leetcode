# LeetCode 3292: Minimum Number of Valid Strings to Form Target II

**LeetCode Problem #3292 — Minimum Number of Valid Strings to Form Target II**
Solve LeetCode Minimum Number of Valid Strings to Form Target II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Valid Strings to Form Target II |
| LeetCode | #3292 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of strings `words` and a string `target`.

A string `x` is called **valid** if `x` is a prefix of **any** string in `words`.

Return the **minimum** number of **valid** strings that can be *concatenated* to form `target`. If it is **not** possible to form `target`, return `-1`.

## Constraints
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 5 * 10^4`
- The input is generated such that `sum(words[i].length) <= 10^5`.
- `words[i]` consists only of lowercase English letters.
- `1 <= target.length <= 5 * 10^4`
- `target` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["abc","aaaaa","bcdef"], target = "aabcdabc"`
- **Output:** `3`
- **Explanation:** The target string can be formed by concatenating: 

 
 Prefix of length 2 of `words[1]`, i.e. `"aa"`. 
 Prefix of length 3 of `words[2]`, i.e. `"bcd"`. 
 Prefix of length 3 of `words[0]`, i.e. `"abc"`.

### Example 2
- **Input:** `words = ["abababab","ab"], target = "ababaababa"`
- **Output:** `2`
- **Explanation:** The target string can be formed by concatenating: 

 
 Prefix of length 5 of `words[0]`, i.e. `"ababa"`. 
 Prefix of length 5 of `words[0]`, i.e. `"ababa"`.

### Example 3
- **Input:** `words = ["abcdef"], target = "xyz"`
- **Output:** `-1`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Number of Valid Strings to Form Target II**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["abc","aaaaa","bcdef"], target = "aabcdabc"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The target string can be formed by concatenating: 

 
 Prefix of length 2 of `words[1]`, i.e. `"aa"`. 
 Prefix of length 3 of `words[2]`, i.e. `"bcd"`. 
 Prefix of length 3 of `words[0]`, i.e. `"abc"`.

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
from typing import List
import random

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        MOD = (1 << 61) - 1
        B = random.randrange(10**6, 10**9)
        m = len(target)

        seen = set()
        maxlen = 0
        for w in words:
            h = 0
            for k, ch in enumerate(w, 1):
                h = (h * B + ord(ch)) % MOD
                seen.add(h * 100003 + k)
            maxlen = max(maxlen, len(w))

        H = [0] * (m + 1)
        P = [1] * (m + 1)
        for i, ch in enumerate(target):
            H[i + 1] = (H[i] * B + ord(ch)) % MOD
            P[i + 1] = P[i] * B % MOD

        L = [0] * m
        for i in range(m):
            lo, hi = 0, min(m - i, maxlen)
            while lo < hi:
                mid = (lo + hi + 1) // 2
                h = (H[i + mid] - H[i] * P[mid]) % MOD
                if h * 100003 + mid in seen:
                    lo = mid
                else:
                    hi = mid - 1
            L[i] = lo

        jumps = 0
        cur = 0
        far = 0
        i = 0
        while cur < m:
            while i <= cur:
                far = max(far, i + L[i])
                i += 1
            if far <= cur:
                return -1
            jumps += 1
            cur = far
        return jumps
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
- [3291. Minimum Number of Valid Strings to Form Target I](../../3501-4000/3559-minimum-number-of-valid-strings-to-form-target-i/)
- [1526. Minimum Number of Increments on Subarrays to Form a Target Array](../../1501-2000/1633-minimum-number-of-increments-on-subarrays-to-form-a-target-array/)
- [1347. Minimum Number of Steps to Make Two Strings Anagram](../../1001-1500/1469-minimum-number-of-steps-to-make-two-strings-anagram/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/)
