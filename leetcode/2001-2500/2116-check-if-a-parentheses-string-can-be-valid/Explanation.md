# LeetCode 2116: Check if a Parentheses String Can Be Valid

**LeetCode Problem #2116 — Check if a Parentheses String Can Be Valid**
Solve LeetCode Check if a Parentheses String Can Be Valid using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if a Parentheses String Can Be Valid |
| LeetCode | #2116 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A parentheses string is a **non-empty** string consisting only of `'('` and `')'`. It is valid if **any** of the following conditions is **true**:

It is `()`. 
 It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid parentheses strings. 
 It can be written as `(A)`, where `A` is a valid parentheses string.

You are given a parentheses string `s` and a string `locked`, both of length `n`. `locked` is a binary string consisting only of `'0'`s and `'1'`s. For **each** index `i` of `locked`,

If `locked[i]` is `'1'`, you **cannot** change `s[i]`. 
 But if `locked[i]` is `'0'`, you **can** change `s[i]` to either `'('` or `')'`.

Return `true` *if you can make `s` a valid parentheses string*. Otherwise, return `false`.

## Constraints
- `n == s.length == locked.length`
- `1 <= n <= 10^5`
- `s[i]` is either `'('` or `')'`.
- `locked[i]` is either `'0'` or `'1'`.

## Examples
### Example 1
- **Input:** `s = "))()))", locked = "010100"`
- **Output:** `true`
- **Explanation:** locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.

### Example 2
- **Input:** `s = "()()", locked = "0000"`
- **Output:** `true`
- **Explanation:** We do not need to make any changes because s is already valid.

### Example 3
- **Input:** `s = ")", locked = "0"`
- **Output:** `false`
- **Explanation:** locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.

### Example 4
- **Input:** `s = "(((())(((())", locked = "111111010111"`
- **Output:** `true`
- **Explanation:** locked permits us to change s[6] and s[8]. 
We change s[6] and s[8] to ')' to make s valid.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Check if a Parentheses String Can Be Valid**, we observe the problem requirements and utilize the **Stack & Queue** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "))()))", locked = "010100"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
            
        # Pass 1: Left to Right (unlocked treated as '(')
        balance = 0
        for i in range(n):
            if locked[i] == '0' or s[i] == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
                
        # Pass 2: Right to Left (unlocked treated as ')')
        balance = 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '0' or s[i] == ')':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
                
        return True
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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2267-check-if-there-is-a-valid-parentheses-string-path/)
- [1433. Check If a String Can Break Another String](../../1001-1500/1433-check-if-a-string-can-break-another-string/)
- [1790. Check if One String Swap Can Make Strings Equal](../../1501-2000/1790-check-if-one-string-swap-can-make-strings-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/)
