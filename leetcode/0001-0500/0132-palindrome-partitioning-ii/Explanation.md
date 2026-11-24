# LeetCode 132: Palindrome Partitioning II

**LeetCode Problem #132 — Palindrome Partitioning II**
Solve LeetCode Palindrome Partitioning II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Palindrome Partitioning II |
| LeetCode | #132 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, partition `s` such that every substring of the partition is a palindrome .

Return *the **minimum** cuts needed for a palindrome partitioning of* `s`.

## Constraints
- `1 <= s.length <= 2000`
- `s` consists of lowercase English letters only.

## Examples
### Example 1
- **Input:** `s = "aab"`
- **Output:** `1`
- **Explanation:** The palindrome partitioning ["aa","b"] could be produced using 1 cut.

### Example 2
- **Input:** `s = "a"`
- **Output:** `0`

### Example 3
- **Input:** `s = "ab"`
- **Output:** `1`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Palindrome Partitioning II**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aab"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The palindrome partitioning ["aa","b"] could be produced using 1 cut.

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
    def minCut(self, s: str) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        dp = [0] * n

        for j in range(n):
            dp[j] = j  # worst case: cut between every character
            for i in range(j + 1):
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True
                    if i == 0:
                        dp[j] = 0
                    else:
                        dp[j] = min(dp[j], dp[i - 1] + 1)

        return dp[n - 1]
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
- [131. Palindrome Partitioning](../../0001-0500/0131-palindrome-partitioning/)
- [1278. Palindrome Partitioning III](../../1001-1500/1278-palindrome-partitioning-iii/)
- [1745. Palindrome Partitioning IV](../../1501-2000/1745-palindrome-partitioning-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/palindrome-partitioning-ii/)
