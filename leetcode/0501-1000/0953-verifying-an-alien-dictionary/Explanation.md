# LeetCode 953: Verifying an Alien Dictionary

**LeetCode Problem #953 — Verifying an Alien Dictionary**
Solve LeetCode Verifying an Alien Dictionary using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Verifying an Alien Dictionary |
| LeetCode | #953 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different `order`. The `order` of the alphabet is some permutation of lowercase letters.

Given a sequence of `words` written in the alien language, and the `order` of the alphabet, return `true` if and only if the given `words` are sorted lexicographically in this alien language.

## Constraints
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 20`
- `order.length == 26`
- All characters in `words[i]` and `order` are English lowercase letters.

## Examples
### Example 1
- **Input:** `words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"`
- **Output:** `true`
- **Explanation:** As 'h' comes before 'l' in this language, then the sequence is sorted.

### Example 2
- **Input:** `words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"`
- **Output:** `false`
- **Explanation:** As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

### Example 3
- **Input:** `words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"`
- **Output:** `false`
- **Explanation:** The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '&empty;', where '&empty;' is defined as the blank character which is less than any other character ( More info ).

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Verifying an Alien Dictionary**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** As 'h' comes before 'l' in this language, then the sequence is sorted.

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
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {char: i for i, char in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if rank[word1[j]] > rank[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False

        return True
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
- [524. Longest Word in Dictionary through Deleting](../../0501-1000/0524-longest-word-in-dictionary-through-deleting/)
- [676. Implement Magic Dictionary](../../0501-1000/0676-implement-magic-dictionary/)
- [720. Longest Word in Dictionary](../../0501-1000/0720-longest-word-in-dictionary/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/verifying-an-alien-dictionary/)
