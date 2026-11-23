# LeetCode 150: Evaluate Reverse Polish Notation

**LeetCode Problem #150 — Evaluate Reverse Polish Notation**
Solve LeetCode Evaluate Reverse Polish Notation using TypeScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Evaluate Reverse Polish Notation |
| LeetCode | #150 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of strings `tokens` that represents an arithmetic expression in a Reverse Polish Notation .

Evaluate the expression. Return *an integer that represents the value of the expression*.

**Note** that:

The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`. 
 Each operand may be an integer or another expression. 
 The division between two integers always **truncates toward zero**. 
 There will not be any division by zero. 
 The input represents a valid arithmetic expression in a reverse polish notation. 
 The answer and all the intermediate calculations can be represented in a **32-bit** integer.

## Constraints
- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.

## Examples
### Example 1
- **Input:** `tokens = ["2","1","+","3","*"]`
- **Output:** `9`
- **Explanation:** ((2 + 1) * 3) = 9

### Example 2
- **Input:** `tokens = ["4","13","5","/","+"]`
- **Output:** `6`
- **Explanation:** (4 + (13 / 5)) = 6

### Example 3
- **Input:** `tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]`
- **Output:** `22`
- **Explanation:** ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a **Stack** to evaluate the RPN expression.

1. **Iterate Through Tokens:** For each token in the array:
   - **If it's an operator** (`+`, `-`, `*`, `/`): Pop two values from the stack. The second popped value `a` is the left operand and the first popped value `b` is the right operand. Apply the operator and push the result back onto the stack. For division, `Math.trunc(a / b)` is used to truncate toward zero.
   - **If it's a number:** Convert it to a number using `Number(token)` and push it onto the stack.
2. **Result:** After processing all tokens, the final result is the single remaining element in the stack (`stack[0]`).

Time complexity is $O(N)$ where $N$ is the number of tokens, and space complexity is $O(N)$ for the stack.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `tokens = ["2","1","+","3","*"]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** ((2 + 1) * 3) = 9

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
function evalRPN(tokens: string[]): number {
    const stack: number[] = [];

    for (const token of tokens) {
        if (token === "+" || token === "-" || token === "*" || token === "/") {
            const b = stack.pop()!;
            const a = stack.pop()!;

            let result: number;

            if (token === "+") {
                result = a + b;
            } else if (token === "-") {
                result = a - b;
            } else if (token === "*") {
                result = a * b;
            } else {
                // Truncate toward zero
                result = Math.trunc(a / b);
            }

            stack.push(result);
        } else {
            stack.push(Number(token));
        }
    }

    return stack[0];
}
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
- [7. Reverse Integer](../../0001-0500/0007-reverse-integer/)
- [25. Reverse Nodes in k-Group](../../0001-0500/0025-reverse-nodes-in-k-group/)
- [92. Reverse Linked List II](../../0001-0500/0092-reverse-linked-list-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
