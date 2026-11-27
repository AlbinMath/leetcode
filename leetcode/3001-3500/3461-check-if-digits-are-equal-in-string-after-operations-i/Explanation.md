# LeetCode 3461: Check If Digits Are Equal in String After Operations I

**LeetCode Problem #3461 — Check If Digits Are Equal in String After Operations I**
Solve LeetCode Check If Digits Are Equal in String After Operations I using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check If Digits Are Equal in String After Operations I |
| LeetCode | #3461 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting of digits. Perform the following operation repeatedly until the string has **exactly** two digits:

For each pair of consecutive digits in `s`, starting from the first digit, calculate a new digit as the sum of the two digits **modulo** 10. 
 Replace `s` with the sequence of newly calculated digits, *maintaining the order* in which they are computed.

Return `true` if the final two digits in `s` are the **same**; otherwise, return `false`.

## Constraints
- `3 <= s.length <= 100`
- `s` consists of only digits.

## Examples
### Example 1
- **Input:** `s = "3902"`
- **Output:** `true`
- **Explanation:** Initially, `s = "3902"` 
 First operation:
 
 `(s[0] + s[1]) % 10 = (3 + 9) % 10 = 2` 
 `(s[1] + s[2]) % 10 = (9 + 0) % 10 = 9` 
 `(s[2] + s[3]) % 10 = (0 + 2) % 10 = 2` 
 `s` becomes `"292"` 
 
 
 Second operation:
 
 `(s[0] + s[1]) % 10 = (2 + 9) % 10 = 1` 
 `(s[1] + s[2]) % 10 = (9 + 2) % 10 = 1` 
 `s` becomes `"11"` 
 
 
 Since the digits in `"11"` are the same, the output is `true`.

### Example 2
- **Input:** `s = "34789"`
- **Output:** `false`
- **Explanation:** Initially, `s = "34789"`. 
 After the first operation, `s = "7157"`. 
 After the second operation, `s = "862"`. 
 After the third operation, `s = "48"`. 
 Since `'4' != '8'`, the output is `false`.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check If Digits Are Equal in String After Operations I**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "3902"`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Initially, `s = "3902"` 
 First operation:
 
 `(s[0] + s[1]) % 10 = (3 + 9) % 10 = 2` 
 `(s[1] + s[2]) % 10 = (9 + 0) % 10 = 9` 
 `(s[2] + s[3]) % 10 = (0 + 2) % 10 = 2` 
 `s` becomes `"292"` 
 
 
 Second operation:
 
 `(s[0] + s[1]) % 10 = (2 + 9) % 10 = 1` 
 `(s[1] + s[2]) % 10 = (9 + 2) % 10 = 1` 
 `s` becomes `"11"` 
 
 
 Since the digits in `"11"` are the same, the output is `true`.

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
/**
 * @param {string} s
 * @return {boolean}
 */
var hasSameDigits = function (s) {
    let arr = s.split("").map(Number);

    while (arr.length > 2) {
        const next = [];
        for (let i = 0; i < arr.length - 1; i++) {
            next.push((arr[i] + arr[i + 1]) % 10);
        }
        arr = next;
    }

    return arr[0] === arr[1];
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
- [3463. Check If Digits Are Equal in String After Operations II](../../3001-3500/3463-check-if-digits-are-equal-in-string-after-operations-ii/)
- [1790. Check if One String Swap Can Make Strings Equal](../../1501-2000/1790-check-if-one-string-swap-can-make-strings-equal/)
- [2840. Check if Strings Can be Made Equal With Operations II](../../2501-3000/2840-check-if-strings-can-be-made-equal-with-operations-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/)
