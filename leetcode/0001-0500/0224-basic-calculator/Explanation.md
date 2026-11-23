# LeetCode 224: Basic Calculator

**LeetCode Problem #224 — Basic Calculator**
Solve LeetCode Basic Calculator using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Basic Calculator |
| LeetCode | #224 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return *the result of the evaluation*.

**Note:** You are **not** allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

## Constraints
- `1 <= s.length <= 3 * 10^5`
- `s` consists of digits, `'+'`, `'-'`, `'('`, `')'`, and `' '`.
- `s` represents a valid expression.
- `'+'` is **not** used as a unary operation (i.e., `"+1"` and `"+(2 + 3)"` is invalid).
- `'-'` could be used as a unary operation (i.e., `"-1"` and `"-(2 + 3)"` is valid).
- There will be no two consecutive operators in the input.
- Every number and running calculation will fit in a signed 32-bit integer.

## Examples
### Example 1
- **Input:** `s = "1 + 1"`
- **Output:** `2`

### Example 2
- **Input:** `s = " 2-1 + 2 "`
- **Output:** `3`

### Example 3
- **Input:** `s = "(1+(4+5+2)-3)+(6+8)"`
- **Output:** `23`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Basic Calculator**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "1 + 1"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var calculate = function(s) {
    const stack = [];
    let result = 0;
    let number = 0;
    let sign = 1;

    for (let i = 0; i < s.length; i++) {
        const char = s[i];

        if (char >= '0' && char <= '9') {
            number = number * 10 + Number(char);
        } else if (char === '+') {
            result += sign * number;
            number = 0;
            sign = 1;
        } else if (char === '-') {
            result += sign * number;
            number = 0;
            sign = -1;
        } else if (char === '(') {
            stack.push(result);
            stack.push(sign);

            result = 0;
            sign = 1;
        } else if (char === ')') {
            result += sign * number;
            number = 0;

            result *= stack.pop();
            result += stack.pop();
        }
    }

    result += sign * number;

    return result;
};
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
- [227. Basic Calculator II](../../0001-0500/0227-basic-calculator-ii/)
- [770. Basic Calculator IV](../../0501-1000/0781-basic-calculator-iv/)
- [2642. Design Graph With Shortest Path Calculator](../../2501-3000/2678-design-graph-with-shortest-path-calculator/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/basic-calculator/)
