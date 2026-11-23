# LeetCode 833: Find And Replace in String

**LeetCode Problem #833 — Find And Replace in String**
Solve LeetCode Find And Replace in String using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find And Replace in String |
| LeetCode | #833 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** string `s` that you must perform `k` replacement operations on. The replacement operations are given as three **0-indexed** parallel arrays, `indices`, `sources`, and `targets`, all of length `k`.

To complete the `i^th` replacement operation:

Check if the **substring** `sources[i]` occurs at index `indices[i]` in the **original string** `s`. 
 If it does not occur, **do nothing**. 
 Otherwise if it does occur, **replace** that substring with `targets[i]`.

For example, if `s = " ab cd"`, `indices[i] = 0`, `sources[i] = "ab"`, and `targets[i] = "eee"`, then the result of this replacement will be `" eee cd"`.

All replacement operations must occur **simultaneously**, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will **not overlap**.

For example, a testcase with `s = "abc"`, `indices = [0, 1]`, and `sources = ["ab","bc"]` will not be generated because the `"ab"` and `"bc"` replacements overlap.

Return *the **resulting string** after performing all replacement operations on *`s`.

A **substring** is a contiguous sequence of characters in a string.

## Constraints
- `1 <= s.length <= 1000`
- `k == indices.length == sources.length == targets.length`
- `1 <= k <= 100`
- `0 <= indexes[i] < s.length`
- `1 <= sources[i].length, targets[i].length <= 50`
- `s` consists of only lowercase English letters.
- `sources[i]` and `targets[i]` consist of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]`
- **Output:** `"eeebffff"`
- **Explanation:** "a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".

### Example 2
- **Input:** `s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]`
- **Output:** `"eeecd"`
- **Explanation:** "ab" occurs at index 0 in s, so we replace it with "eee".
"ec" does not occur at index 2 in s, so we do nothing.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find And Replace in String**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"eeebffff"`.
4. **Verification:** "a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".

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
    def findReplaceString(self, s: str, indices: List[int],
                          sources: List[str], targets: List[str]) -> str:
        match = {}  # start index -> (source length, target)
        for idx, src, tgt in zip(indices, sources, targets):
            if s.startswith(src, idx):
                match[idx] = (len(src), tgt)

        res = []
        i = 0
        while i < len(s):
            if i in match:
                length, tgt = match[i]
                res.append(tgt)
                i += length
            else:
                res.append(s[i])
                i += 1

        return ''.join(res)
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
- [890. Find and Replace Pattern](../../0501-1000/0926-find-and-replace-pattern/)
- [1234. Replace the Substring for Balanced String](../../1001-1500/1351-replace-the-substring-for-balanced-string/)
- [1894. Find the Student that Will Replace the Chalk](../../2001-2500/2006-find-the-student-that-will-replace-the-chalk/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-and-replace-in-string/)
