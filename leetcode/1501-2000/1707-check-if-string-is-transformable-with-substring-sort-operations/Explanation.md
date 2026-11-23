# LeetCode 1585: Check If String Is Transformable With Substring Sort Operations

**LeetCode Problem #1585 — Check If String Is Transformable With Substring Sort Operations**
Solve LeetCode Check If String Is Transformable With Substring Sort Operations using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check If String Is Transformable With Substring Sort Operations |
| LeetCode | #1585 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two strings `s` and `t`, transform string `s` into string `t` using the following operation any number of times:

Choose a **non-empty** substring in `s` and sort it in place so the characters are in **ascending order**.

For example, applying the operation on the underlined substring in `"1 4234 "` results in `"1 2344 "`.

Return `true` if *it is possible to transform `s` into `t`*. Otherwise, return `false`.

A **substring** is a contiguous sequence of characters within a string.

## Constraints
- `s.length == t.length`
- `1 <= s.length <= 10^5`
- `s` and `t` consist of only digits.

## Examples
### Example 1
- **Input:** `s = "84532", t = "34852"`
- **Output:** `true`
- **Explanation:** You can transform s into t using the following sort operations:
"84 53 2" (from index 2 to 3) -> "84 35 2"
" 843 52" (from index 0 to 2) -> " 348 52"

### Example 2
- **Input:** `s = "34521", t = "23415"`
- **Output:** `true`
- **Explanation:** You can transform s into t using the following sort operations:
" 3452 1" -> " 2345 1"
"234 51 " -> "234 15 "

### Example 3
- **Input:** `s = "12345", t = "12435"`
- **Output:** `false`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Check If String Is Transformable With Substring Sort Operations**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "84532", t = "34852"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** You can transform s into t using the following sort operations:
"84 53 2" (from index 2 to 3) -> "84 35 2"
" 843 52" (from index 0 to 2) -> " 348 52"

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
from collections import deque

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = [deque() for _ in range(10)]
        for i, ch in enumerate(s):
            pos[int(ch)].append(i)

        for ch in t:
            d = int(ch)
            if not pos[d]:
                return False
            p = pos[d][0]
            for x in range(d):
                if pos[x] and pos[x][0] < p:
                    return False
            pos[d].popleft()

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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [3461. Check If Digits Are Equal in String After Operations I](../../3501-4000/3768-check-if-digits-are-equal-in-string-after-operations-i/)
- [3463. Check If Digits Are Equal in String After Operations II](../../3501-4000/3774-check-if-digits-are-equal-in-string-after-operations-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/)
