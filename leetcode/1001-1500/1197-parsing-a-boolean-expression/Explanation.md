# LeetCode 1106: Parsing A Boolean Expression

**LeetCode Problem #1106 — Parsing A Boolean Expression**
Solve LeetCode Parsing A Boolean Expression using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Parsing A Boolean Expression |
| LeetCode | #1106 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A **boolean expression** is an expression that evaluates to either `true` or `false`. It can be in one of the following shapes:

`'t'` that evaluates to `true`. 
 `'f'` that evaluates to `false`. 
 `'!(subExpr)'` that evaluates to **the logical NOT** of the inner expression `subExpr`. 
 `'&(subExpr_1, subExpr_2, ..., subExpr_n)'` that evaluates to **the logical AND** of the inner expressions `subExpr_1, subExpr_2, ..., subExpr_n` where `n >= 1`. 
 `'|(subExpr_1, subExpr_2, ..., subExpr_n)'` that evaluates to **the logical OR** of the inner expressions `subExpr_1, subExpr_2, ..., subExpr_n` where `n >= 1`.

Given a string `expression` that represents a **boolean expression**, return *the evaluation of that expression*.

It is **guaranteed** that the given expression is valid and follows the given rules.

## Constraints
- `1 <= expression.length <= 2 * 10^4`
- expression[i] is one following characters: `'('`, `')'`, `'&'`, `'|'`, `'!'`, `'t'`, `'f'`, and `','`.

## Examples
### Example 1
- **Input:** `expression = "&(|(f))"`
- **Output:** `false`
- **Explanation:** First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.

### Example 2
- **Input:** `expression = "|(f,f,f,t)"`
- **Output:** `true`
- **Explanation:** The evaluation of (false OR false OR false OR true) is true.

### Example 3
- **Input:** `expression = "!(&(f,t))"`
- **Output:** `true`
- **Explanation:** First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Parsing A Boolean Expression**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `expression = "&(|(f))"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for c in expression:
            if c == ',':
                continue
            if c != ')':
                stack.append(c)
                continue

            has_t = has_f = False
            while stack[-1] != '(':
                if stack.pop() == 't':
                    has_t = True
                else:
                    has_f = True
            stack.pop()        # '('
            op = stack.pop()   # operator

            if op == '!':
                res = has_f
            elif op == '&':
                res = not has_f
            else:  # '|'
                res = has_t
            stack.append('t' if res else 'f')

        return stack[0] == 't'
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
- [2331. Evaluate Boolean Binary Tree](../../2001-2500/2416-evaluate-boolean-binary-tree/)
- [10. Regular Expression Matching](../../0001-0500/0010-regular-expression-matching/)
- [282. Expression Add Operators](../../0001-0500/0282-expression-add-operators/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/parsing-a-boolean-expression/)
