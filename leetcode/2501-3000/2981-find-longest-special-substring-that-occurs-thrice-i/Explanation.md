# LeetCode 2981: Find Longest Special Substring That Occurs Thrice I

**LeetCode Problem #2981 — Find Longest Special Substring That Occurs Thrice I**
Solve LeetCode Find Longest Special Substring That Occurs Thrice I using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Longest Special Substring That Occurs Thrice I |
| LeetCode | #2981 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` that consists of lowercase English letters.

A string is called **special** if it is made up of only a single character. For example, the string `"abc"` is not special, whereas the strings `"ddd"`, `"zz"`, and `"f"` are special.

Return *the length of the **longest special substring** of *`s` *which occurs **at least thrice***, *or *`-1`* if no special substring occurs at least thrice*.

A **substring** is a contiguous **non-empty** sequence of characters within a string.

## Constraints
- `3 <= s.length <= 50`
- `s` consists of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "aaaa"`
- **Output:** `2`
- **Explanation:** The longest special substring which occurs thrice is "aa": substrings "

### Example 2
- **Input:** `s = "abcdef"`
- **Output:** `-1`
- **Explanation:** There exists no special substring which occurs at least thrice. Hence return -1.

### Example 3
- **Input:** `s = "abcaba"`
- **Output:** `1`
- **Explanation:** The longest special substring which occurs thrice is "a": substrings "

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find Longest Special Substring That Occurs Thrice I**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aaaa"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The longest special substring which occurs thrice is "aa": substrings "

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
from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        cnt = defaultdict(int)
        n = len(s)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            L = j - i
            for ln in range(1, L + 1):
                cnt[(s[i], ln)] += L - ln + 1
            i = j

        ans = -1
        for (ch, ln), c in cnt.items():
            if c >= 3 and ln > ans:
                ans = ln
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
- [2982. Find Longest Special Substring That Occurs Thrice II](../../2501-3000/2982-find-longest-special-substring-that-occurs-thrice-ii/)
- [1371. Find the Longest Substring Containing Vowels in Even Counts](../../1001-1500/1371-find-the-longest-substring-containing-vowels-in-even-counts/)
- [1542. Find Longest Awesome Substring](../../1501-2000/1542-find-longest-awesome-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/)
