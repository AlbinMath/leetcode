# LeetCode 131: Palindrome Partitioning

**LeetCode Problem #131 — Palindrome Partitioning**
Solve LeetCode Palindrome Partitioning using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Palindrome Partitioning |
| LeetCode | #131 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, partition `s` such that every substring of the partition is a **palindrome** . Return *all possible palindrome partitioning of *`s`.

## Constraints
- `1 <= s.length <= 16`
- `s` contains only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "aab"`
- **Output:** `[["a","a","b"],["aa","b"]]`

### Example 2
- **Input:** `s = "a"`
- **Output:** `[["a"]]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Palindrome Partitioning**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

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
3. **Result:** Arrive at the expected output `[["a","a","b"],["aa","b"]]`.

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
    def partition(self, s):
        res = []
        def dfs(i, path):
            if i == len(s):
                res.append(path[:])
                return
            for j in range(i, len(s)):
                t = s[i:j+1]
                if t == t[::-1]:
                    dfs(j+1, path+[t])
        dfs(0, [])
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
- [132. Palindrome Partitioning II](../../0001-0500/0132-palindrome-partitioning-ii/)
- [1278. Palindrome Partitioning III](../../1001-1500/1403-palindrome-partitioning-iii/)
- [1745. Palindrome Partitioning IV](../../1501-2000/1871-palindrome-partitioning-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/palindrome-partitioning/)
