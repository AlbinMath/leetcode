# LeetCode 20: Valid Parentheses

**LeetCode Problem #20 — Valid Parentheses**
Solve LeetCode Valid Parentheses using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Parentheses |
| LeetCode | #20 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a string  s  containing just the characters  &#39;(&#39; ,  &#39;)&#39; ,  &#39;{&#39; ,  &#39;}&#39; ,  &#39;[&#39;  and  &#39;]&#39; , determine if the input string is valid.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a **Stack** to match opening and closing brackets.

1. It iterates through each character `ch` in the string.
2. **Opening Bracket:** When it encounters an opening bracket (`(`, `[`, or `{`), it pushes the **corresponding closing bracket** onto the stack. This is a clever trick — instead of pushing the opening bracket and then having to look up the matching closer later, it directly pushes what it *expects* to see next.
3. **Closing Bracket:** When it encounters a closing bracket, it checks:
   - If the stack is empty (no matching open bracket), it returns `false`.
   - If the top of the stack (popped value) does not equal the current `ch`, the brackets don't match, so it returns `false`.
4. **Final Check:** After processing all characters, the stack must be empty for the string to be valid. If there are leftover items, there are unmatched opening brackets.

Time complexity is $O(N)$ and space complexity is $O(N)$ in the worst case.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Valid Parentheses**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1208. Get Equal Substrings Within Budget](../1208-maximum-nesting-depth-of-two-valid-parentheses-strings/)
- [2349. Design a Number Container System](../2349-check-if-there-is-a-valid-parentheses-string-path/)
- [193. Valid Phone Numbers](../0193-valid-phone-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-parentheses/)
