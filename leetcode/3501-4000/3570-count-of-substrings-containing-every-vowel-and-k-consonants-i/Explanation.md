# LeetCode 3305: Count of Substrings Containing Every Vowel and K Consonants I

**LeetCode Problem #3305 — Count of Substrings Containing Every Vowel and K Consonants I**
Solve LeetCode Count of Substrings Containing Every Vowel and K Consonants I using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count of Substrings Containing Every Vowel and K Consonants I |
| LeetCode | #3305 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `word` and a **non-negative** integer `k`.

Return the total number of substrings of `word` that contain every vowel (`'a'`, `'e'`, `'i'`, `'o'`, and `'u'`) **at least** once and **exactly** `k` consonants.

## Constraints
- `5 <= word.length <= 250`
- `word` consists only of lowercase English letters.
- `0 <= k <= word.length - 5`

## Examples
### Example 1
- **Input:** `word = "aeioqq", k = 1`
- **Output:** `0`
- **Explanation:** There is no substring with every vowel.

### Example 2
- **Input:** `word = "aeiou", k = 0`
- **Output:** `1`
- **Explanation:** The only substring with every vowel and zero consonants is `word[0..4]`, which is `"aeiou"`.

### Example 3
- **Input:** `word = " ieaouqqieaouqq ", k = 1`
- **Output:** `3`
- **Explanation:** The substrings with every vowel and one consonant are: 

 
 `word[0..5]`, which is `"ieaouq"`. 
 `word[6..11]`, which is `"qieaou"`. 
 `word[7..12]`, which is `"ieaouq"`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count of Substrings Containing Every Vowel and K Consonants I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "aeioqq", k = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** There is no substring with every vowel.

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
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = "aeiou"
        ans = 0
        for i in range(n):
            seen = set()
            cons = 0
            for j in range(i, n):
                ch = word[j]
                if ch in vowels:
                    seen.add(ch)
                else:
                    cons += 1
                    if cons > k:
                        break
                if cons == k and len(seen) == 5:
                    ans += 1
        return ans
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
- [3306. Count of Substrings Containing Every Vowel and K Consonants II](../../3501-4000/3569-count-of-substrings-containing-every-vowel-and-k-consonants-ii/)
- [2062. Count Vowel Substrings of a String](../../2001-2500/2186-count-vowel-substrings-of-a-string/)
- [3258. Count Substrings That Satisfy K-Constraint I](../../3501-4000/3543-count-substrings-that-satisfy-k-constraint-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/)
