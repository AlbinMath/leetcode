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

## Problem
You are given an array of strings  tokens  that represents an arithmetic expression in a  Reverse Polish Notation .

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

## Example
Consider the standard input for **Evaluate Reverse Polish Notation**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)

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
- [7. Reverse Integer](../0007-reverse-integer/)
- [25. Reverse Nodes in k-Group](../0025-reverse-nodes-in-k-group/)
- [206. Reverse Linked List](../0206-reverse-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
