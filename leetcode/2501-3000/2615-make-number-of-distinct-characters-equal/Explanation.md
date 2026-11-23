# LeetCode 2531: Make Number of Distinct Characters Equal

**LeetCode Problem #2531 — Make Number of Distinct Characters Equal**
Solve LeetCode Make Number of Distinct Characters Equal using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make Number of Distinct Characters Equal |
| LeetCode | #2531 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **0-indexed** strings `word1` and `word2`.

A **move** consists of choosing two indices `i` and `j` such that `0 <= i < word1.length` and `0 <= j < word2.length` and swapping `word1[i]` with `word2[j]`.

Return `true` *if it is possible to get the number of distinct characters in* `word1` *and* `word2` *to be equal with **exactly one** move. *Return `false` *otherwise*.

## Constraints
- `1 <= word1.length, word2.length <= 10^5`
- `word1` and `word2` consist of only lowercase English letters.

## Examples
### Example 1
- **Input:** `word1 = "ac", word2 = "b"`
- **Output:** `false`
- **Explanation:** Any pair of swaps would yield two distinct characters in the first string, and one in the second string.

### Example 2
- **Input:** `word1 = "abcc", word2 = "aab"`
- **Output:** `true`
- **Explanation:** We swap index 2 of the first string with index 0 of the second string. The resulting strings are word1 = "abac" and word2 = "cab", which both have 3 distinct characters.

### Example 3
- **Input:** `word1 = "abcde", word2 = "fghij"`
- **Output:** `true`
- **Explanation:** Both resulting strings will have 5 distinct characters, regardless of which indices we swap.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Make Number of Distinct Characters Equal**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word1 = "ac", word2 = "b"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** Any pair of swaps would yield two distinct characters in the first string, and one in the second string.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import Counter

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        d1, d2 = len(count1), len(count2)
        
        for ch1 in count1:
            for ch2 in count2:
                if ch1 == ch2:
                    if d1 == d2:
                        return True
                else:
                    new_d1 = d1 - (count1[ch1] == 1) + (count1[ch2] == 0)
                    new_d2 = d2 - (count2[ch2] == 1) + (count2[ch1] == 0)
                    if new_d1 == new_d2:
                        return True
                        
        return False
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1897. Redistribute Characters to Make All Strings Equal](../../2001-2500/2025-redistribute-characters-to-make-all-strings-equal/)
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2753-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../3001-3500/3249-minimum-number-of-operations-to-make-array-xor-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-number-of-distinct-characters-equal/)
