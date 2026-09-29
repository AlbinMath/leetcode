# Reverse Substrings Between Each Pair Of Parentheses

## Problem Explanation
Given a string `s` with lowercase letters and parentheses, reverse the strings within each pair of matching parentheses, starting from the innermost pair. Return the result without any parentheses.

For example, `"(abcd)"` → `"dcba"`, `"(u(love)i)"` → `"iloveu"`.

## How the Code Works
The code uses a **Stack of Strings**.

1. **Maintain `current`:** A string being built from the current nesting level.
2. **On `(`:** Push `current` onto the stack (save progress) and reset `current` to empty.
3. **On `)`:** Reverse `current`, then prepend the string from the top of the stack (pop it). This effectively reverses the content within the parentheses and concatenates it with the content before the opening parenthesis.
4. **On any other character:** Append it to `current`.
5. After processing all characters, `current` holds the final result.

Time complexity is $O(N^2)$ in the worst case (due to reversals) and space complexity is $O(N)$.
