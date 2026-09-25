# Reverse Degree of a String

## Problem Explanation
The "reverse degree" of a string is calculated by taking each character in a string, finding its position in the reversed English alphabet (`'z'` is 1, `'y'` is 2, ..., `'a'` is 26), and multiplying that by its 1-indexed position in the string. The total reverse degree is the sum of all these products.

For example, for the string `"abc"`:
- `'a'` is 1st in the string, 26th in reversed alphabet: `1 * 26 = 26`
- `'b'` is 2nd in the string, 25th in reversed alphabet: `2 * 25 = 50`
- `'c'` is 3rd in the string, 24th in reversed alphabet: `3 * 24 = 72`
- Total: `26 + 50 + 72 = 148`.

## How the Code Works
The code simply iterates through the string, computing the required product for each character and adding it to a running total.
1. It initializes `total = 0`.
2. It loops through the string using `enumerate(s)`, which gives both the zero-based index `i` and the character `ch`.
3. To calculate the character's value in the reversed alphabet:
   - `ord(ch) - ord('a')` gives the 0-based index in the normal alphabet (e.g., `'a'` is 0, `'z'` is 25).
   - Subtracting this from 26 gives the 1-based index in the reversed alphabet (e.g., `26 - 0 = 26` for `'a'`).
4. The 1-based position in the string is simply `i + 1`.
5. It multiplies the `value` and `position`, adding the result to `total`.
6. After processing all characters, it returns the final `total`.
