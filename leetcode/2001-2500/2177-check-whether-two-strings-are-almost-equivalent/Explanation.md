# LeetCode 2068: Check Whether Two Strings are Almost Equivalent

**LeetCode Problem #2068 — Check Whether Two Strings are Almost Equivalent**
Solve LeetCode Check Whether Two Strings are Almost Equivalent using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check Whether Two Strings are Almost Equivalent |
| LeetCode | #2068 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Two strings `word1` and `word2` are considered **almost equivalent** if the differences between the frequencies of each letter from `'a'` to `'z'` between `word1` and `word2` is **at most** `3`.

Given two strings `word1` and `word2`, each of length `n`, return `true` *if *`word1` *and* `word2` *are **almost equivalent**, or* `false` *otherwise*.

The **frequency** of a letter `x` is the number of times it occurs in the string.

## Constraints
- `n == word1.length == word2.length`
- `1 <= n <= 100`
- `word1` and `word2` consist only of lowercase English letters.

## Examples
### Example 1
- **Input:** `word1 = "aaaa", word2 = "bccb"`
- **Output:** `false`
- **Explanation:** There are 4 'a's in "aaaa" but 0 'a's in "bccb".
The difference is 4, which is more than the allowed 3.

### Example 2
- **Input:** `word1 = "abcdeef", word2 = "abaaacc"`
- **Output:** `true`
- **Explanation:** The differences between the frequencies of each letter in word1 and word2 are at most 3:
- 'a' appears 1 time in word1 and 4 times in word2. The difference is 3.
- 'b' appears 1 time in word1 and 1 time in word2. The difference is 0.
- 'c' appears 1 time in word1 and 2 times in word2. The difference is 1.
- 'd' appears 1 time in word1 and 0 times in word2. The difference is 1.
- 'e' appears 2 times in word1 and 0 times in word2. The difference is 2.
- 'f' appears 1 time in word1 and 0 times in word2. The difference is 1.

### Example 3
- **Input:** `word1 = "cccddabba", word2 = "babababab"`
- **Output:** `true`
- **Explanation:** The differences between the frequencies of each letter in word1 and word2 are at most 3:
- 'a' appears 2 times in word1 and 4 times in word2. The difference is 2.
- 'b' appears 2 times in word1 and 5 times in word2. The difference is 3.
- 'c' appears 3 times in word1 and 0 times in word2. The difference is 3.
- 'd' appears 2 times in word1 and 0 times in word2. The difference is 2.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Check Whether Two Strings are Almost Equivalent**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word1 = "aaaa", word2 = "bccb"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** There are 4 'a's in "aaaa" but 0 'a's in "bccb".
The difference is 4, which is more than the allowed 3.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var checkAlmostEquivalent = function(word1, word2) {
    const freq = new Array(26).fill(0);

    for (const ch of word1) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    for (const ch of word2) {
        freq[ch.charCodeAt(0) - 97]--;
    }

    for (const count of freq) {
        if (Math.abs(count) > 3) {
            return false;
        }
    }

    return true;
};
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
- [1662. Check If Two String Arrays are Equivalent](../../1501-2000/1781-check-if-two-string-arrays-are-equivalent/)
- [1657. Determine if Two Strings Are Close](../../1501-2000/1777-determine-if-two-strings-are-close/)
- [3327. Check if DFS Strings Are Palindromes](../../3501-4000/3603-check-if-dfs-strings-are-palindromes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/)
