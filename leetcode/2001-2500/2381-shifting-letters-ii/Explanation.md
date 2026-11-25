# LeetCode 2381: Shifting Letters II

**LeetCode Problem #2381 — Shifting Letters II**
Solve LeetCode Shifting Letters II using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shifting Letters II |
| LeetCode | #2381 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` of lowercase English letters and a 2D integer array `shifts` where `shifts[i] = [start_i, end_i, direction_i]`. For every `i`, **shift** the characters in `s` from the index `start_i` to the index `end_i` (**inclusive**) forward if `direction_i = 1`, or shift the characters backward if `direction_i = 0`.

Shifting a character **forward** means replacing it with the **next** letter in the alphabet (wrapping around so that `'z'` becomes `'a'`). Similarly, shifting a character **backward** means replacing it with the **previous** letter in the alphabet (wrapping around so that `'a'` becomes `'z'`).

Return *the final string after all such shifts to *`s`* are applied*.

## Constraints
- `1 <= s.length, shifts.length <= 5 * 10^4`
- `shifts[i].length == 3`
- `0 <= start_i <= end_i < s.length`
- `0 <= direction_i <= 1`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]`
- **Output:** `"ace"`
- **Explanation:** Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".

### Example 2
- **Input:** `s = "dztz", shifts = [[0,0,0],[1,1,1]]`
- **Output:** `"catz"`
- **Explanation:** Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Shifting Letters II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"ace"`.
4. **Verification:** Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".

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
var shiftingLetters = function(s, shifts) {
    const n = s.length;
    let diff = new Array(n + 1).fill(0);
    for (let [start, end, direction] of shifts) {
        let shift = direction === 1 ? 1 : -1;
        diff[start] += shift;
        diff[end + 1] -= shift;
    }
    let result = [];
    let currentShift = 0;
    for (let i = 0; i < n; i++) {
        currentShift += diff[i];
        let shift = ((currentShift % 26) + 26) % 26;
        let charCode = s.charCodeAt(i) - 97;
        let newChar = (charCode + shift) % 26;
        result.push(String.fromCharCode(newChar + 97));
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
- [848. Shifting Letters](../../0501-1000/0848-shifting-letters/)
- [316. Remove Duplicate Letters](../../0001-0500/0316-remove-duplicate-letters/)
- [917. Reverse Only Letters](../../0501-1000/0917-reverse-only-letters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shifting-letters-ii/)
