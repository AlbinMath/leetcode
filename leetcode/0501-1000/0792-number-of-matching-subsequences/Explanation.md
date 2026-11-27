# LeetCode 792: Number of Matching Subsequences

**LeetCode Problem #792 — Number of Matching Subsequences**
Solve LeetCode Number of Matching Subsequences using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Matching Subsequences |
| LeetCode | #792 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s` and an array of strings `words`, return *the number of* `words[i]` *that is a subsequence of* `s`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, `"ace"` is a subsequence of `"abcde"`.

## Constraints
- `1 <= s.length <= 5 * 10^4`
- `1 <= words.length <= 5000`
- `1 <= words[i].length <= 50`
- `s` and `words[i]` consist of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abcde", words = ["a","bb","acd","ace"]`
- **Output:** `3`
- **Explanation:** There are three strings in words that are a subsequence of s: "a", "acd", "ace".

### Example 2
- **Input:** `s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]`
- **Output:** `2`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number of Matching Subsequences**, we observe the problem requirements and utilize the **Dynamic Programming** technique. By maintaining a **DP Table / Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **DP Table / Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcde", words = ["a","bb","acd","ace"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** There are three strings in words that are a subsequence of s: "a", "acd", "ace".

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
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for w in words:
            waiting[w[0]].append((w, 0))

        count = 0
        for ch in s:
            bucket = waiting.pop(ch, [])
            for w, i in bucket:
                i += 1
                if i == len(w):
                    count += 1
                else:
                    waiting[w[i]].append((w, i))
        return count
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
- [3405. Count the Number of Arrays with K Matching Adjacent Elements](../../3001-3500/3405-count-the-number-of-arrays-with-k-matching-adjacent-elements/)
- [1498. Number of Subsequences That Satisfy the Given Sum Condition](../../1001-1500/1498-number-of-subsequences-that-satisfy-the-given-sum-condition/)
- [1819. Number of Different Subsequences GCDs](../../1501-2000/1819-number-of-different-subsequences-gcds/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-matching-subsequences/)
