# LeetCode 227: Basic Calculator II

**LeetCode Problem #227 — Basic Calculator II**
Solve LeetCode Basic Calculator II using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Basic Calculator II |
| LeetCode | #227 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s` which represents an expression, *evaluate this expression and return its value*.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2^31, 2^31 - 1]`.

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

## Constraints
- `1 <= s.length <= 3 * 10^5`
- `s` consists of integers and operators `('+', '-', '*', '/')` separated by some number of spaces.
- `s` represents a valid expression.
- All the integers in the expression are non-negative integers in the range `[0, 2^31 - 1]`.
- The answer is **guaranteed** to fit in a **32-bit integer**.

## Examples
### Example 1
- **Input:** `s = "3+2*2"`
- **Output:** `7`

### Example 2
- **Input:** `s = " 3/2 "`
- **Output:** `1`

### Example 3
- **Input:** `s = " 3+5 / 2 "`
- **Output:** `5`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Basic Calculator II**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "3+2*2"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {string} s
 * @return {number}
 */
var calculate = function (s) {
  const stack = [];
  let num = 0;
  let op = '+'; // operator preceding the current number

  for (let i = 0; i < s.length; i++) {
    const ch = s[i];

    if (ch >= '0' && ch <= '9') {
      num = num * 10 + (ch.charCodeAt(0) - 48);
    }

    // Process when we hit an operator, or reach the end of the string
    if ((ch !== ' ' && (ch < '0' || ch > '9')) || i === s.length - 1) {
      if (op === '+') {
        stack.push(num);
      } else if (op === '-') {
        stack.push(-num);
      } else if (op === '*') {
        stack.push(stack.pop() * num);
      } else if (op === '/') {
        stack.push(Math.trunc(stack.pop() / num));
      }
      op = ch;
      num = 0;
    }
  }

  return stack.reduce((a, b) => a + b, 0);
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [224. Basic Calculator](../../0001-0500/0224-basic-calculator/)
- [770. Basic Calculator IV](../../0501-1000/0781-basic-calculator-iv/)
- [2642. Design Graph With Shortest Path Calculator](../../2501-3000/2678-design-graph-with-shortest-path-calculator/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/basic-calculator-ii/)
