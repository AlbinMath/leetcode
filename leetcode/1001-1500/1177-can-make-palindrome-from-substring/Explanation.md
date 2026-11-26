# LeetCode 1177: Can Make Palindrome from Substring

**LeetCode Problem #1177 — Can Make Palindrome from Substring**
Solve LeetCode Can Make Palindrome from Substring using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Can Make Palindrome from Substring |
| LeetCode | #1177 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` and array `queries` where `queries[i] = [left_i, right_i, k_i]`. We may rearrange the substring `s[left_i...right_i]` for each query and then choose up to `k_i` of them to replace with any lowercase English letter.

If the substring is possible to be a palindrome string after the operations above, the result of the query is `true`. Otherwise, the result is `false`.

Return a boolean array `answer` where `answer[i]` is the result of the `i^th` query `queries[i]`.

Note that each letter is counted individually for replacement, so if, for example `s[left_i...right_i] = "aaa"`, and `k_i = 2`, we can only replace two of the letters. Also, note that no query modifies the initial string `s`.

## Constraints
- `1 <= s.length, queries.length <= 10^5`
- `0 <= left_i <= right_i < s.length`
- `0 <= k_i <= s.length`
- `s` consists of lowercase English letters.

## Examples
### Example 2
- **Input:** `s = "lyb", queries = [[0,1,0],[2,2,1]]`
- **Output:** `[false,true]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Can Make Palindrome from Substring**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "lyb", queries = [[0,1,0],[2,2,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[false,true]`.

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
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        p = [0] * (len(s) + 1)
        for i, ch in enumerate(s):
            p[i + 1] = p[i] ^ (1 << (ord(ch) - 97))

        return [(p[r + 1] ^ p[l]).bit_count() // 2 <= k for l, r, k in queries]
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
- [1502. Can Make Arithmetic Progression From Sequence](../../1501-2000/1502-can-make-arithmetic-progression-from-sequence/)
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1298-maximum-candies-you-can-get-from-boxes/)
- [1423. Maximum Points You Can Obtain from Cards](../../1001-1500/1423-maximum-points-you-can-obtain-from-cards/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/can-make-palindrome-from-substring/)
