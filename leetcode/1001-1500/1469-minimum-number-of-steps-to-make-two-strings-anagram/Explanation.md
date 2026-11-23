# LeetCode 1347: Minimum Number of Steps to Make Two Strings Anagram

**LeetCode Problem #1347 — Minimum Number of Steps to Make Two Strings Anagram**
Solve LeetCode Minimum Number of Steps to Make Two Strings Anagram using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Steps to Make Two Strings Anagram |
| LeetCode | #1347 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two strings of the same length `s` and `t`. In one step you can choose **any character** of `t` and replace it with **another character**.

Return *the minimum number of steps* to make `t` an anagram of `s`.

An **Anagram** of a string is a string that contains the same characters with a different (or the same) ordering.

## Constraints
- `1 <= s.length <= 5 * 10^4`
- `s.length == t.length`
- `s` and `t` consist of lowercase English letters only.

## Examples
### Example 1
- **Input:** `s = "bab", t = "aba"`
- **Output:** `1`
- **Explanation:** Replace the first 'a' in t with b, t = "bba" which is anagram of s.

### Example 2
- **Input:** `s = "leetcode", t = "practice"`
- **Output:** `5`
- **Explanation:** Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

### Example 3
- **Input:** `s = "anagram", t = "mangaar"`
- **Output:** `0`
- **Explanation:** "anagram" and "mangaar" are anagrams.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Number of Steps to Make Two Strings Anagram**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "bab", t = "aba"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Replace the first 'a' in t with b, t = "bba" which is anagram of s.

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
    def minSteps(self, s: str, t: str) -> int:
        diff = Counter(t) - Counter(s)  # keeps only positive surpluses in t
        return sum(diff.values())
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
- [2186. Minimum Number of Steps to Make Two Strings Anagram II](../../2001-2500/2293-minimum-number-of-steps-to-make-two-strings-anagram-ii/)
- [712. Minimum ASCII Delete Sum for Two Strings](../../0501-1000/0712-minimum-ascii-delete-sum-for-two-strings/)
- [1247. Minimum Swaps to Make Strings Equal](../../1001-1500/1369-minimum-swaps-to-make-strings-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/)
