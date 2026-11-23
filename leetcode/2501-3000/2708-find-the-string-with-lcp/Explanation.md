# LeetCode 2573: Find the String with LCP

**LeetCode Problem #2573 — Find the String with LCP**
Solve LeetCode Find the String with LCP using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the String with LCP |
| LeetCode | #2573 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
We define the `lcp` matrix of any **0-indexed** string `word` of `n` lowercase English letters as an `n x n` grid such that:

`lcp[i][j]` is equal to the length of the **longest common prefix** between the substrings `word[i,n-1]` and `word[j,n-1]`.

Given an `n x n` matrix `lcp`, return the alphabetically smallest string `word` that corresponds to `lcp`. If there is no such string, return an empty string.

A string `a` is lexicographically smaller than a string `b` (of the same length) if in the first position where `a` and `b` differ, string `a` has a letter that appears earlier in the alphabet than the corresponding letter in `b`. For example, `"aabd"` is lexicographically smaller than `"aaca"` because the first position they differ is at the third letter, and `'b'` comes before `'c'`.

## Constraints
- `1 <= n == ``lcp.length == ``lcp[i].length` `<= 1000`
- ` 0 <= lcp[i][j] <= n `

## Examples
### Example 1
- **Input:** `lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]`
- **Output:** `"abab"`
- **Explanation:** lcp corresponds to any 4 letter string with two alternating letters. The lexicographically smallest of them is "abab".

### Example 2
- **Input:** `lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]`
- **Output:** `"aaaa"`
- **Explanation:** lcp corresponds to any 4 letter string with a single distinct letter. The lexicographically smallest of them is "aaaa".

### Example 3
- **Input:** `lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]`
- **Output:** `""`
- **Explanation:** lcp[3][3] cannot be equal to 3 since word[3,...,3] consists of only a single letter; Thus, no answer exists.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find the String with LCP**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"abab"`.
4. **Verification:** lcp corresponds to any 4 letter string with two alternating letters. The lexicographically smallest of them is "abab".

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
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [''] * n
        curr_char_code = ord('a')

        # Step 1: Greedy character assignment
        for i in range(n):
            if not word[i]:
                if curr_char_code > ord('z'):
                    return ""  # Exceeded 26 lowercase English letters
                assigned_char = chr(curr_char_code)
                curr_char_code += 1
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        word[j] = assigned_char

        # Step 2: Validate the generated string against the LCP matrix
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected = 0
                if word[i] == word[j]:
                    expected = 1 + (lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0)

                if lcp[i][j] != expected:
                    return ""

        return "".join(word)
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
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [438. Find All Anagrams in a String](../../0001-0500/0438-find-all-anagrams-in-a-string/)
- [833. Find And Replace in String](../../0501-1000/0862-find-and-replace-in-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-string-with-lcp/)
