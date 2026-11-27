# LeetCode 3675: Minimum Operations to Transform String

**LeetCode Problem #3675 — Minimum Operations to Transform String**
Solve LeetCode Minimum Operations to Transform String using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Transform String |
| LeetCode | #3675 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting only of lowercase English letters.

You can perform the following operation any number of times (including zero):

Choose any character `c` in the string and replace **every** occurrence of `c` with the **next** lowercase letter in the English alphabet.

Return the **minimum** number of operations required to transform `s` into a string consisting of **only** `'a'` characters.

**Note: **Consider the alphabet as circular, thus `'a'` comes after `'z'`.

## Constraints
- `1 <= s.length <= 5 * 10^5`
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "yz"`
- **Output:** `2`
- **Explanation:** Change `'y'` to `'z'` to get `"zz"`. 
 Change `'z'` to `'a'` to get `"aa"`. 
 Thus, the answer is 2.

### Example 2
- **Input:** `s = "a"`
- **Output:** `0`
- **Explanation:** The string `"a"` only consists of `'a'`​​​​​​​ characters. Thus, the answer is 0.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Operations to Transform String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "yz"`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Change `'y'` to `'z'` to get `"zz"`. 
 Change `'z'` to `'a'` to get `"aa"`. 
 Thus, the answer is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minOperations = function(s) {
    let ans = 0;

    for (let i = 0; i < s.length; i++) {
        const distance = 26 - (s.charCodeAt(i) - 97);

        ans = Math.max(ans, distance === 26 ? 0 : distance);
    }

    return ans;
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3980. Minimum Operations to Transform Binary String](../../3501-4000/3980-minimum-operations-to-transform-binary-string/)
- [1830. Minimum Number of Operations to Make String Sorted](../../1501-2000/1830-minimum-number-of-operations-to-make-string-sorted/)
- [3223. Minimum Length of String After Operations](../../3001-3500/3223-minimum-length-of-string-after-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-transform-string/)
