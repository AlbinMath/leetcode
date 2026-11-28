# LeetCode 3992: Rearrange String to Avoid Character Pair

**LeetCode Problem #3992 — Rearrange String to Avoid Character Pair**
Solve LeetCode Rearrange String to Avoid Character Pair using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rearrange String to Avoid Character Pair |
| LeetCode | #3992 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` and two distinct lowercase English letters `x` and `y`.

Rearrange the characters of `s` to construct a new string `t` such that:

`t` is a permutation of `s`. 
 Every occurrence of `y` appears before every occurrence of `x` in `t`.

Return any valid string `t`.

## Constraints
- `1 <= s.length <= 100`
- `s` consists of lowercase English letters.
- `x` and `y` are lowercase English letters.
- `x != y`

## Examples
### Example 1
- **Input:** `s = "aabc", x = "a", y = "c"`
- **Output:** `"cbaa"`
- **Explanation:** The string `"cbaa"` is a permutation of `"aabc"`, and every occurrence of `'c'` appears before every occurrence of `'a'`.

### Example 2
- **Input:** `s = "dcab", x = "d", y = "b"`
- **Output:** `"cabd"`
- **Explanation:** The string `"cabd"` is a permutation of `"dcab"`, and every occurrence of `'b'` appears before every occurrence of `'d'`.

### Example 3
- **Input:** `s = "axe", x = "o", y = "x"`
- **Output:** `"axe"`
- **Explanation:** The string `"axe"` is already valid. Since `'o'` does not occur in the string, the required condition is automatically satisfied.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Rearrange String to Avoid Character Pair**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aabc", x = "a", y = "c"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"cbaa"`.
4. **Verification:** The string `"cbaa"` is a permutation of `"aabc"`, and every occurrence of `'c'` appears before every occurrence of `'a'`.

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
var rearrangeString = function(s, x, y) {
    let other = "";
    let xChars = "";
    let yChars = "";

    for (const ch of s) {
        if (ch === y) {
            yChars += ch;
        } else if (ch === x) {
            xChars += ch;
        } else {
            other += ch;
        }
    }

    return other + yChars + xChars;
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
- [387. First Unique Character in a String](../../0001-0500/0387-first-unique-character-in-a-string/)
- [3304. Find the K-th Character in String Game I](../../3001-3500/3304-find-the-k-th-character-in-string-game-i/)
- [3307. Find the K-th Character in String Game II](../../3001-3500/3307-find-the-k-th-character-in-string-game-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/)
