# LeetCode 2864: Maximum Odd Binary Number

**LeetCode Problem #2864 — Maximum Odd Binary Number**
Solve LeetCode Maximum Odd Binary Number using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Odd Binary Number |
| LeetCode | #2864 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **binary** string `s` that contains at least one `'1'`.

You have to **rearrange** the bits in such a way that the resulting binary number is the **maximum odd binary number** that can be created from this combination.

Return *a string representing the maximum odd binary number that can be created from the given combination.*

**Note **that the resulting string **can** have leading zeros.

## Constraints
- `1 <= s.length <= 100`
- `s` consists only of `'0'` and `'1'`.
- `s` contains at least one `'1'`.

## Examples
### Example 1
- **Input:** `s = "010"`
- **Output:** `"001"`
- **Explanation:** Because there is just one '1', it must be in the last position. So the answer is "001".

### Example 2
- **Input:** `s = "0101"`
- **Output:** `"1001"`
- **Explanation:** One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Odd Binary Number**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "010"`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"001"`.
4. **Verification:** Because there is just one '1', it must be in the last position. So the answer is "001".

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maximumOddBinaryNumber = function(s) {
    let ones = 0;
    let zeros = 0;

    for (let ch of s) {
        if (ch === '1') ones++;
        else zeros++;
    }

    ones--; // Reserve one '1' for the last position

    return '1'.repeat(ones) + '0'.repeat(zeros) + '1';
};
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3309. Maximum Possible Number by Binary Concatenation](../../3001-3500/3309-maximum-possible-number-by-binary-concatenation/)
- [1524. Number of Sub-arrays With Odd Sum](../../1501-2000/1524-number-of-sub-arrays-with-odd-sum/)
- [1903. Largest Odd Number in String](../../1501-2000/1903-largest-odd-number-in-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-odd-binary-number/)
