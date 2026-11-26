# LeetCode 3813: Vowel-Consonant Score

**LeetCode Problem #3813 — Vowel-Consonant Score**
Solve LeetCode Vowel-Consonant Score using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Vowel-Consonant Score |
| LeetCode | #3813 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting of lowercase English letters, spaces, and digits.

Let `v` be the number of vowels in `s` and `c` be the number of consonants in `s`.

A vowel is one of the letters `'a'`, `'e'`, `'i'`, `'o'`, or `'u'`, while any other letter in the English alphabet is considered a consonant.

The **score** of the string `s` is defined as follows:

If `c > 0`, the `score = floor(v / c)` where floor denotes **rounding down** to the nearest integer. 
 Otherwise, the `score = 0`.

Return an integer denoting the score of the string.

## Constraints
- `1 <= s.length <= 100`
- `s` consists of lowercase English letters, spaces and digits.

## Examples
### Example 1
- **Input:** `s = "cooear"`
- **Output:** `2`
- **Explanation:** The string `s = "cooear"` contains `v = 4` vowels `('o', 'o', 'e', 'a')` and `c = 2` consonants `('c', 'r')`. 

 The score is `floor(v / c) = floor(4 / 2) = 2`.

### Example 2
- **Input:** `s = "axeyizou"`
- **Output:** `1`
- **Explanation:** The string `s = "axeyizou"` contains `v = 5` vowels `('a', 'e', 'i', 'o', 'u')` and `c = 3` consonants `('x', 'y', 'z')`. 

 The score is `floor(v / c) = floor(5 / 3) = 1`.

### Example 3
- **Input:** `s = "au 123"`
- **Output:** `0`
- **Explanation:** The string `s = "au 123"` contains no consonants `(c = 0)`, so the score is 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Vowel-Consonant Score**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "cooear"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The string `s = "cooear"` contains `v = 4` vowels `('o', 'o', 'e', 'a')` and `c = 2` consonants `('c', 'r')`. 

 The score is `floor(v / c) = floor(4 / 2) = 2`.

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
    def vowelConsonantScore(self, s: str) -> int:
        v = c = 0
        for ch in s:
            if ch in "aeiou":
                v += 1
            elif ch.isalpha():
                c += 1
        return v // c if c > 0 else 0
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
- [3541. Find Most Frequent Vowel and Consonant](../../3501-4000/3541-find-most-frequent-vowel-and-consonant/)
- [966. Vowel Spellchecker](../../0501-1000/0966-vowel-spellchecker/)
- [1641. Count Sorted Vowel Strings](../../1501-2000/1641-count-sorted-vowel-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/vowel-consonant-score/)
