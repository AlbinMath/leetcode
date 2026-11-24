# LeetCode 880: Decoded String at Index

**LeetCode Problem #880 — Decoded String at Index**
Solve LeetCode Decoded String at Index using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Decoded String at Index |
| LeetCode | #880 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an encoded string `s`. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape. 
 If the character read is a digit `d`, the entire current tape is repeatedly written `d - 1` more times in total.

Given an integer `k`, return *the *`k^th`* letter (**1-indexed)** in the decoded string*.

## Constraints
- `2 <= s.length <= 100`
- `s` consists of lowercase English letters and digits `2` through `9`.
- `s` starts with a letter.
- `1 <= k <= 10^9`
- It is guaranteed that `k` is less than or equal to the length of the decoded string.
- The decoded string is guaranteed to have less than `2^63` letters.

## Examples
### Example 1
- **Input:** `s = "leet2code3", k = 10`
- **Output:** `"o"`
- **Explanation:** The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10^th letter in the string is "o".

### Example 2
- **Input:** `s = "ha22", k = 5`
- **Output:** `"h"`
- **Explanation:** The decoded string is "hahahaha".
The 5^th letter is "h".

### Example 3
- **Input:** `s = "a2345678999999999999999", k = 1`
- **Output:** `"a"`
- **Explanation:** The decoded string is "a" repeated 8301530446056247680 times.
The 1^st letter is "a".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Decoded String at Index**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "leet2code3", k = 10`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"o"`.
4. **Verification:** The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10^th letter in the string is "o".

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
var decodeAtIndex = function(s, k) {
    let size = 0n;
    k = BigInt(k);

    // Calculate decoded string length
    for (const ch of s) {
        if (ch >= '2' && ch <= '9') {
            size *= BigInt(ch);
        } else {
            size++;
        }
    }

    // Traverse backward
    for (let i = s.length - 1; i >= 0; i--) {
        const ch = s[i];

        k %= size;

        // Find the required character
        if (k === 0n && ch >= 'a' && ch <= 'z') {
            return ch;
        }

        if (ch >= '2' && ch <= '9') {
            size /= BigInt(ch);
        } else {
            size--;
        }
    }

    return "";
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
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [274. H-Index](../../0001-0500/0274-h-index/)
- [275. H-Index II](../../0001-0500/0275-h-index-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/decoded-string-at-index/)
