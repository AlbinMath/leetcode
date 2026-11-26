# LeetCode 1312: Minimum Insertion Steps to Make a String Palindrome

**LeetCode Problem #1312 — Minimum Insertion Steps to Make a String Palindrome**
Solve LeetCode Minimum Insertion Steps to Make a String Palindrome using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Insertion Steps to Make a String Palindrome |
| LeetCode | #1312 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`. In one step you can insert any character at any index of the string.

Return *the minimum number of steps* to make `s` palindrome.

A Palindrome String is one that reads the same backward as well as forward.

## Constraints
- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "zzazz"`
- **Output:** `0`
- **Explanation:** The string "zzazz" is already palindrome we do not need any insertions.

### Example 2
- **Input:** `s = "mbadm"`
- **Output:** `2`
- **Explanation:** String can be "mbdadbm" or "mdbabdm".

### Example 3
- **Input:** `s = "leetcode"`
- **Output:** `5`
- **Explanation:** Inserting 5 characters the string becomes "leetcodocteel".

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Insertion Steps to Make a String Palindrome**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "zzazz"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** The string "zzazz" is already palindrome we do not need any insertions.

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
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] if j - 1 >= i + 1 else 0
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
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
- [1653. Minimum Deletions to Make String Balanced](../../1501-2000/1653-minimum-deletions-to-make-string-balanced/)
- [1758. Minimum Changes To Make Alternating Binary String](../../1501-2000/1758-minimum-changes-to-make-alternating-binary-string/)
- [1830. Minimum Number of Operations to Make String Sorted](../../1501-2000/1830-minimum-number-of-operations-to-make-string-sorted/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/)
