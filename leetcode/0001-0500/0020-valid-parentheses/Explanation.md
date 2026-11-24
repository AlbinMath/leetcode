# LeetCode 20: Valid Parentheses

**LeetCode Problem #20 — Valid Parentheses**
Solve LeetCode Valid Parentheses using JavaScript, Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Parentheses |
| LeetCode | #20 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets. 
 Open brackets must be closed in the correct order. 
 Every close bracket has a corresponding open bracket of the same type.

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

## Examples
### Example 1
- **Input:** `s = "()"`
- **Output:** `true`

### Example 2
- **Input:** `s = "()[]{}"`
- **Output:** `true`

### Example 3
- **Input:** `s = "(]"`
- **Output:** `false`

### Example 4
- **Input:** `s = "([])"`
- **Output:** `true`

### Example 5
- **Input:** `s = "([)]"`
- **Output:** `false`

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

## Example Walkthrough
1. **Input State:** We begin with `s = "()"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var isValid = function(s) {
    const stack = [];
    const pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    };

    for (const char of s) {
        if (char === '(' || char === '{' || char === '[') {
            stack.push(char);
        } else {
            if (
                stack.length === 0 ||
                stack.pop() !== pairs[char]
            ) {
                return false;
            }
        }
    }

    return stack.length === 0;
};
```

### Python
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()

        return len(stack) == 0
```

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
- [32. Longest Valid Parentheses](../../0001-0500/0032-longest-valid-parentheses/)
- [921. Minimum Add to Make Parentheses Valid](../../0501-1000/0921-minimum-add-to-make-parentheses-valid/)
- [1111. Maximum Nesting Depth of Two Valid Parentheses Strings](../../1001-1500/1111-maximum-nesting-depth-of-two-valid-parentheses-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-parentheses/)
