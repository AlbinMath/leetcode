# LeetCode 2781: Length of the Longest Valid Substring

**LeetCode Problem #2781 — Length of the Longest Valid Substring**
Solve LeetCode Length of the Longest Valid Substring using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Length of the Longest Valid Substring |
| LeetCode | #2781 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `word` and an array of strings `forbidden`.

A string is called **valid** if none of its substrings are present in `forbidden`.

Return *the length of the **longest valid substring** of the string *`word`.

A **substring** is a contiguous sequence of characters in a string, possibly empty.

## Constraints
- `1 <= word.length <= 10^5`
- `word` consists only of lowercase English letters.
- `1 <= forbidden.length <= 10^5`
- `1 <= forbidden[i].length <= 10`
- `forbidden[i]` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `word = "cbaaaabc", forbidden = ["aaa","cb"]`
- **Output:** `4`
- **Explanation:** There are 11 valid substrings in word: "c", "b", "a", "ba", "aa", "bc", "baa", "aab", "ab", "abc" and "aabc". The length of the longest valid substring is 4. 
It can be shown that all other substrings contain either "aaa" or "cb" as a substring.

### Example 2
- **Input:** `word = "leetcode", forbidden = ["de","le","e"]`
- **Output:** `4`
- **Explanation:** There are 11 valid substrings in word: "l", "t", "c", "o", "d", "tc", "co", "od", "tco", "cod", and "tcod". The length of the longest valid substring is 4.
It can be shown that all other substrings contain either "de", "le", or "e" as a substring.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Length of the Longest Valid Substring**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "cbaaaabc", forbidden = ["aaa","cb"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** There are 11 valid substrings in word: "c", "b", "a", "ba", "aa", "bc", "baa", "aab", "ab", "abc" and "aabc". The length of the longest valid substring is 4. 
It can be shown that all other substrings contain either "aaa" or "cb" as a substring.

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

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        bad = set(forbidden)
        n = len(word)
        left = 0
        ans = 0
        for r in range(n):
            lo = max(left, r - 9)
            for i in range(r, lo - 1, -1):
                if word[i:r + 1] in bad:
                    left = i + 1
                    break
            ans = max(ans, r - left + 1)
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
- [32. Longest Valid Parentheses](../../0001-0500/0032-longest-valid-parentheses/)
- [1964. Find the Longest Valid Obstacle Course at Each Position](../../1501-2000/1964-find-the-longest-valid-obstacle-course-at-each-position/)
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/length-of-the-longest-valid-substring/)
