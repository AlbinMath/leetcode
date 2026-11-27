# LeetCode 1156: Swap For Longest Repeated Character Substring

**LeetCode Problem #1156 — Swap For Longest Repeated Character Substring**
Solve LeetCode Swap For Longest Repeated Character Substring using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Swap For Longest Repeated Character Substring |
| LeetCode | #1156 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `text`. You can swap two of the characters in the `text`.

Return *the length of the longest substring with repeated characters*.

## Constraints
- `1 <= text.length <= 2 * 10^4`
- `text` consist of lowercase English characters only.

## Examples
### Example 1
- **Input:** `text = "ababa"`
- **Output:** `3`
- **Explanation:** We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa" with length 3.

### Example 2
- **Input:** `text = "aaabaaa"`
- **Output:** `6`
- **Explanation:** Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa" with length 6.

### Example 3
- **Input:** `text = "aaaaa"`
- **Output:** `5`
- **Explanation:** No need to swap, longest repeated character substring is "aaaaa" with length is 5.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Swap For Longest Repeated Character Substring**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `text = "ababa"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa" with length 3.

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
from itertools import groupby

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        total = Counter(text)
        runs = [(ch, sum(1 for _ in grp)) for ch, grp in groupby(text)]
        
        ans = 0
        for i, (ch, length) in enumerate(runs):
            ans = max(ans, min(length + 1, total[ch]))
            
            if 0 < i < len(runs) - 1 and length == 1 and runs[i - 1][0] == runs[i + 1][0]:
                adj_ch = runs[i - 1][0]
                merged = runs[i - 1][1] + runs[i + 1][1] + 1
                ans = max(ans, min(merged, total[adj_ch]))
                
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
- [2213. Longest Substring of One Repeating Character](../../2001-2500/2213-longest-substring-of-one-repeating-character/)
- [3900. Longest Balanced Substring After One Swap](../../3501-4000/3900-longest-balanced-substring-after-one-swap/)
- [459. Repeated Substring Pattern](../../0001-0500/0459-repeated-substring-pattern/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/swap-for-longest-repeated-character-substring/)
