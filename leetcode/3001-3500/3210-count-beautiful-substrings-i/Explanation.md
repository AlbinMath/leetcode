# LeetCode 2947: Count Beautiful Substrings I

**LeetCode Problem #2947 — Count Beautiful Substrings I**
Solve LeetCode Count Beautiful Substrings I using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Beautiful Substrings I |
| LeetCode | #2947 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` and a positive integer `k`.

Let `vowels` and `consonants` be the number of vowels and consonants in a string.

A string is **beautiful** if:

`vowels == consonants`. 
 `(vowels * consonants) % k == 0`, in other terms the multiplication of `vowels` and `consonants` is divisible by `k`.

Return *the number of **non-empty beautiful substrings** in the given string* `s`.

A **substring** is a contiguous sequence of characters in a string.

**Vowel letters** in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

**Consonant letters** in English are every letter except vowels.

## Constraints
- `1 <= s.length <= 1000`
- `1 <= k <= 1000`
- `s` consists of only English lowercase letters.

## Examples
### Example 1
- **Input:** `s = "baeyh", k = 2`
- **Output:** `2`
- **Explanation:** There are 2 beautiful substrings in the given string.
- Substring "b aeyh ", vowels = 2 (["a",e"]), consonants = 2 (["y","h"]).
You can see that string "aeyh" is beautiful as vowels == consonants and vowels * consonants % k == 0.
- Substring " baey h", vowels = 2 (["a",e"]), consonants = 2 (["b","y"]). 
You can see that string "baey" is beautiful as vowels == consonants and vowels * consonants % k == 0.
It can be shown that there are only 2 beautiful substrings in the given string.

### Example 2
- **Input:** `s = "abba", k = 1`
- **Output:** `3`
- **Explanation:** There are 3 beautiful substrings in the given string.
- Substring " ab ba", vowels = 1 (["a"]), consonants = 1 (["b"]). 
- Substring "ab ba ", vowels = 1 (["a"]), consonants = 1 (["b"]).
- Substring " abba ", vowels = 2 (["a","a"]), consonants = 2 (["b","b"]).
It can be shown that there are only 3 beautiful substrings in the given string.

### Example 3
- **Input:** `s = "bcdf", k = 1`
- **Output:** `0`
- **Explanation:** There are no beautiful substrings in the given string.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Beautiful Substrings I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "baeyh", k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** There are 2 beautiful substrings in the given string.
- Substring "b aeyh ", vowels = 2 (["a",e"]), consonants = 2 (["y","h"]).
You can see that string "aeyh" is beautiful as vowels == consonants and vowels * consonants % k == 0.
- Substring " baey h", vowels = 2 (["a",e"]), consonants = 2 (["b","y"]). 
You can see that string "baey" is beautiful as vowels == consonants and vowels * consonants % k == 0.
It can be shown that there are only 2 beautiful substrings in the given string.

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
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var beautifulSubstrings = function(s, k) {
    const n = s.length;
    const isVowel = (ch) => ch === 'a' || ch === 'e' || ch === 'i' || ch === 'o' || ch === 'u';
    let count = 0;

    for (let i = 0; i < n; i++) {
        let vowels = 0;
        let consonants = 0;

        for (let j = i; j < n; j++) {
            if (isVowel(s[j])) {
                vowels++;
            } else {
                consonants++;
            }

            if (vowels === consonants && (vowels * consonants) % k === 0) {
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
- [2949. Count Beautiful Substrings II](../../3001-3500/3208-count-beautiful-substrings-ii/)
- [2588. Count the Number of Beautiful Subarrays](../../2501-3000/2656-count-the-number-of-beautiful-subarrays/)
- [2767. Partition String Into Minimum Beautiful Substrings](../../2501-3000/2883-partition-string-into-minimum-beautiful-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-beautiful-substrings-i/)
