# LeetCode 1541: Minimum Insertions to Balance a Parentheses String

**LeetCode Problem #1541 — Minimum Insertions to Balance a Parentheses String**
Solve LeetCode Minimum Insertions to Balance a Parentheses String using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Insertions to Balance a Parentheses String |
| LeetCode | #1541 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a parentheses string `s` containing only the characters `'('` and `')'`. A parentheses string is **balanced** if:

Any left parenthesis `'('` must have a corresponding two consecutive right parenthesis `'))'`. 
 Left parenthesis `'('` must go before the corresponding two consecutive right parenthesis `'))'`.

In other words, we treat `'('` as an opening parenthesis and `'))'` as a closing parenthesis.

For example, `"())"`, `"())(())))"` and `"(())())))"` are balanced, `")()"`, `"()))"` and `"(()))"` are not balanced.

You can insert the characters `'('` and `')'` at any position of the string to balance it if needed.

Return *the minimum number of insertions* needed to make `s` balanced.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of `'('` and `')'` only.

## Examples
### Example 1
- **Input:** `s = "(()))"`
- **Output:** `1`
- **Explanation:** The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.

### Example 2
- **Input:** `s = "())"`
- **Output:** `0`
- **Explanation:** The string is already balanced.

### Example 3
- **Input:** `s = "))())("`
- **Output:** `3`
- **Explanation:** Add '(' to match the first '))', Add '))' to match the last '('.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Insertions to Balance a Parentheses String**, we observe the problem requirements and utilize the **Stack & Queue** technique. We iterate through the inputs using **Stack Push / Pop Parsing**, leveraging a **Stack** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Stack**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "(()))"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.

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
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_count = 0

        i = 0
        while i < len(s):
            if s[i] == '(':
                open_count += 1
            else:
                # A closing pair must be '))'
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    # Insert one ')' to complete the pair
                    insertions += 1

                if open_count > 0:
                    open_count -= 1
                else:
                    # Insert '(' to match this closing pair
                    insertions += 1

            i += 1

        # Every remaining '(' needs two ')'
        insertions += open_count * 2

        return insertions
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
- [921. Minimum Add to Make Parentheses Valid](../../0501-1000/0921-minimum-add-to-make-parentheses-valid/)
- [1249. Minimum Remove to Make Valid Parentheses](../../1001-1500/1249-minimum-remove-to-make-valid-parentheses/)
- [1312. Minimum Insertion Steps to Make a String Palindrome](../../1001-1500/1312-minimum-insertion-steps-to-make-a-string-palindrome/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/)
