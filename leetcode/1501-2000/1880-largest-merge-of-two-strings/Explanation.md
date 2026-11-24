# LeetCode 1754: Largest Merge Of Two Strings

**LeetCode Problem #1754 — Largest Merge Of Two Strings**
Solve LeetCode Largest Merge Of Two Strings using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Merge Of Two Strings |
| LeetCode | #1754 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `word1` and `word2`. You want to construct a string `merge` in the following way: while either `word1` or `word2` are non-empty, choose **one** of the following options:

If `word1` is non-empty, append the **first** character in `word1` to `merge` and delete it from `word1`.

For example, if `word1 = "abc" `and `merge = "dv"`, then after choosing this operation, `word1 = "bc"` and `merge = "dva"`. 
 
 
 If `word2` is non-empty, append the **first** character in `word2` to `merge` and delete it from `word2`.
 
 For example, if `word2 = "abc" `and `merge = ""`, then after choosing this operation, `word2 = "bc"` and `merge = "a"`.

Return *the lexicographically **largest** *`merge`* you can construct*.

A string `a` is lexicographically larger than a string `b` (of the same length) if in the first position where `a` and `b` differ, `a` has a character strictly larger than the corresponding character in `b`. For example, `"abcd"` is lexicographically larger than `"abcc"` because the first position they differ is at the fourth character, and `d` is greater than `c`.

## Constraints
- `1 <= word1.length, word2.length <= 3000`
- `word1` and `word2` consist only of lowercase English letters.

## Examples
### Example 1
- **Input:** `word1 = "cabaa", word2 = "bcaaa"`
- **Output:** `"cbcabaaaaa"`
- **Explanation:** One way to get the lexicographically largest merge is:
- Take from word1: merge = "c", word1 = "abaa", word2 = "bcaaa"
- Take from word2: merge = "cb", word1 = "abaa", word2 = "caaa"
- Take from word2: merge = "cbc", word1 = "abaa", word2 = "aaa"
- Take from word1: merge = "cbca", word1 = "baa", word2 = "aaa"
- Take from word1: merge = "cbcab", word1 = "aa", word2 = "aaa"
- Append the remaining 5 a's from word1 and word2 at the end of merge.

### Example 2
- **Input:** `word1 = "abcabc", word2 = "abdcaba"`
- **Output:** `"abdcabcabcaba"`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Largest Merge Of Two Strings**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word1 = "cabaa", word2 = "bcaaa"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"cbcabaaaaa"`.
4. **Verification:** One way to get the lexicographically largest merge is:
- Take from word1: merge = "c", word1 = "abaa", word2 = "bcaaa"
- Take from word2: merge = "cb", word1 = "abaa", word2 = "caaa"
- Take from word2: merge = "cbc", word1 = "abaa", word2 = "aaa"
- Take from word1: merge = "cbca", word1 = "baa", word2 = "aaa"
- Take from word1: merge = "cbcab", word1 = "aa", word2 = "aaa"
- Append the remaining 5 a's from word1 and word2 at the end of merge.

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
    def largestMerge(self, word1: str, word2: str) -> str:
        i = j = 0
        m, n = len(word1), len(word2)
        res = []

        while i < m and j < n:
            if word1[i:] > word2[j:]:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1

        res.append(word1[i:])
        res.append(word2[j:])
        return ''.join(res)
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
- [583. Delete Operation for Two Strings](../../0501-1000/0583-delete-operation-for-two-strings/)
- [712. Minimum ASCII Delete Sum for Two Strings](../../0501-1000/0712-minimum-ascii-delete-sum-for-two-strings/)
- [1111. Maximum Nesting Depth of Two Valid Parentheses Strings](../../1001-1500/1208-maximum-nesting-depth-of-two-valid-parentheses-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-merge-of-two-strings/)
