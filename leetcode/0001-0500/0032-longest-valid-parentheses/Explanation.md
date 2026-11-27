# LeetCode 32: Longest Valid Parentheses

**LeetCode Problem #32 — Longest Valid Parentheses**
Solve LeetCode Longest Valid Parentheses using JavaScript, Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Valid Parentheses |
| LeetCode | #32 |
| Difficulty | Hard |
| Language | JavaScript, Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string containing just the characters `'('` and `')'`, return *the length of the longest valid (well-formed) parentheses * *substring* .

## Constraints
- `0 <= s.length <= 3 * 10^4`
- `s[i]` is `'('`, or `')'`.

## Examples
### Example 1
- **Input:** `s = "(()"`
- **Output:** `2`
- **Explanation:** The longest valid parentheses substring is "()".

### Example 2
- **Input:** `s = ")()())"`
- **Output:** `4`
- **Explanation:** The longest valid parentheses substring is "()()".

### Example 3
- **Input:** `s = ""`
- **Output:** `0`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Valid Parentheses**, we observe the problem requirements and utilize the **Stack & Queue** technique. We decompose the problem into overlapping subproblems using a **Stack**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "(()"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The longest valid parentheses substring is "()".

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
var longestValidParentheses = function(s) {
    const n = s.length;
    const dp = Array(n).fill(0);
    let maxLength = 0;

    for (let i = 1; i < n; i++) {
        if (s[i] === ')') {
            if (s[i - 1] === '(') {
                // Pattern: ...()
                dp[i] = (i >= 2 ? dp[i - 2] : 0) + 2;
            } else if (i - dp[i - 1] - 1 >= 0 &&
                       s[i - dp[i - 1] - 1] === '(') {
                // Pattern: ...))
                const previousLength = dp[i - 1];
                const matchingOpen = i - previousLength - 1;

                dp[i] = previousLength + 2 +
                    (matchingOpen > 0 ? dp[matchingOpen - 1] : 0);
            }

            maxLength = Math.max(maxLength, dp[i]);
        }
    }

    return maxLength;
};
```

### Python
```python
class Solution:
    def longestValidParentheses(self, s):
        n = len(s)
        dp = [0] * n
        answer = 0

        for i in range(1, n):
            if s[i] == ')':

                # Case: "()"
                if s[i - 1] == '(':
                    dp[i] = 2

                    if i >= 2:
                        dp[i] += dp[i - 2]

                # Case: "))"
                elif s[i - 1] == ')':
                    j = i - dp[i - 1] - 1

                    if j >= 0 and s[j] == '(':
                        dp[i] = dp[i - 1] + 2

                        if j >= 1:
                            dp[i] += dp[j - 1]

                answer = max(answer, dp[i])

        return answer
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
- [1964. Find the Longest Valid Obstacle Course at Each Position](../../1501-2000/1964-find-the-longest-valid-obstacle-course-at-each-position/)
- [2781. Length of the Longest Valid Substring](../../2501-3000/2781-length-of-the-longest-valid-substring/)
- [20. Valid Parentheses](../../0001-0500/0020-valid-parentheses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-valid-parentheses/)
