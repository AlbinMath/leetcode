# LeetCode 1525: Number of Good Ways to Split a String

**LeetCode Problem #1525 — Number of Good Ways to Split a String**
Solve LeetCode Number of Good Ways to Split a String using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Good Ways to Split a String |
| LeetCode | #1525 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s`.

A split is called **good** if you can split `s` into two non-empty strings `s_left` and `s_right` where their concatenation is equal to `s` (i.e., `s_left + s_right = s`) and the number of distinct letters in `s_left` and `s_right` is the same.

Return *the number of **good splits** you can make in `s`*.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "aacaba"`
- **Output:** `2`
- **Explanation:** There are 5 ways to split `"aacaba"` and 2 of them are good. 
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.

### Example 2
- **Input:** `s = "abcd"`
- **Output:** `1`
- **Explanation:** Split the string as follows ("ab", "cd").

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number of Good Ways to Split a String**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aacaba"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** There are 5 ways to split `"aacaba"` and 2 of them are good. 
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.

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
    def numSplits(self, s: str) -> int:
        right = Counter(s)
        right_distinct = len(right)
        left = set()
        ans = 0

        for ch in s[:-1]:
            left.add(ch)
            right[ch] -= 1
            if right[ch] == 0:
                right_distinct -= 1
            if len(left) == right_distinct:
                ans += 1

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
- [1573. Number of Ways to Split a String](../../1501-2000/1573-number-of-ways-to-split-a-string/)
- [1593. Split a String Into the Max Number of Unique Substrings](../../1501-2000/1593-split-a-string-into-the-max-number-of-unique-substrings/)
- [2270. Number of Ways to Split Array](../../2001-2500/2270-number-of-ways-to-split-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-good-ways-to-split-a-string/)
