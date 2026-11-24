# LeetCode 1048: Longest String Chain

**LeetCode Problem #1048 — Longest String Chain**
Solve LeetCode Longest String Chain using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest String Chain |
| LeetCode | #1048 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of `words` where each word consists of lowercase English letters.

`word_A` is a **predecessor** of `word_B` if and only if we can insert **exactly one** letter anywhere in `word_A` **without changing the order of the other characters** to make it equal to `word_B`.

For example, `"abc"` is a **predecessor** of `"ab a c"`, while `"cba"` is not a **predecessor** of `"bcad"`.

A **word chain*** *is a sequence of words `[word_1, word_2, ..., word_k]` with `k >= 1`, where `word_1` is a **predecessor** of `word_2`, `word_2` is a **predecessor** of `word_3`, and so on. A single word is trivially a **word chain** with `k == 1`.

Return *the **length** of the **longest possible word chain** with words chosen from the given list of *`words`.

## Constraints
- `1 <= words.length <= 1000`
- `1 <= words[i].length <= 16`
- `words[i]` only consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["a","b","ba","bca","bda","bdca"]`
- **Output:** `4`
- **Explanation:** : One of the longest word chains is ["a"," b a","b d a","bd c a"].

### Example 2
- **Input:** `words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]`
- **Output:** `5`
- **Explanation:** All the words can be put in a word chain ["xb", "xb c ", " c xbc", " p cxbc", "pcxbc f "].

### Example 3
- **Input:** `words = ["abcd","dbqca"]`
- **Output:** `1`
- **Explanation:** The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Longest String Chain**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["a","b","ba","bca","bda","bdca"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** : One of the longest word chains is ["a"," b a","b d a","bd c a"].

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
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        best = 1

        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                prev = w[:i] + w[i + 1:]
                if prev in dp:
                    dp[w] = max(dp[w], dp[prev] + 1)
            best = max(best, dp[w])

        return best
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
- [1405. Longest Happy String](../../1001-1500/1304-longest-happy-string/)
- [2745. Construct the Longest New String](../../2501-3000/2850-construct-the-longest-new-string/)
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-string-chain/)
