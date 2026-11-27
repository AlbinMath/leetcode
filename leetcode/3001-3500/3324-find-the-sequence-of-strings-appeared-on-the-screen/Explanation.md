# LeetCode 3324: Find the Sequence of Strings Appeared on the Screen

**LeetCode Problem #3324 — Find the Sequence of Strings Appeared on the Screen**
Solve LeetCode Find the Sequence of Strings Appeared on the Screen using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Sequence of Strings Appeared on the Screen |
| LeetCode | #3324 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `target`.

Alice is going to type `target` on her computer using a special keyboard that has **only two** keys:

Key 1 appends the character `"a"` to the string on the screen. 
 Key 2 changes the **last** character of the string on the screen to its **next** character in the English alphabet. For example, `"c"` changes to `"d"` and `"z"` changes to `"a"`.

**Note** that initially there is an *empty* string `""` on the screen, so she can **only** press key 1.

Return a list of *all* strings that appear on the screen as Alice types `target`, in the order they appear, using the **minimum** key presses.

## Constraints
- `1 <= target.length <= 400`
- `target` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `target = "abc"`
- **Output:** `["a","aa","ab","aba","abb","abc"]`
- **Explanation:** The sequence of key presses done by Alice are: 

 
 Press key 1, and the string on the screen becomes `"a"`. 
 Press key 1, and the string on the screen becomes `"aa"`. 
 Press key 2, and the string on the screen becomes `"ab"`. 
 Press key 1, and the string on the screen becomes `"aba"`. 
 Press key 2, and the string on the screen becomes `"abb"`. 
 Press key 2, and the string on the screen becomes `"abc"`.

### Example 2
- **Input:** `target = "he"`
- **Output:** `["a","b","c","d","e","f","g","h","ha","hb","hc","hd","he"]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Sequence of Strings Appeared on the Screen**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `target = "abc"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["a","aa","ab","aba","abb","abc"]`.
4. **Verification:** The sequence of key presses done by Alice are: 

 
 Press key 1, and the string on the screen becomes `"a"`. 
 Press key 1, and the string on the screen becomes `"aa"`. 
 Press key 2, and the string on the screen becomes `"ab"`. 
 Press key 1, and the string on the screen becomes `"aba"`. 
 Press key 2, and the string on the screen becomes `"abb"`. 
 Press key 2, and the string on the screen becomes `"abc"`.

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
var stringSequence = function(target) {
    const result = [];
    let prefix = "";

    for (const ch of target) {
        const targetCode = ch.charCodeAt(0);
        for (let code = 97; code <= targetCode; code++) {
            result.push(prefix + String.fromCharCode(code));
        }
        prefix += ch;
    }

    return result;
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
- [3287. Find the Maximum Sequence Value of Array](../../3001-3500/3287-find-the-maximum-sequence-value-of-array/)
- [3302. Find the Lexicographically Smallest Valid Sequence](../../3001-3500/3302-find-the-lexicographically-smallest-valid-sequence/)
- [1397. Find All Good Strings](../../1001-1500/1397-find-all-good-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/)
