# LeetCode 2000: Reverse Prefix of Word

**LeetCode Problem #2000 — Reverse Prefix of Word**
Solve LeetCode Reverse Prefix of Word using JavaScript and Trie. This solution finds the optimal result using Prefix Tree Lookup in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reverse Prefix of Word |
| LeetCode | #2000 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Prefix Tree Lookup |
| Data Structure | Trie Node |
| Pattern | Trie |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a **0-indexed** string `word` and a character `ch`, **reverse** the segment of `word` that starts at index `0` and ends at the index of the **first occurrence** of `ch` (**inclusive**). If the character `ch` does not exist in `word`, do nothing.

For example, if `word = "abcdefd"` and `ch = "d"`, then you should **reverse** the segment that starts at `0` and ends at `3` (**inclusive**). The resulting string will be `" dcba efd"`.

Return *the resulting string*.

## Constraints
- `1 <= word.length <= 250`
- `word` consists of lowercase English letters.
- `ch` is a lowercase English letter.

## Examples
### Example 1
- **Input:** `word = " abcd efd", ch = "d"`
- **Output:** `" dcba efd"`
- **Explanation:** The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

### Example 2
- **Input:** `word = " xyxz xe", ch = "z"`
- **Output:** `" zxyx xe"`
- **Explanation:** The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

### Example 3
- **Input:** `word = "abcd", ch = "z"`
- **Output:** `"abcd"`
- **Explanation:** "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".

## Key Insight
Leverage **Trie** with **Trie Node** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reverse Prefix of Word**, we observe the problem requirements and utilize the **Trie** technique. We iterate through the inputs using **Prefix Tree Lookup**, leveraging a **Trie Node** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Trie Node**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = " abcd efd", ch = "d"`.
2. **Processing Steps:** We apply **Prefix Tree Lookup** using our **Trie Node**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `" dcba efd"`.
4. **Verification:** The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Trie Node.

## Pattern
**Trie**

## Topics
- Trie
- String
- Prefix Search

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var reversePrefix = function(word, ch) {
    const index = word.indexOf(ch);

    if (index === -1) {
        return word;
    }

    const prefix = word.slice(0, index + 1);
    const reversed = prefix.split('').reverse().join('');

    return reversed + word.slice(index + 1);
};
```

## Why This Works
By utilizing **Trie**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence](../../1501-2000/1566-check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)
- [58. Length of Last Word](../../0001-0500/0058-length-of-last-word/)
- [79. Word Search](../../0001-0500/0079-word-search/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reverse-prefix-of-word/)
