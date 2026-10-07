# LeetCode 7: Reverse Integer

**LeetCode Problem #7 — Reverse Integer**
Solve LeetCode Reverse Integer using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reverse Integer |
| LeetCode | #7 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a signed 32-bit integer  x , return  x   with its digits reversed . If reversing  x  causes the value to go outside the signed 32-bit integer range  [-2 31 , 2 31  - 1] , then return  0 .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses mathematical operations to reverse the integer instead of converting it to a string. This is faster and avoids unnecessary memory allocation.

1. **Sign Handling:** It first determines the sign of the number (`1` for positive, `-1` for negative) and then converts `x` to its absolute value to simplify the math.
2. **Reversing the Digits:** It uses a `while (x > 0)` loop to extract the digits from right to left.
   - `x % 10` gets the last digit of the number.
   - `rev = rev * 10 + digit` appends the extracted digit to the end of the reversed number.
   - `Math.trunc(x / 10)` removes the last digit from `x`.
3. **Restoring Sign:** After the loop, it multiplies `rev` by the original `sign`.
4. **Overflow Check:** Finally, it checks if the reversed number falls outside the 32-bit signed integer range (`-2147483648` to `2147483647`). If it overflows, it returns `0`. Otherwise, it returns the reversed number.

This solution takes $O(\log_{10}(x))$ time (since there are roughly $\log_{10}(x)$ digits in $x$) and $O(1)$ space.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Reverse Integer**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [8. String to Integer (atoi)](../0008-string-to-integer-atoi/)
- [12. Integer to Roman](../0012-integer-to-roman/)
- [13. Roman to Integer](../0013-roman-to-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reverse-integer/)
