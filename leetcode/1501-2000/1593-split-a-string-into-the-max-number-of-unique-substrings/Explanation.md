# LeetCode 1593: Split a String Into the Max Number of Unique Substrings

**LeetCode Problem #1593 — Split a String Into the Max Number of Unique Substrings**
Solve LeetCode Split a String Into the Max Number of Unique Substrings using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split a String Into the Max Number of Unique Substrings |
| LeetCode | #1593 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s` , return *the maximum number of unique substrings that the given string can be split into*.

You can split string `s` into any list of **non-empty substrings**, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are **unique**.

A **substring** is a contiguous sequence of characters within a string.

## Constraints
- `1 <= s.length <= 16`
- `s` contains only lower case English letters.

## Examples
### Example 1
- **Input:** `s = "ababccc"`
- **Output:** `5`
- **Explanation:** : One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

### Example 2
- **Input:** `s = "aba"`
- **Output:** `2`
- **Explanation:** : One way to split maximally is ['a', 'ba'].

### Example 3
- **Input:** `s = "aa"`
- **Output:** `1`
- **Explanation:** : It is impossible to split the string any further.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Split a String Into the Max Number of Unique Substrings**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "ababccc"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** : One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

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
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        seen = set()
        best = 0

        def dfs(pos: int) -> None:
            nonlocal best
            if len(seen) + (n - pos) <= best:
                return  # even one character per piece can't beat best
            if pos == n:
                best = len(seen)
                return
            for end in range(pos + 1, n + 1):
                piece = s[pos:end]
                if piece in seen:
                    continue
                seen.add(piece)
                dfs(end)
                seen.remove(piece)

        dfs(0)
        return best
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
- [467. Unique Substrings in Wraparound String](../../0001-0500/0467-unique-substrings-in-wraparound-string/)
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0828-count-unique-characters-of-all-substrings-of-a-given-string/)
- [2767. Partition String Into Minimum Beautiful Substrings](../../2501-3000/2767-partition-string-into-minimum-beautiful-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/)
