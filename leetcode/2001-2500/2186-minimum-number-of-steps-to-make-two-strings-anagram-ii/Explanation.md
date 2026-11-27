# LeetCode 2186: Minimum Number of Steps to Make Two Strings Anagram II

**LeetCode Problem #2186 — Minimum Number of Steps to Make Two Strings Anagram II**
Solve LeetCode Minimum Number of Steps to Make Two Strings Anagram II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Steps to Make Two Strings Anagram II |
| LeetCode | #2186 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two strings `s` and `t`. In one step, you can append **any character** to either `s` or `t`.

Return *the minimum number of steps to make *`s`* and *`t`* **anagrams** of each other.*

An **anagram** of a string is a string that contains the same characters with a different (or the same) ordering.

## Constraints
- `1 <= s.length, t.length <= 2 * 10^5`
- `s` and `t` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "`
- **Output:** `7`
- **Explanation:** - In 2 steps, we can append the letters in "as" onto s = "leetcode", forming s = "leetcode

### Example 2
- **Input:** `s = "night", t = "thing"`
- **Output:** `0`
- **Explanation:** The given strings are already anagrams of each other. Thus, we do not need any further steps.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Number of Steps to Make Two Strings Anagram II**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** - In 2 steps, we can append the letters in "as" onto s = "leetcode", forming s = "leetcode

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
    def minSteps(self, s: str, t: str) -> int:
        diff = [0] * 26
        base = ord('a')
        
        for ch in s:
            diff[ord(ch) - base] += 1
            
        for ch in t:
            diff[ord(ch) - base] -= 1
            
        return sum(abs(count) for count in diff)
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
- [1347. Minimum Number of Steps to Make Two Strings Anagram](../../1001-1500/1347-minimum-number-of-steps-to-make-two-strings-anagram/)
- [3800. Minimum Cost to Make Two Binary Strings Equal](../../3501-4000/3800-minimum-cost-to-make-two-binary-strings-equal/)
- [712. Minimum ASCII Delete Sum for Two Strings](../../0501-1000/0712-minimum-ascii-delete-sum-for-two-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/)
