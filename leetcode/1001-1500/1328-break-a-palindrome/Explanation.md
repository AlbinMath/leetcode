# LeetCode 1328: Break a Palindrome

**LeetCode Problem #1328 — Break a Palindrome**
Solve LeetCode Break a Palindrome using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Break a Palindrome |
| LeetCode | #1328 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a palindromic string of lowercase English letters `palindrome`, replace **exactly one** character with any lowercase English letter so that the resulting string is **not** a palindrome and that it is the **lexicographically smallest** one possible.

Return *the resulting string. If there is no way to replace a character to make it not a palindrome, return an **empty string**.*

A string `a` is lexicographically smaller than a string `b` (of the same length) if in the first position where `a` and `b` differ, `a` has a character strictly smaller than the corresponding character in `b`. For example, `"abcc"` is lexicographically smaller than `"abcd"` because the first position they differ is at the fourth character, and `'c'` is smaller than `'d'`.

## Constraints
- `1 <= palindrome.length <= 1000`
- `palindrome` consists of only lowercase English letters.

## Examples
### Example 1
- **Input:** `palindrome = "abccba"`
- **Output:** `"aaccba"`
- **Explanation:** There are many ways to make "abccba" not a palindrome, such as " z bccba", "a a ccba", and "ab a cba".
Of all the ways, "aaccba" is the lexicographically smallest.

### Example 2
- **Input:** `palindrome = "a"`
- **Output:** `""`
- **Explanation:** There is no way to replace a single character to make "a" not a palindrome, so return an empty string.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Break a Palindrome**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `palindrome = "abccba"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"aaccba"`.
4. **Verification:** There are many ways to make "abccba" not a palindrome, such as " z bccba", "a a ccba", and "ab a cba".
Of all the ways, "aaccba" is the lexicographically smallest.

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
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""

        for i in range(n // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]

        return palindrome[:-1] + 'b'
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
[View problem on LeetCode](https://leetcode.com/problems/break-a-palindrome/)
