# LeetCode 856: Score of Parentheses

**LeetCode Problem #856 — Score of Parentheses**
Solve LeetCode Score of Parentheses using Python and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Score of Parentheses |
| LeetCode | #856 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a balanced parentheses string `s`, return *the **score** of the string*.

The **score** of a balanced parentheses string is based on the following rule:

`"()"` has score `1`. 
 `AB` has score `A + B`, where `A` and `B` are balanced parentheses strings. 
 `(A)` has score `2 * A`, where `A` is a balanced parentheses string.

## Constraints
- `2 <= s.length <= 50`
- `s` consists of only `'('` and `')'`.
- `s` is a balanced parentheses string.

## Examples
### Example 1
- **Input:** `s = "()"`
- **Output:** `1`

### Example 2
- **Input:** `s = "(())"`
- **Output:** `2`

### Example 3
- **Input:** `s = "()()"`
- **Output:** `2`

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
To solve **Score of Parentheses**, we observe the problem requirements and utilize the **Stack & Queue** technique. We maintain a **Stack** with elements in strictly monotonic order. Whenever an incoming element violates monotonicity, we pop previous elements and compute answer intervals in amortized linear time.

## Algorithm
1. Initialize an empty stack.
2. For each element, pop previous items from stack while monotonic invariant is violated.
3. Push current element or index onto stack.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "()"`.
2. **Processing Steps:** We apply **Monotonic Stack Filtering** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                current = stack.pop()

                if current == 0:
                    score = 1
                else:
                    score = 2 * current

                stack[-1] += score

        return stack[0]
```

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [798. Smallest Rotation with Highest Score](../../0501-1000/0798-smallest-rotation-with-highest-score/)
- [861. Score After Flipping Matrix](../../0501-1000/0861-score-after-flipping-matrix/)
- [1255. Maximum Score Words Formed by Letters](../../1001-1500/1255-maximum-score-words-formed-by-letters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/score-of-parentheses/)
