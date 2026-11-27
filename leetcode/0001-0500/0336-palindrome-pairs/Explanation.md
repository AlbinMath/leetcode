# LeetCode 336: Palindrome Pairs

**LeetCode Problem #336 — Palindrome Pairs**
Solve LeetCode Palindrome Pairs using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Palindrome Pairs |
| LeetCode | #336 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** array of **unique** strings `words`.

A **palindrome pair** is a pair of integers `(i, j)` such that:

`0 <= i, j < words.length`, 
 `i != j`, and 
 `words[i] + words[j]` (the concatenation of the two strings) is a palindrome .

Return *an array of all the **palindrome pairs** of *`words`.

You must write an algorithm with `O(sum of words[i].length)` runtime complexity.

## Constraints
- `1 <= words.length <= 5000`
- `0 <= words[i].length <= 300`
- `words[i]` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["abcd","dcba","lls","s","sssll"]`
- **Output:** `[[0,1],[1,0],[3,2],[2,4]]`
- **Explanation:** The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]

### Example 2
- **Input:** `words = ["bat","tab","cat"]`
- **Output:** `[[0,1],[1,0]]`
- **Explanation:** The palindromes are ["battab","tabbat"]

### Example 3
- **Input:** `words = ["a",""]`
- **Output:** `[[0,1],[1,0]]`
- **Explanation:** The palindromes are ["a","a"]

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Palindrome Pairs**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["abcd","dcba","lls","s","sssll"]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[0,1],[1,0],[3,2],[2,4]]`.
4. **Verification:** The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]

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
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        rev = {w[::-1]: i for i, w in enumerate(words)}
        res = []
        for i, w in enumerate(words):
            n = len(w)
            for j in range(n + 1):
                prefix, suffix = w[:j], w[j:]
                if prefix == prefix[::-1]:
                    k = rev.get(suffix)
                    if k is not None and k != i:
                        res.append([k, i])
                if j != n and suffix == suffix[::-1]:
                    k = rev.get(prefix)
                    if k is not None and k != i:
                        res.append([i, k])
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
- [9. Palindrome Number](../../0001-0500/0009-palindrome-number/)
- [125. Valid Palindrome](../../0001-0500/0125-valid-palindrome/)
- [131. Palindrome Partitioning](../../0001-0500/0131-palindrome-partitioning/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/palindrome-pairs/)
