# LeetCode 524: Longest Word in Dictionary through Deleting

**LeetCode Problem #524 — Longest Word in Dictionary through Deleting**
Solve LeetCode Longest Word in Dictionary through Deleting using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Word in Dictionary through Deleting |
| LeetCode | #524 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s` and a string array `dictionary`, return *the longest string in the dictionary that can be formed by deleting some of the given string characters*. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

## Constraints
- `1 <= s.length <= 1000`
- `1 <= dictionary.length <= 1000`
- `1 <= dictionary[i].length <= 1000`
- `s` and `dictionary[i]` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]`
- **Output:** `"apple"`

### Example 2
- **Input:** `s = "abpcplea", dictionary = ["a","b","c"]`
- **Output:** `"a"`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Longest Word in Dictionary through Deleting**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"apple"`.

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
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subseq(word: str) -> bool:
            it = iter(s)
            return all(ch in it for ch in word)

        best = ""
        for word in dictionary:
            if len(word) < len(best):
                continue
            if len(word) == len(best) and word >= best:
                continue
            if is_subseq(word):
                best = word
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
- [720. Longest Word in Dictionary](../../0501-1000/0720-longest-word-in-dictionary/)
- [1493. Longest Subarray of 1's After Deleting One Element](../../1001-1500/1493-longest-subarray-of-1s-after-deleting-one-element/)
- [676. Implement Magic Dictionary](../../0501-1000/0676-implement-magic-dictionary/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/)
