# LeetCode 3955: Valid Binary Strings With Cost Limit

**LeetCode Problem #3955 — Valid Binary Strings With Cost Limit**
Solve LeetCode Valid Binary Strings With Cost Limit using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Binary Strings With Cost Limit |
| LeetCode | #3955 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integers `n` and `k`.

The **cost** of a binary string `s` is defined as the sum of all indices `i` (0-based) such that `s[i] == '1'`.

A binary string is considered **valid** if:

It does not contain two consecutive `'1'` characters. 
 Its cost is **less than or equal** to `k`.

Return a list of all valid binary strings of length `n` in any order.

## Constraints
- `1 <= n <= 12`
- `0 <= k <= n * (n - 1) / 2`

## Examples
### Example 1
- **Input:** `n = 3, k = 1`
- **Output:** `["000","010","100"]`
- **Explanation:** The binary strings of length 3 without consecutive `'1'` characters are: 

 
 `"000"` : `cost = 0` 
 "`100"` : `cost = 0` 
 `"010"` : `cost = 1` 
 `"001"` : `cost = 2` 
 `"101"` : `cost = 0 + 2 = 2` 
 

 Among these, the strings with cost less than or equal to `k = 1` are `"000"`, `"010"` and `"100"`. 

 Thus, the valid strings are `["000", "010", "100"]`.

### Example 2
- **Input:** `n = 1, k = 0`
- **Output:** `["0","1"]`
- **Explanation:** The valid binary strings of length 1 are `"0"` and `"1"`. 

 Thus the answer is `["0", "1"]`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Valid Binary Strings With Cost Limit**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, k = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["000","010","100"]`.
4. **Verification:** The binary strings of length 3 without consecutive `'1'` characters are: 

 
 `"000"` : `cost = 0` 
 "`100"` : `cost = 0` 
 `"010"` : `cost = 1` 
 `"001"` : `cost = 2` 
 `"101"` : `cost = 0 + 2 = 2` 
 

 Among these, the strings with cost less than or equal to `k = 1` are `"000"`, `"010"` and `"100"`. 

 Thus, the valid strings are `["000", "010", "100"]`.

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
from typing import List

class Solution:
    def generateValidStrings(self, n: int, k: int) -> List[str]:
        res = []
        path = []

        def dfs(i: int, cost: int, prev_one: bool) -> None:
            if i == n:
                res.append("".join(path))
                return
            path.append("0")
            dfs(i + 1, cost, False)
            path.pop()
            if not prev_one and cost + i <= k:
                path.append("1")
                dfs(i + 1, cost + i, True)
                path.pop()

        dfs(0, 0, False)
        return res
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
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [3864. Minimum Cost to Partition a Binary String](../../3501-4000/3864-minimum-cost-to-partition-a-binary-string/)
- [1111. Maximum Nesting Depth of Two Valid Parentheses Strings](../../1001-1500/1111-maximum-nesting-depth-of-two-valid-parentheses-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-binary-strings-with-cost-limit/)
