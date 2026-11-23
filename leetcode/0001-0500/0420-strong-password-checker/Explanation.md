# LeetCode 420: Strong Password Checker

**LeetCode Problem #420 — Strong Password Checker**
Solve LeetCode Strong Password Checker using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Strong Password Checker |
| LeetCode | #420 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A password is considered strong if the below conditions are all met:

It has at least `6` characters and at most `20` characters. 
 It contains at least **one lowercase** letter, at least **one uppercase** letter, and at least **one digit**. 
 It does not contain three repeating characters in a row (i.e., `"B **aaa** bb0"` is weak, but `"B** aa **b **a** 0"` is strong).

Given a string `password`, return *the minimum number of steps required to make `password` strong. if `password` is already strong, return `0`.*

In one step, you can:

Insert one character to `password`, 
 Delete one character from `password`, or 
 Replace one character of `password` with another character.

## Constraints
- `1 <= password.length <= 50`
- `password` consists of letters, digits, dot `'.'` or exclamation mark `'!'`.

## Examples
### Example 1
- **Input:** `password = "a"`
- **Output:** `5`

### Example 2
- **Input:** `password = "aA1"`
- **Output:** `3`

### Example 3
- **Input:** `password = "1337C0d3"`
- **Output:** `0`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Strong Password Checker**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `password = "a"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.

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
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        missing = 3
        if any(c.islower() for c in password): missing -= 1
        if any(c.isupper() for c in password): missing -= 1
        if any(c.isdigit() for c in password): missing -= 1

        repl = 0
        one = two = 0  # counts of runs with L%3 == 0 and L%3 == 1
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            L = j - i
            if L >= 3:
                repl += L // 3
                if L % 3 == 0:
                    one += 1
                elif L % 3 == 1:
                    two += 1
            i = j

        if n < 6:
            return max(6 - n, missing)
        if n <= 20:
            return max(missing, repl)

        over = n - 20
        left = over
        # 1 deletion per replacement saved on L%3==0 runs
        use = min(left, one)
        repl -= use
        left -= use
        # 2 deletions per replacement saved on L%3==1 runs
        use = min(left // 2, two)
        repl -= use
        left -= use * 2
        # 3 deletions per replacement saved otherwise
        repl -= left // 3
        repl = max(repl, 0)
        return over + max(missing, repl)
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
- [2932. Maximum Strong Pair XOR I](../../3001-3500/3193-maximum-strong-pair-xor-i/)
- [2935. Maximum Strong Pair XOR II](../../3001-3500/3197-maximum-strong-pair-xor-ii/)
- [1051. Height Checker](../../1001-1500/1137-height-checker/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/strong-password-checker/)
