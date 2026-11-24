# LeetCode 1249: Minimum Remove to Make Valid Parentheses

**LeetCode Problem #1249 — Minimum Remove to Make Valid Parentheses**
Solve LeetCode Minimum Remove to Make Valid Parentheses using Python and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Remove to Make Valid Parentheses |
| LeetCode | #1249 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string s of `'('` , `')'` and lowercase English characters.

Your task is to remove the minimum number of parentheses ( `'('` or `')'`, in any positions ) so that the resulting *parentheses string* is valid and return **any** valid string.

Formally, a *parentheses string* is valid if and only if:

It is the empty string, contains only lowercase characters, or 
 It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or 
 It can be written as `(A)`, where `A` is a valid string.

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is either `'('` , `')'`, or lowercase English letter.

## Examples
### Example 1
- **Input:** `s = "lee(t(c)o)de)"`
- **Output:** `"lee(t(c)o)de"`
- **Explanation:** "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

### Example 2
- **Input:** `s = "a)b(c)d"`
- **Output:** `"ab(c)d"`

### Example 3
- **Input:** `s = "))(("`
- **Output:** `""`
- **Explanation:** An empty string is also valid.

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
To solve **Minimum Remove to Make Valid Parentheses**, we observe the problem requirements and utilize the **Stack & Queue** technique. We maintain a **Stack** with elements in strictly monotonic order. Whenever an incoming element violates monotonicity, we pop previous elements and compute answer intervals in amortized linear time.

## Algorithm
1. Initialize an empty stack.
2. For each element, pop previous items from stack while monotonic invariant is violated.
3. Push current element or index onto stack.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "lee(t(c)o)de)"`.
2. **Processing Steps:** We apply **Monotonic Stack Filtering** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"lee(t(c)o)de"`.
4. **Verification:** "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

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
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = set()

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    remove.add(i)

        remove.update(stack)

        return ''.join(
            ch for i, ch in enumerate(s)
            if i not in remove
        )
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
- [921. Minimum Add to Make Parentheses Valid](../../0501-1000/0921-minimum-add-to-make-parentheses-valid/)
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [2645. Minimum Additions to Make Valid String](../../2501-3000/2645-minimum-additions-to-make-valid-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)
