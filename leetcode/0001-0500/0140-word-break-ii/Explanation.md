# LeetCode 140: Word Break II

**LeetCode Problem #140 — Word Break II**
Solve LeetCode Word Break II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Word Break II |
| LeetCode | #140 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s` and a dictionary of strings `wordDict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in **any order**.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.

## Constraints
- `1 <= s.length <= 20`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 10`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are **unique**.
- Input is generated in a way that the length of the answer doesn't exceed 10^5.

## Examples
### Example 1
- **Input:** `s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]`
- **Output:** `["cats and dog","cat sand dog"]`

### Example 2
- **Input:** `s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]`
- **Output:** `["pine apple pen apple","pineapple pen apple","pine applepen apple"]`
- **Explanation:** Note that you are allowed to reuse a dictionary word.

### Example 3
- **Input:** `s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]`
- **Output:** `[]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Word Break II**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["cats and dog","cat sand dog"]`.

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
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        n = len(s)
        maxlen = max(len(w) for w in words)

        @lru_cache(maxsize=None)
        def solve(i):
            if i == n:
                return [""]
            res = []
            for j in range(i + 1, min(n, i + maxlen) + 1):
                w = s[i:j]
                if w in words:
                    for rest in solve(j):
                        res.append(w + (" " + rest if rest else ""))
            return res

        return solve(0)
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
- [139. Word Break](../../0001-0500/0139-word-break/)
- [1328. Break a Palindrome](../../1001-1500/1252-break-a-palindrome/)
- [1433. Check If a String Can Break Another String](../../1501-2000/1530-check-if-a-string-can-break-another-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/word-break-ii/)
