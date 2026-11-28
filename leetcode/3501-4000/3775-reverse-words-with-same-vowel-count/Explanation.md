# LeetCode 3775: Reverse Words With Same Vowel Count

**LeetCode Problem #3775 — Reverse Words With Same Vowel Count**
Solve LeetCode Reverse Words With Same Vowel Count using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reverse Words With Same Vowel Count |
| LeetCode | #3775 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting of lowercase English words, each separated by a single space.

Determine how many vowels appear in the **first** word. Then, reverse each following word that has the **same vowel count**. Leave all remaining words unchanged.

Return the resulting string.

Vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters and spaces.
- Words in `s` are separated by a **single** space.
- `s` does **not** contain leading or trailing spaces.

## Examples
### Example 1
- **Input:** `s = "cat and mice"`
- **Output:** `"cat dna mice"`
- **Explanation:** ​​​​​​​ 

 
 The first word `"cat"` has 1 vowel. 
 `"and"` has 1 vowel, so it is reversed to form `"dna"`. 
 `"mice"` has 2 vowels, so it remains unchanged. 
 Thus, the resulting string is `"cat dna mice"`.

### Example 2
- **Input:** `s = "book is nice"`
- **Output:** `"book is ecin"`
- **Explanation:** The first word `"book"` has 2 vowels. 
 `"is"` has 1 vowel, so it remains unchanged. 
 `"nice"` has 2 vowels, so it is reversed to form `"ecin"`. 
 Thus, the resulting string is `"book is ecin"`.

### Example 3
- **Input:** `s = "banana healthy"`
- **Output:** `"banana healthy"`
- **Explanation:** The first word `"banana"` has 3 vowels. 
 `"healthy"` has 2 vowels, so it remains unchanged. 
 Thus, the resulting string is `"banana healthy"`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reverse Words With Same Vowel Count**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "cat and mice"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"cat dna mice"`.
4. **Verification:** ​​​​​​​ 

 
 The first word `"cat"` has 1 vowel. 
 `"and"` has 1 vowel, so it is reversed to form `"dna"`. 
 `"mice"` has 2 vowels, so it remains unchanged. 
 Thus, the resulting string is `"cat dna mice"`.

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
    def reverseWords(self, s: str) -> str:
        vowels = set("aeiou")
        words = s.split(' ')

        def count(w: str) -> int:
            return sum(c in vowels for c in w)

        target = count(words[0])
        for i in range(1, len(words)):
            if count(words[i]) == target:
                words[i] = words[i][::-1]
        return ' '.join(words)
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
- [1641. Count Sorted Vowel Strings](../../1501-2000/1641-count-sorted-vowel-strings/)
- [2062. Count Vowel Substrings of a String](../../2001-2500/2062-count-vowel-substrings-of-a-string/)
- [2559. Count Vowel Strings in Ranges](../../2501-3000/2559-count-vowel-strings-in-ranges/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reverse-words-with-same-vowel-count/)
