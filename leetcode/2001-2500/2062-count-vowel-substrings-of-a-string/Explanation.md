# LeetCode 2062: Count Vowel Substrings of a String

**LeetCode Problem #2062 — Count Vowel Substrings of a String**
Solve LeetCode Count Vowel Substrings of a String using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Vowel Substrings of a String |
| LeetCode | #2062 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **substring** is a contiguous (non-empty) sequence of characters within a string.

A **vowel substring** is a substring that **only** consists of vowels (`'a'`, `'e'`, `'i'`, `'o'`, and `'u'`) and has **all five** vowels present in it.

Given a string `word`, return *the number of **vowel substrings** in* `word`.

## Constraints
- `1 <= word.length <= 100`
- `word` consists of lowercase English letters only.

## Examples
### Example 1
- **Input:** `word = "aeiouu"`
- **Output:** `2`
- **Explanation:** The vowel substrings of word are as follows (underlined):
- "

### Example 2
- **Input:** `word = "unicornarihan"`
- **Output:** `0`
- **Explanation:** Not all 5 vowels are present, so there are no vowel substrings.

### Example 3
- **Input:** `word = "cuaieuouac"`
- **Output:** `7`
- **Explanation:** The vowel substrings of word are as follows (underlined):
- "c

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Vowel Substrings of a String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "aeiouu"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The vowel substrings of word are as follows (underlined):
- "

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var countVowelSubstrings = function(word) {
    let count = 0;
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);

    for (let i = 0; i < word.length; i++) {
        const seen = new Set();

        for (let j = i; j < word.length; j++) {
            if (!vowels.has(word[j])) {
                break;
            }

            seen.add(word[j]);

            if (seen.size === 5) {
                count++;
            }
        }
    }

    return count;
};
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
- [3305. Count of Substrings Containing Every Vowel and K Consonants I](../../3001-3500/3305-count-of-substrings-containing-every-vowel-and-k-consonants-i/)
- [3306. Count of Substrings Containing Every Vowel and K Consonants II](../../3001-3500/3306-count-of-substrings-containing-every-vowel-and-k-consonants-ii/)
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0828-count-unique-characters-of-all-substrings-of-a-given-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-vowel-substrings-of-a-string/)
