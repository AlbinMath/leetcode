# LeetCode 1003: Check If Word Is Valid After Substitutions

**LeetCode Problem #1003 — Check If Word Is Valid After Substitutions**
Solve LeetCode Check If Word Is Valid After Substitutions using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check If Word Is Valid After Substitutions |
| LeetCode | #1003 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s`, determine if it is **valid**.

A string `s` is **valid** if, starting with an empty string `t = ""`, you can **transform **`t`** into **`s` after performing the following operation **any number of times**:

Insert string `"abc"` into any position in `t`. More formally, `t` becomes `t_left + "abc" + t_right`, where `t == t_left + t_right`. Note that `t_left` and `t_right` may be **empty**.

Return `true` *if *`s`* is a **valid** string, otherwise, return* `false`.

## Constraints
- `1 <= s.length <= 2 * 10^4`
- `s` consists of letters `'a'`, `'b'`, and `'c'`

## Examples
### Example 1
- **Input:** `s = "aabcbc"`
- **Output:** `true`
- **Explanation:** "" -> " abc " -> "a abc bc"
Thus, "aabcbc" is valid.

### Example 2
- **Input:** `s = "abcabcababcc"`
- **Output:** `true`
- **Explanation:** "" -> " abc " -> "abc abc " -> "abcabc abc " -> "abcabcab abc c"
Thus, "abcabcababcc" is valid.

### Example 3
- **Input:** `s = "abccba"`
- **Output:** `false`
- **Explanation:** It is impossible to get "abccba" using the operation.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check If Word Is Valid After Substitutions**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aabcbc"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** "" -> " abc " -> "a abc bc"
Thus, "aabcbc" is valid.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var isValid = function(s) {
    const stack = [];

    for (let ch of s) {
        stack.push(ch);

        // Check whether the last three characters are "abc"
        const n = stack.length;

        if (
            n >= 3 &&
            stack[n - 3] === 'a' &&
            stack[n - 2] === 'b' &&
            stack[n - 1] === 'c'
        ) {
            // Remove "abc"
            stack.pop();
            stack.pop();
            stack.pop();
        }
    }

    return stack.length === 0;
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence](../../1501-2000/1566-check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)
- [1880. Check if Word Equals Summation of Two Words](../../2001-2500/2010-check-if-word-equals-summation-of-two-words/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/)
