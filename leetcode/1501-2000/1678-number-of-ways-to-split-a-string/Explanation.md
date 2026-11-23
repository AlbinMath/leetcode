# LeetCode 1573: Number of Ways to Split a String

**LeetCode Problem #1573 — Number of Ways to Split a String**
Solve LeetCode Number of Ways to Split a String using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways to Split a String |
| LeetCode | #1573 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a binary string `s`, you can split `s` into 3 **non-empty** strings `s1`, `s2`, and `s3` where `s1 + s2 + s3 = s`.

Return the number of ways `s` can be split such that the number of ones is the same in `s1`, `s2`, and `s3`. Since the answer may be too large, return it **modulo** `10^9 + 7`.

## Constraints
- `3 <= s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.

## Examples
### Example 1
- **Input:** `s = "10101"`
- **Output:** `4`
- **Explanation:** There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"

### Example 2
- **Input:** `s = "1001"`
- **Output:** `0`

### Example 3
- **Input:** `s = "0000"`
- **Output:** `3`
- **Explanation:** There are three ways to split s in 3 parts.
"0|0|00"
"0|00|0"
"00|0|0"

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number of Ways to Split a String**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "10101"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"

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
class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        pos = [i for i, ch in enumerate(s) if ch == '1']
        ones = len(pos)

        if ones % 3:
            return 0
        if ones == 0:
            return ((n - 1) * (n - 2) // 2) % MOD

        t = ones // 3
        first = pos[t] - pos[t - 1]
        second = pos[2 * t] - pos[2 * t - 1]
        return (first * second) % MOD
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
- [1525. Number of Good Ways to Split a String](../../1501-2000/1632-number-of-good-ways-to-split-a-string/)
- [1639. Number of Ways to Form a Target String Given a Dictionary](../../1501-2000/1744-number-of-ways-to-form-a-target-string-given-a-dictionary/)
- [1593. Split a String Into the Max Number of Unique Substrings](../../1501-2000/1715-split-a-string-into-the-max-number-of-unique-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-split-a-string/)
