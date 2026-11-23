# LeetCode 1147: Longest Chunked Palindrome Decomposition

**LeetCode Problem #1147 — Longest Chunked Palindrome Decomposition**
Solve LeetCode Longest Chunked Palindrome Decomposition using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Chunked Palindrome Decomposition |
| LeetCode | #1147 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `text`. You should split it to k substrings `(subtext_1, subtext_2, ..., subtext_k)` such that:

`subtext_i` is a **non-empty** string. 
 The concatenation of all the substrings is equal to `text` (i.e., `subtext_1 + subtext_2 + ... + subtext_k == text`). 
 `subtext_i == subtext_k - i + 1` for all valid values of `i` (i.e., `1 <= i <= k`).

Return the largest possible value of `k`.

## Constraints
- `1 <= text.length <= 1000`
- `text` consists only of lowercase English characters.

## Examples
### Example 1
- **Input:** `text = "ghiabcdefhelloadamhelloabcdefghi"`
- **Output:** `7`
- **Explanation:** We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".

### Example 2
- **Input:** `text = "merchant"`
- **Output:** `1`
- **Explanation:** We can split the string on "(merchant)".

### Example 3
- **Input:** `text = "antaprezatepzapreanta"`
- **Output:** `11`
- **Explanation:** We can split the string on "(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)".

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Longest Chunked Palindrome Decomposition**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `text = "ghiabcdefhelloadamhelloabcdefghi"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".

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
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        res = 0
        l, r = 0, n          # current middle is text[l:r]
        while l < r:
            found = False
            for length in range(1, (r - l) // 2 + 1):
                if text[l:l + length] == text[r - length:r]:
                    res += 2
                    l += length
                    r -= length
                    found = True
                    break
            if not found:
                res += 1     # the whole middle is one chunk
                break
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
- [409. Longest Palindrome](../../0001-0500/0409-longest-palindrome/)
- [2131. Longest Palindrome by Concatenating Two Letter Words](../../2001-2500/2237-longest-palindrome-by-concatenating-two-letter-words/)
- [3503. Longest Palindrome After Substring Concatenation I](../../3501-4000/3793-longest-palindrome-after-substring-concatenation-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/)
