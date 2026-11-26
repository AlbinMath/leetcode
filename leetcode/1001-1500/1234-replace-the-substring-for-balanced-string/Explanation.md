# LeetCode 1234: Replace the Substring for Balanced String

**LeetCode Problem #1234 — Replace the Substring for Balanced String**
Solve LeetCode Replace the Substring for Balanced String using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Replace the Substring for Balanced String |
| LeetCode | #1234 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string s of length `n` containing only four kinds of characters: `'Q'`, `'W'`, `'E'`, and `'R'`.

A string is said to be **balanced*** *if each of its characters appears `n / 4` times where `n` is the length of the string.

Return *the minimum length of the substring that can be replaced with **any** other string of the same length to make *`s`* **balanced***. If s is already **balanced**, return `0`.

## Constraints
- `n == s.length`
- `4 <= n <= 10^5`
- `n` is a multiple of `4`.
- `s` contains only `'Q'`, `'W'`, `'E'`, and `'R'`.

## Examples
### Example 1
- **Input:** `s = "QWER"`
- **Output:** `0`
- **Explanation:** s is already balanced.

### Example 2
- **Input:** `s = "QQWE"`
- **Output:** `1`
- **Explanation:** We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.

### Example 3
- **Input:** `s = "QQQW"`
- **Output:** `2`
- **Explanation:** We can replace the first "QQ" to "ER".

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Replace the Substring for Balanced String**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "QWER"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** s is already balanced.

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
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4
        cnt = Counter(s)
        
        if all(cnt[c] <= target for c in "QWER"):
            return 0
            
        min_len = n
        left = 0
        
        for right, ch in enumerate(s):
            cnt[ch] -= 1
            while all(cnt[c] <= target for c in "QWER"):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                cnt[s[left]] += 1
                left += 1
                
        return min_len
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
- [833. Find And Replace in String](../../0501-1000/0833-find-and-replace-in-string/)
- [1221. Split a String in Balanced Strings](../../1001-1500/1221-split-a-string-in-balanced-strings/)
- [1585. Check If String Is Transformable With Substring Sort Operations](../../1501-2000/1585-check-if-string-is-transformable-with-substring-sort-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/replace-the-substring-for-balanced-string/)
