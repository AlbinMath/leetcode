# LeetCode 828: Count Unique Characters of All Substrings of a Given String

**LeetCode Problem #828 — Count Unique Characters of All Substrings of a Given String**
Solve LeetCode Count Unique Characters of All Substrings of a Given String using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Unique Characters of All Substrings of a Given String |
| LeetCode | #828 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Let's define a function `countUniqueChars(s)` that returns the number of unique characters in `s`.

For example, calling `countUniqueChars(s)` if `s = "LEETCODE"` then `"L"`, `"T"`, `"C"`, `"O"`, `"D"` are the unique characters since they appear only once in `s`, therefore `countUniqueChars(s) = 5`.

Given a string `s`, return the sum of `countUniqueChars(t)` where `t` is a substring of `s`. The test cases are generated such that the answer fits in a 32-bit integer.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of uppercase English letters only.

## Examples
### Example 1
- **Input:** `s = "ABC"`
- **Output:** `10`
- **Explanation:** All possible substrings are: "A","B","C","AB","BC" and "ABC".
Every substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

### Example 2
- **Input:** `s = "ABA"`
- **Output:** `8`
- **Explanation:** The same as

### Example 3
- **Input:** `s = "LEETCODE"`
- **Output:** `92`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Unique Characters of All Substrings of a Given String**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "ABC"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** All possible substrings are: "A","B","C","AB","BC" and "ABC".
Every substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

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
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        last = [-1] * 26        # most recent index of each letter
        prev = [0] * n

        # pass 1: previous occurrence of each position
        for i, ch in enumerate(s):
            c = ord(ch) - 65
            prev[i] = last[c]
            last[c] = i

        # pass 2: next occurrence, accumulate contributions
        nxt = [n] * 26
        total = 0
        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - 65
            total += (i - prev[i]) * (nxt[c] - i)
            nxt[c] = i

        return total
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
- [467. Unique Substrings in Wraparound String](../../0001-0500/0467-unique-substrings-in-wraparound-string/)
- [1239. Maximum Length of a Concatenated String with Unique Characters](../../1001-1500/1360-maximum-length-of-a-concatenated-string-with-unique-characters/)
- [1593. Split a String Into the Max Number of Unique Substrings](../../1501-2000/1715-split-a-string-into-the-max-number-of-unique-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/)
