# LeetCode 301: Remove Invalid Parentheses

**LeetCode Problem #301 — Remove Invalid Parentheses**
Solve LeetCode Remove Invalid Parentheses using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Invalid Parentheses |
| LeetCode | #301 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return *a list of **unique strings** that are valid with the minimum number of removals*. You may return the answer in **any order**.

## Constraints
- `1 <= s.length <= 25`
- `s` consists of lowercase English letters and parentheses `'('` and `')'`.
- There will be at most `20` parentheses in `s`.

## Examples
### Example 1
- **Input:** `s = "()())()"`
- **Output:** `["(())()","()()()"]`

### Example 2
- **Input:** `s = "(a)())()"`
- **Output:** `["(a())()","(a)()()"]`

### Example 3
- **Input:** `s = ")("`
- **Output:** `[""]`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Remove Invalid Parentheses**, we observe the problem requirements and utilize the **Stack & Queue** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "()())()"`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["(())()","()()()"]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def removeInvalidParentheses(self, s):
        left_remove = 0
        right_remove = 0

        # Find the minimum number of removals
        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def backtrack(index, path, balance, left_rem, right_rem):

            # Invalid parentheses
            if balance < 0:
                return

            # End of string
            if index == len(s):
                if balance == 0 and left_rem == 0 and right_rem == 0:
                    result.add(path)
                return

            ch = s[index]

            if ch == '(':

                # Remove '('
                if left_rem > 0:
                    backtrack(
                        index + 1,
                        path,
                        balance,
                        left_rem - 1,
                        right_rem
                    )

                # Keep '('
                backtrack(
                    index + 1,
                    path + ch,
                    balance + 1,
                    left_rem,
                    right_rem
                )

            elif ch == ')':

                # Remove ')'
                if right_rem > 0:
                    backtrack(
                        index + 1,
                        path,
                        balance,
                        left_rem,
                        right_rem - 1
                    )

                # Keep ')' only if possible
                if balance > 0:
                    backtrack(
                        index + 1,
                        path + ch,
                        balance - 1,
                        left_rem,
                        right_rem
                    )

            else:
                # Keep letters
                backtrack(
                    index + 1,
                    path + ch,
                    balance,
                    left_rem,
                    right_rem
                )

        backtrack(
            0,
            "",
            0,
            left_remove,
            right_remove
        )

        return list(result)
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1021. Remove Outermost Parentheses](../../1001-1500/1021-remove-outermost-parentheses/)
- [1249. Minimum Remove to Make Valid Parentheses](../../1001-1500/1249-minimum-remove-to-make-valid-parentheses/)
- [1169. Invalid Transactions](../../1001-1500/1169-invalid-transactions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-invalid-parentheses/)
