# LeetCode 3085: Minimum Deletions to Make String K-Special

**LeetCode Problem #3085 — Minimum Deletions to Make String K-Special**
Solve LeetCode Minimum Deletions to Make String K-Special using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Deletions to Make String K-Special |
| LeetCode | #3085 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `word` and an integer `k`.

We consider `word` to be **k-special** if `|freq(word[i]) - freq(word[j])| <= k` for all indices `i` and `j` in the string.

Here, `freq(x)` denotes the frequency of the character `x` in `word`, and `|y|` denotes the absolute value of `y`.

Return *the **minimum** number of characters you need to delete to make* `word` ***k-special***.

## Constraints
- `1 <= word.length <= 10^5`
- `0 <= k <= 10^5`
- `word` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `word = "aabcaba", k = 0`
- **Output:** `3`
- **Explanation:** We can make `word` `0`-special by deleting `2` occurrences of `"a"` and `1` occurrence of `"c"`. Therefore, `word` becomes equal to `"baba"` where `freq('a') == freq('b') == 2`.

### Example 2
- **Input:** `word = "dabdcbdcdcd", k = 2`
- **Output:** `2`
- **Explanation:** We can make `word` `2`-special by deleting `1` occurrence of `"a"` and `1` occurrence of `"d"`. Therefore, `word` becomes equal to "bdcbdcdcd" where `freq('b') == 2`, `freq('c') == 3`, and `freq('d') == 4`.

### Example 3
- **Input:** `word = "aaabaaa", k = 2`
- **Output:** `1`
- **Explanation:** We can make `word` `2`-special by deleting `1` occurrence of `"b"`. Therefore, `word` becomes equal to `"aaaaaa"` where each letter's frequency is now uniformly `6`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Deletions to Make String K-Special**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "aabcaba", k = 0`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We can make `word` `0`-special by deleting `2` occurrences of `"a"` and `1` occurrence of `"c"`. Therefore, `word` becomes equal to `"baba"` where `freq('a') == freq('b') == 2`.

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
    def minimumDeletions(self, word: str, k: int) -> int:
        freqs = list(Counter(word).values())
        min_deletions = len(word)
        
        for base in freqs:
            deletions = 0
            max_allowed = base + k
            
            for f in freqs:
                if f < base:
                    deletions += f
                elif f > max_allowed:
                    deletions += f - max_allowed
                    
            if deletions < min_deletions:
                min_deletions = deletions
                
        return min_deletions
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
- [1653. Minimum Deletions to Make String Balanced](../../1501-2000/1653-minimum-deletions-to-make-string-balanced/)
- [2844. Minimum Operations to Make a Special Number](../../2501-3000/2844-minimum-operations-to-make-a-special-number/)
- [1312. Minimum Insertion Steps to Make a String Palindrome](../../1001-1500/1312-minimum-insertion-steps-to-make-a-string-palindrome/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/)
