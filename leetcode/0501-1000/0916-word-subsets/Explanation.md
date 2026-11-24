# LeetCode 916: Word Subsets

**LeetCode Problem #916 — Word Subsets**
Solve LeetCode Word Subsets using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Word Subsets |
| LeetCode | #916 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two string arrays `words1` and `words2`.

A string `b` is a **subset** of string `a` if every letter in `b` occurs in `a` including multiplicity.

For example, `"wrr"` is a subset of `"warrior"` but is not a subset of `"world"`.

A string `a` from `words1` is **universal** if for every string `b` in `words2`, `b` is a subset of `a`.

Return an array of all the **universal** strings in `words1`. You may return the answer in **any order**.

## Constraints
- `1 <= words1.length, words2.length <= 10^4`
- `1 <= words1[i].length, words2[i].length <= 10`
- `words1[i]` and `words2[i]` consist only of lowercase English letters.
- All the strings of `words1` are **unique**.

## Examples
### Example 1
- **Input:** `words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]`
- **Output:** `["facebook","google","leetcode"]`

### Example 2
- **Input:** `words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]`
- **Output:** `["leetcode"]`

### Example 3
- **Input:** `words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]`
- **Output:** `["cccbb"]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Word Subsets**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["facebook","google","leetcode"]`.

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

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        need = [0] * 26
        for b in words2:
            for ch, c in Counter(b).items():
                i = ord(ch) - 97
                if c > need[i]:
                    need[i] = c

        res = []
        for a in words1:
            have = [0] * 26
            for ch in a:
                have[ord(ch) - 97] += 1
            if all(have[i] >= need[i] for i in range(26)):
                res.append(a)
        return res
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
- [58. Length of Last Word](../../0001-0500/0058-length-of-last-word/)
- [79. Word Search](../../0001-0500/0079-word-search/)
- [126. Word Ladder II](../../0001-0500/0126-word-ladder-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/word-subsets/)
