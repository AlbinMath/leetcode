# LeetCode 1839: Longest Substring Of All Vowels in Order

**LeetCode Problem #1839 — Longest Substring Of All Vowels in Order**
Solve LeetCode Longest Substring Of All Vowels in Order using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Substring Of All Vowels in Order |
| LeetCode | #1839 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A string is considered **beautiful** if it satisfies the following conditions:

Each of the 5 English vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`) must appear **at least once** in it. 
 The letters must be sorted in **alphabetical order** (i.e. all `'a'`s before `'e'`s, all `'e'`s before `'i'`s, etc.).

For example, strings `"aeiou"` and `"aaaaaaeiiiioou"` are considered **beautiful**, but `"uaeio"`, `"aeoiu"`, and `"aaaeeeooo"` are **not beautiful**.

Given a string `word` consisting of English vowels, return *the **length of the longest beautiful substring** of *`word`*. If no such substring exists, return *`0`.

A **substring** is a contiguous sequence of characters in a string.

## Constraints
- `1 <= word.length <= 5 * 10^5`
- `word` consists of characters `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

## Examples
### Example 1
- **Input:** `word = "aeiaaio aaaaeiiiiouuu ooaauuaeiu"`
- **Output:** `13`

### Example 2
- **Input:** `word = "aeeeiiiioooauuu aeiou "`
- **Output:** `5`

### Example 3
- **Input:** `word = "a"`
- **Output:** `0`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Substring Of All Vowels in Order**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "aeiaaio aaaaeiiiiouuu ooaauuaeiu"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.

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
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        curr_len = 1
        distinct = 1
        max_len = 0
        
        for i in range(1, len(word)):
            if word[i] > word[i - 1]:
                curr_len += 1
                distinct += 1
            elif word[i] == word[i - 1]:
                curr_len += 1
            else:
                curr_len = 1
                distinct = 1
                
            if distinct == 5 and curr_len > max_len:
                max_len = curr_len
                
        return max_len
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
- [1371. Find the Longest Substring Containing Vowels in Even Counts](../../1001-1500/1473-find-the-longest-substring-containing-vowels-in-even-counts/)
- [30. Substring with Concatenation of All Words](../../0001-0500/0030-substring-with-concatenation-of-all-words/)
- [1910. Remove All Occurrences of a Substring](../../2001-2500/2021-remove-all-occurrences-of-a-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/)
