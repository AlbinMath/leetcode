# LeetCode 3271: Hash Divided String

**LeetCode Problem #3271 — Hash Divided String**
Solve LeetCode Hash Divided String using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Hash Divided String |
| LeetCode | #3271 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` of length `n` and an integer `k`, where `n` is a **multiple** of `k`. Your task is to hash the string `s` into a new string called `result`, which has a length of `n / k`.

First, divide `s` into `n / k` ** substrings **, each with a length of `k`. Then, initialize `result` as an **empty** string.

For each **substring** in order from the beginning:

The **hash value** of a character is the index of that characte r in the **English alphabet** (e.g., `'a' &rarr; 0`, `'b' &rarr; 1`, ..., `'z' &rarr; 25`). 
 Calculate the *sum* of all the **hash values** of the characters in the substring. 
 Find the remainder of this sum when divided by 26, which is called `hashedChar`. 
 Identify the character in the English lowercase alphabet that corresponds to `hashedChar`. 
 Append that character to the end of `result`.

Return `result`.

## Constraints
- `1 <= k <= 100`
- `k <= s.length <= 1000`
- `s.length` is divisible by `k`.
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abcd", k = 2`
- **Output:** `"bf"`
- **Explanation:** First substring: `"ab"`, `0 + 1 = 1`, `1 % 26 = 1`, `result[0] = 'b'`. 

 Second substring: `"cd"`, `2 + 3 = 5`, `5 % 26 = 5`, `result[1] = 'f'`.

### Example 2
- **Input:** `s = "mxz", k = 3`
- **Output:** `"i"`
- **Explanation:** The only substring: `"mxz"`, `12 + 23 + 25 = 60`, `60 % 26 = 8`, `result[0] = 'i'`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Hash Divided String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcd", k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"bf"`.
4. **Verification:** First substring: `"ab"`, `0 + 1 = 1`, `1 % 26 = 1`, `result[0] = 'b'`. 

 Second substring: `"cd"`, `2 + 3 = 5`, `5 % 26 = 5`, `result[1] = 'f'`.

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
var stringHash = function(s, k) {
    const result = [];

    for (let i = 0; i < s.length; i += k) {
        let total = 0;
        for (let j = i; j < i + k; j++) {
            total += s.charCodeAt(j) - 97;
        }
        result.push(String.fromCharCode(97 + (total % 26)));
    }

    return result.join('');
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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [2156. Find Substring With Given Hash Value](../../2001-2500/2275-find-substring-with-given-hash-value/)
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/hash-divided-string/)
