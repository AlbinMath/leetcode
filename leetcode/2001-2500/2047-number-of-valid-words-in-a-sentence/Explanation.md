# LeetCode 2047: Number of Valid Words in a Sentence

**LeetCode Problem #2047 — Number of Valid Words in a Sentence**
Solve LeetCode Number of Valid Words in a Sentence using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Valid Words in a Sentence |
| LeetCode | #2047 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A sentence consists of lowercase letters (`'a'` to `'z'`), digits (`'0'` to `'9'`), hyphens (`'-'`), punctuation marks (`'!'`, `'.'`, and `','`), and spaces (`' '`) only. Each sentence can be broken down into **one or more tokens** separated by one or more spaces `' '`.

A token is a valid word if **all three** of the following are true:

It only contains lowercase letters, hyphens, and/or punctuation (**no** digits). 
 There is **at most one** hyphen `'-'`. If present, it **must** be surrounded by lowercase characters (`"a-b"` is valid, but `"-ab"` and `"ab-"` are not valid). 
 There is **at most one** punctuation mark. If present, it **must** be at the **end** of the token (`"ab,"`, `"cd!"`, and `"."` are valid, but `"a!b"` and `"c.,"` are not valid).

Examples of valid words include `"a-b."`, `"afad"`, `"ba-c"`, `"a!"`, and `"!"`.

Given a string `sentence`, return *the **number** of valid words in *`sentence`.

## Constraints
- `1 <= sentence.length <= 1000`
- `sentence` only contains lowercase English letters, digits, `' '`, `'-'`, `'!'`, `'.'`, and `','`.
- There will be at least `1` token.

## Examples
### Example 1
- **Input:** `sentence = " cat and dog "`
- **Output:** `3`
- **Explanation:** The valid words in the sentence are "cat", "and", and "dog".

### Example 2
- **Input:** `sentence = "!this 1-s b8d!"`
- **Output:** `0`
- **Explanation:** There are no valid words in the sentence.
"!this" is invalid because it starts with a punctuation mark.
"1-s" and "b8d" are invalid because they contain digits.

### Example 3
- **Input:** `sentence = " alice and bob are playing stone-game10"`
- **Output:** `5`
- **Explanation:** The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
"stone-game10" is invalid because it contains digits.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Valid Words in a Sentence**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `sentence = " cat and dog "`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The valid words in the sentence are "cat", "and", and "dog".

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
var countValidWords = function(sentence) {
    const tokens = sentence.split(" ");
    let count = 0;

    for (const word of tokens) {
        if (word === "") continue;

        // No digits allowed.
        if (/\d/.test(word)) continue;

        // At most one hyphen, surrounded by lowercase letters.
        if (word.includes("-")) {
            if (!/^[a-z]+(-[a-z]+)?[!.,]?$/.test(word)) {
                continue;
            }
        }

        // Punctuation is allowed only once, at the end.
        if (!/^[a-z-]*[!.,]?$/.test(word)) continue;

        const punctuationCount = (word.match(/[!.,]/g) || []).length;
        const hyphenCount = (word.match(/-/g) || []).length;

        if (punctuationCount > 1 || hyphenCount > 1) continue;

        // A hyphen must have lowercase letters on both sides.
        if (word.includes("-") && !/[a-z]-[a-z]/.test(word)) {
            continue;
        }

        count++;
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
- [1178. Number of Valid Words for Each Puzzle](../../1001-1500/1178-number-of-valid-words-for-each-puzzle/)
- [65. Valid Number](../../0001-0500/0065-valid-number/)
- [611. Valid Triangle Number](../../0501-1000/0611-valid-triangle-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-valid-words-in-a-sentence/)
