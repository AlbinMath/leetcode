# LeetCode 3045: Count Prefix and Suffix Pairs II

**LeetCode Problem #3045 — Count Prefix and Suffix Pairs II**
Solve LeetCode Count Prefix and Suffix Pairs II using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Prefix and Suffix Pairs II |
| LeetCode | #3045 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** string array `words`.

Let's define a **boolean** function `isPrefixAndSuffix` that takes two strings, `str1` and `str2`:

`isPrefixAndSuffix(str1, str2)` returns `true` if `str1` is **both** a prefix and a suffix of `str2`, and `false` otherwise.

For example, `isPrefixAndSuffix("aba", "ababa")` is `true` because `"aba"` is a prefix of `"ababa"` and also a suffix, but `isPrefixAndSuffix("abc", "abcd")` is `false`.

Return *an integer denoting the **number** of index pairs *`(i*, *j)`* such that *`i < j`*, and *`isPrefixAndSuffix(words[i], words[j])`* is *`true`*.*

## Constraints
- `1 <= words.length <= 10^5`
- `1 <= words[i].length <= 10^5`
- `words[i]` consists only of lowercase English letters.
- The sum of the lengths of all `words[i]` does not exceed `5 * 10^5`.

## Examples
### Example 1
- **Input:** `words = ["a","aba","ababa","aa"]`
- **Output:** `4`
- **Explanation:** In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("a", "aba") is true.
i = 0 and j = 2 because isPrefixAndSuffix("a", "ababa") is true.
i = 0 and j = 3 because isPrefixAndSuffix("a", "aa") is true.
i = 1 and j = 2 because isPrefixAndSuffix("aba", "ababa") is true.
Therefore, the answer is 4.

### Example 2
- **Input:** `words = ["pa","papa","ma","mama"]`
- **Output:** `2`
- **Explanation:** In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("pa", "papa") is true.
i = 2 and j = 3 because isPrefixAndSuffix("ma", "mama") is true.
Therefore, the answer is 2.

### Example 3
- **Input:** `words = ["abab","ab"]`
- **Output:** `0`
- **Explanation:** In this example, the only valid index pair is i = 0 and j = 1, and isPrefixAndSuffix("abab", "ab") is false.
Therefore, the answer is 0.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Prefix and Suffix Pairs II**, we observe the problem requirements and utilize the **Prefix Sum** technique. By maintaining a **Prefix Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Prefix Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["a","aba","ababa","aa"]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("a", "aba") is true.
i = 0 and j = 2 because isPrefixAndSuffix("a", "ababa") is true.
i = 0 and j = 3 because isPrefixAndSuffix("a", "aa") is true.
i = 1 and j = 2 because isPrefixAndSuffix("aba", "ababa") is true.
Therefore, the answer is 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = [{}]
        cnt = [0]
        ans = 0
        for w in words:
            L = len(w)
            node = 0
            for k in range(L):
                key = (w[k], w[L - 1 - k])
                nxt = trie[node].get(key)
                if nxt is None:
                    trie.append({})
                    cnt.append(0)
                    nxt = len(trie) - 1
                    trie[node][key] = nxt
                node = nxt
                ans += cnt[node]
            cnt[node] += 1
        return ans
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3042. Count Prefix and Suffix Pairs I](../../3001-3500/3042-count-prefix-and-suffix-pairs-i/)
- [745. Prefix and Suffix Search](../../0501-1000/0745-prefix-and-suffix-search/)
- [1782. Count Pairs Of Nodes](../../1501-2000/1782-count-pairs-of-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/)
