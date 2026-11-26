# LeetCode 745: Prefix and Suffix Search

**LeetCode Problem #745 — Prefix and Suffix Search**
Solve LeetCode Prefix and Suffix Search using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Prefix and Suffix Search |
| LeetCode | #745 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Design a special dictionary that searches the words in it by a prefix and a suffix.

Implement the `WordFilter` class:

`WordFilter(string[] words)` Initializes the object with the `words` in the dictionary. 
 `f(string pref, string suff)` Returns *the index of the word in the dictionary,* which has the prefix `pref` and the suffix `suff`. If there is more than one valid index, return **the largest** of them. If there is no such word in the dictionary, return `-1`.

## Constraints
- `1 <= words.length <= 10^4`
- `1 <= words[i].length <= 7`
- `1 <= pref.length, suff.length <= 7`
- `words[i]`, `pref` and `suff` consist of lowercase English letters only.
- At most `10^4` calls will be made to the function `f`.

## Examples
### Example 1
- **Input:** `["WordFilter", "f"]
[[["apple"]], ["a", "e"]]`
- **Output:** `[null, 0]`
- **Explanation:** WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Prefix and Suffix Search**, we observe the problem requirements and utilize the **Prefix Sum** technique. By maintaining a **Prefix Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Prefix Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["WordFilter", "f"]
[[["apple"]], ["a", "e"]]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, 0]`.
4. **Verification:** WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".

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
class WordFilter:

    def __init__(self, words: list[str]):
        self.table = {}
        for idx, w in enumerate(words):
            n = len(w)
            for i in range(1, n + 1):
                pre = w[:i]
                for j in range(n):
                    self.table[pre + '#' + w[j:]] = idx

    def f(self, pref: str, suff: str) -> int:
        return self.table.get(pref + '#' + suff, -1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
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
- [3045. Count Prefix and Suffix Pairs II](../../3001-3500/3045-count-prefix-and-suffix-pairs-ii/)
- [1529. Minimum Suffix Flips](../../1501-2000/1529-minimum-suffix-flips/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/prefix-and-suffix-search/)
