# Valid Parentheses

## Problem Explanation
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid. A string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

For example:
- `"()"` → `true`
- `"()[]{}"` → `true`
- `"(]"` → `false`

## How the Code Works
The code uses a **Stack** to match opening and closing brackets.

1. It iterates through each character `ch` in the string.
2. **Opening Bracket:** When it encounters an opening bracket (`(`, `[`, or `{`), it pushes the **corresponding closing bracket** onto the stack. This is a clever trick — instead of pushing the opening bracket and then having to look up the matching closer later, it directly pushes what it *expects* to see next.
3. **Closing Bracket:** When it encounters a closing bracket, it checks:
   - If the stack is empty (no matching open bracket), it returns `false`.
   - If the top of the stack (popped value) does not equal the current `ch`, the brackets don't match, so it returns `false`.
4. **Final Check:** After processing all characters, the stack must be empty for the string to be valid. If there are leftover items, there are unmatched opening brackets.

Time complexity is $O(N)$ and space complexity is $O(N)$ in the worst case.
