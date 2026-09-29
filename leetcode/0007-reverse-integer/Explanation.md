# Reverse Integer

## Problem Explanation
Given a signed 32-bit integer `x`, you need to return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, you must return `0`.

For example:
- `x = 123` returns `321`
- `x = -123` returns `-321`
- `x = 120` returns `21`

## How the Code Works
The code uses mathematical operations to reverse the integer instead of converting it to a string. This is faster and avoids unnecessary memory allocation.

1. **Sign Handling:** It first determines the sign of the number (`1` for positive, `-1` for negative) and then converts `x` to its absolute value to simplify the math.
2. **Reversing the Digits:** It uses a `while (x > 0)` loop to extract the digits from right to left.
   - `x % 10` gets the last digit of the number.
   - `rev = rev * 10 + digit` appends the extracted digit to the end of the reversed number.
   - `Math.trunc(x / 10)` removes the last digit from `x`.
3. **Restoring Sign:** After the loop, it multiplies `rev` by the original `sign`.
4. **Overflow Check:** Finally, it checks if the reversed number falls outside the 32-bit signed integer range (`-2147483648` to `2147483647`). If it overflows, it returns `0`. Otherwise, it returns the reversed number.

This solution takes $O(\log_{10}(x))$ time (since there are roughly $\log_{10}(x)$ digits in $x$) and $O(1)$ space.
