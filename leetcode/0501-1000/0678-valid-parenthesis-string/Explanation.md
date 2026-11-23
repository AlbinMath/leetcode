# LeetCode 678: Valid Parenthesis String

**LeetCode Problem #678 — Valid Parenthesis String**
Solve LeetCode Valid Parenthesis String using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Parenthesis String |
| LeetCode | #678 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return `true` *if* `s` *is **valid***.

The following rules define a **valid** string:

Any left parenthesis `'('` must have a corresponding right parenthesis `')'`. 
 Any right parenthesis `')'` must have a corresponding left parenthesis `'('`. 
 Left parenthesis `'('` must go before the corresponding right parenthesis `')'`. 
 `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string `""`.

## Constraints
- `1 <= s.length <= 100`
- `s[i]` is `'('`, `')'` or `'*'`.

## Examples
### Example 1
- **Input:** `s = "()"`
- **Output:** `true`

### Example 2
- **Input:** `s = "(*)"`
- **Output:** `true`

### Example 3
- **Input:** `s = "(*))"`
- **Output:** `true`

### Example 4
- **Input:** `s = "("`
- **Output:** `false`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Valid Parenthesis String**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "()"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

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
    def checkValidString(self, s):
        low = 0
        high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1
                high += 1

            if high < 0:
                return False

            low = max(low, 0)

        return low == 0
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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [2116. Check if a Parentheses String Can Be Valid](../../2001-2500/2221-check-if-a-parentheses-string-can-be-valid/)
- [2645. Minimum Additions to Make Valid String](../../2501-3000/2736-minimum-additions-to-make-valid-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-parenthesis-string/)
