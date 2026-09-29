# Evaluate Reverse Polish Notation

## Problem Explanation
You are given an array of strings `tokens` that represents an arithmetic expression in **Reverse Polish Notation** (RPN). Evaluate the expression and return the result. Valid operators are `+`, `-`, `*`, and `/`. Division should truncate toward zero.

For example, `tokens = ["2","1","+","3","*"]` → `((2 + 1) * 3) = 9`.

## How the Code Works
The code uses a **Stack** to evaluate the RPN expression.

1. **Iterate Through Tokens:** For each token in the array:
   - **If it's an operator** (`+`, `-`, `*`, `/`): Pop two values from the stack. The second popped value `a` is the left operand and the first popped value `b` is the right operand. Apply the operator and push the result back onto the stack. For division, `Math.trunc(a / b)` is used to truncate toward zero.
   - **If it's a number:** Convert it to a number using `Number(token)` and push it onto the stack.
2. **Result:** After processing all tokens, the final result is the single remaining element in the stack (`stack[0]`).

Time complexity is $O(N)$ where $N$ is the number of tokens, and space complexity is $O(N)$ for the stack.
