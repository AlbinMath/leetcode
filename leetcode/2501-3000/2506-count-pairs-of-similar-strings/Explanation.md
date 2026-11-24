# LeetCode 2506: Count Pairs Of Similar Strings

**LeetCode Problem #2506 — Count Pairs Of Similar Strings**
Solve LeetCode Count Pairs Of Similar Strings using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Pairs Of Similar Strings |
| LeetCode | #2506 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** string array `words`.

Two strings are **similar** if they consist of the same characters.

For example, `"abca"` and `"cba"` are similar since both consist of characters `'a'`, `'b'`, and `'c'`. 
 However, `"abacba"` and `"bcfd"` are not similar since they do not consist of the same characters.

Return *the number of pairs *`(i, j)`* such that *`0 <= i < j <= word.length - 1`* and the two strings *`words[i]`* and *`words[j]`* are similar*.

## Constraints
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consist of only lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["aba","aabb","abcd","bac","aabc"]`
- **Output:** `2`
- **Explanation:** There are 2 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
- i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'.

### Example 2
- **Input:** `words = ["aabb","ab","ba"]`
- **Output:** `3`
- **Explanation:** There are 3 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
- i = 0 and j = 2 : both words[0] and words[2] only consist of characters 'a' and 'b'.
- i = 1 and j = 2 : both words[1] and words[2] only consist of characters 'a' and 'b'.

### Example 3
- **Input:** `words = ["nba","cba","dba"]`
- **Output:** `0`
- **Explanation:** Since there does not exist any pair that satisfies the conditions, we return 0.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Pairs Of Similar Strings**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["aba","aabb","abcd","bac","aabc"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** There are 2 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
- i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'.

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
class Solution(object):
    def similarPairs(self, words):
        cnt = {}
        ans = 0
        for w in words:
            m = 0
            for ch in w:
                m |= 1 << (ord(ch) - 97)
            c = cnt.get(m, 0)
            ans += c
            cnt[m] = c + 1
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
- [854. K-Similar Strings](../../0501-1000/0854-k-similar-strings/)
- [1641. Count Sorted Vowel Strings](../../1501-2000/1641-count-sorted-vowel-strings/)
- [1684. Count the Number of Consistent Strings](../../1501-2000/1684-count-the-number-of-consistent-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-pairs-of-similar-strings/)
