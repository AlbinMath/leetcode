# LeetCode 1639: Number of Ways to Form a Target String Given a Dictionary

**LeetCode Problem #1639 — Number of Ways to Form a Target String Given a Dictionary**
Solve LeetCode Number of Ways to Form a Target String Given a Dictionary using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways to Form a Target String Given a Dictionary |
| LeetCode | #1639 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a list of strings of the **same length** `words` and a string `target`.

Your task is to form `target` using the given `words` under the following rules:

`target` should be formed from left to right. 
 To form the `i^th` character (**0-indexed**) of `target`, you can choose the `k^th` character of the `j^th` string in `words` if `target[i] = words[j][k]`. 
 Once you use the `k^th` character of the `j^th` string of `words`, you **can no longer** use the `x^th` character of any string in `words` where `x <= k`. In other words, all characters to the left of or at index `k` become unusuable for every string. 
 Repeat the process until you form the string `target`.

**Notice** that you can use **multiple characters** from the **same string** in `words` provided the conditions above are met.

Return *the number of ways to form `target` from `words`*. Since the answer may be too large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= words.length <= 1000`
- `1 <= words[i].length <= 1000`
- All strings in `words` have the same length.
- `1 <= target.length <= 1000`
- `words[i]` and `target` contain only lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["acca","bbbb","caca"], target = "aba"`
- **Output:** `6`
- **Explanation:** There are 6 ways to form target.
"aba" -> index 0 (" a cca"), index 1 ("b b bb"), index 3 ("cac a ")
"aba" -> index 0 (" a cca"), index 2 ("bb b b"), index 3 ("cac a ")
"aba" -> index 0 (" a cca"), index 1 ("b b bb"), index 3 ("acc a ")
"aba" -> index 0 (" a cca"), index 2 ("bb b b"), index 3 ("acc a ")
"aba" -> index 1 ("c a ca"), index 2 ("bb b b"), index 3 ("acc a ")
"aba" -> index 1 ("c a ca"), index 2 ("bb b b"), index 3 ("cac a ")

### Example 2
- **Input:** `words = ["abba","baab"], target = "bab"`
- **Output:** `4`
- **Explanation:** There are 4 ways to form target.
"bab" -> index 0 (" b aab"), index 1 ("b a ab"), index 2 ("ab b a")
"bab" -> index 0 (" b aab"), index 1 ("b a ab"), index 3 ("baa b ")
"bab" -> index 0 (" b aab"), index 2 ("ba a b"), index 3 ("baa b ")
"bab" -> index 1 ("a b ba"), index 2 ("ba a b"), index 3 ("baa b ")

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number of Ways to Form a Target String Given a Dictionary**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["acca","bbbb","caca"], target = "aba"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** There are 6 ways to form target.
"aba" -> index 0 (" a cca"), index 1 ("b b bb"), index 3 ("cac a ")
"aba" -> index 0 (" a cca"), index 2 ("bb b b"), index 3 ("cac a ")
"aba" -> index 0 (" a cca"), index 1 ("b b bb"), index 3 ("acc a ")
"aba" -> index 0 (" a cca"), index 2 ("bb b b"), index 3 ("acc a ")
"aba" -> index 1 ("c a ca"), index 2 ("bb b b"), index 3 ("acc a ")
"aba" -> index 1 ("c a ca"), index 2 ("bb b b"), index 3 ("cac a ")

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
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m = len(words[0])
        n = len(target)

        # cnt[k][c]: number of words with letter c at column k
        cnt = [[0] * 26 for _ in range(m)]
        for w in words:
            for k, ch in enumerate(w):
                cnt[k][ord(ch) - 97] += 1

        dp = [0] * (n + 1)
        dp[0] = 1

        for k in range(m):
            row = cnt[k]
            # iterate i downward so column k is used for at most one target char
            for i in range(min(k, n - 1), -1, -1):
                c = row[ord(target[i]) - 97]
                if c and dp[i]:
                    dp[i + 1] = (dp[i + 1] + dp[i] * c) % MOD

        return dp[n]
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
- [1525. Number of Good Ways to Split a String](../../1501-2000/1525-number-of-good-ways-to-split-a-string/)
- [1573. Number of Ways to Split a String](../../1501-2000/1573-number-of-ways-to-split-a-string/)
- [3365. Rearrange K Substrings to Form Target String](../../3001-3500/3365-rearrange-k-substrings-to-form-target-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/)
