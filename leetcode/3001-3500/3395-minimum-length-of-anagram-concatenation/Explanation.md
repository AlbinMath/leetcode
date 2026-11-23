# LeetCode 3138: Minimum Length of Anagram Concatenation

**LeetCode Problem #3138 — Minimum Length of Anagram Concatenation**
Solve LeetCode Minimum Length of Anagram Concatenation using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Length of Anagram Concatenation |
| LeetCode | #3138 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s`, which is known to be a concatenation of **anagrams** of some string `t`.

Return the **minimum** possible length of the string `t`.

An **anagram** is formed by rearranging the letters of a string. For example, "aab", "aba", and, "baa" are anagrams of "aab".

## Constraints
- `1 <= s.length <= 10^5`
- `s` consist only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abba"`
- **Output:** `2`
- **Explanation:** One possible string `t` could be `"ba"`.

### Example 2
- **Input:** `s = "cdef"`
- **Output:** `4`
- **Explanation:** One possible string `t` could be `"cdef"`, notice that `t` can be equal to `s`.

### Example 2
- **Input:** `s = "abcbcacabbaccba"`
- **Output:** `3`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Length of Anagram Concatenation**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abba"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** One possible string `t` could be `"ba"`.

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
from collections import Counter
from math import gcd
from functools import reduce

class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        total_counts = Counter(s)
        g = reduce(gcd, total_counts.values())
        min_len = n // g
        
        for length in range(min_len, n, min_len):
            if n % length != 0:
                continue
                
            target_freq = Counter(s[:length])
            if all(Counter(s[i : i + length]) == target_freq for i in range(length, n, length)):
                return length
                
        return n
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
- [1347. Minimum Number of Steps to Make Two Strings Anagram](../../1001-1500/1469-minimum-number-of-steps-to-make-two-strings-anagram/)
- [1750. Minimum Length of String After Deleting Similar Ends](../../1501-2000/1850-minimum-length-of-string-after-deleting-similar-ends/)
- [2186. Minimum Number of Steps to Make Two Strings Anagram II](../../2001-2500/2293-minimum-number-of-steps-to-make-two-strings-anagram-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-length-of-anagram-concatenation/)
