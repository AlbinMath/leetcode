# LeetCode 318: Maximum Product of Word Lengths

**LeetCode Problem #318 — Maximum Product of Word Lengths**
Solve LeetCode Maximum Product of Word Lengths using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product of Word Lengths |
| LeetCode | #318 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string array `words`, return *the maximum value of* `length(word[i]) * length(word[j])` *where the two words do not share common letters*. If no such two words exist, return `0`.

## Constraints
- `2 <= words.length <= 1000`
- `1 <= words[i].length <= 1000`
- `words[i]` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["abcw","baz","foo","bar","xtfn","abcdef"]`
- **Output:** `16`
- **Explanation:** The two words can be "abcw", "xtfn".

### Example 2
- **Input:** `words = ["a","ab","abc","d","cd","bcd","abcd"]`
- **Output:** `4`
- **Explanation:** The two words can be "ab", "cd".

### Example 3
- **Input:** `words = ["a","aa","aaa","aaaa"]`
- **Output:** `0`
- **Explanation:** No such pair of words.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Product of Word Lengths**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["abcw","baz","foo","bar","xtfn","abcdef"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `16`.
4. **Verification:** The two words can be "abcw", "xtfn".

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
    def maxProduct(self, words: List[str]) -> int:
        best = {}  # mask -> longest word length with that mask
        for w in words:
            m = 0
            for ch in w:
                m |= 1 << (ord(ch) - 97)
            if len(w) > best.get(m, 0):
                best[m] = len(w)

        items = list(best.items())
        ans = 0
        for i in range(len(items)):
            mi, li = items[i]
            for j in range(i + 1, len(items)):
                mj, lj = items[j]
                if mi & mj == 0:
                    ans = max(ans, li * lj)
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
- [152. Maximum Product Subarray](../../0001-0500/0152-maximum-product-subarray/)
- [628. Maximum Product of Three Numbers](../../0501-1000/0628-maximum-product-of-three-numbers/)
- [1339. Maximum Product of Splitted Binary Tree](../../1001-1500/1465-maximum-product-of-splitted-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-of-word-lengths/)
