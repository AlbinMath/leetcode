# LeetCode 1616: Split Two Strings to Make Palindrome

**LeetCode Problem #1616 — Split Two Strings to Make Palindrome**
Solve LeetCode Split Two Strings to Make Palindrome using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split Two Strings to Make Palindrome |
| LeetCode | #1616 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `a` and `b` of the same length. Choose an index and split both strings **at the same index**, splitting `a` into two strings: `a_prefix` and `a_suffix` where `a = a_prefix + a_suffix`, and splitting `b` into two strings: `b_prefix` and `b_suffix` where `b = b_prefix + b_suffix`. Check if `a_prefix + b_suffix` or `b_prefix + a_suffix` forms a palindrome.

When you split a string `s` into `s_prefix` and `s_suffix`, either `s_suffix` or `s_prefix` is allowed to be empty. For example, if `s = "abc"`, then `"" + "abc"`, `"a" + "bc"`, `"ab" + "c"` , and `"abc" + ""` are valid splits.

Return `true`* if it is possible to form** a palindrome string, otherwise return *`false`.

**Notice** that `x + y` denotes the concatenation of strings `x` and `y`.

## Constraints
- `1 <= a.length, b.length <= 10^5`
- `a.length == b.length`
- `a` and `b` consist of lowercase English letters

## Examples
### Example 1
- **Input:** `a = "x", b = "y"`
- **Output:** `true`

### Example 2
- **Input:** `a = "xbdef", b = "xecab"`
- **Output:** `false`

### Example 3
- **Input:** `a = "ulacfd", b = "jizalu"`
- **Output:** `true`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Split Two Strings to Make Palindrome**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `a = "x", b = "y"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

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
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def is_pal(s: str, i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def check(x: str, y: str) -> bool:
            # prefix from x, suffix from y
            i, j = 0, len(x) - 1
            while i < j and x[i] == y[j]:
                i += 1
                j -= 1
            # core [i..j] must be a palindrome in x or in y
            return is_pal(x, i, j) or is_pal(y, i, j)

        return check(a, b) or check(b, a)
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
- [1347. Minimum Number of Steps to Make Two Strings Anagram](../../1001-1500/1347-minimum-number-of-steps-to-make-two-strings-anagram/)
- [2186. Minimum Number of Steps to Make Two Strings Anagram II](../../2001-2500/2186-minimum-number-of-steps-to-make-two-strings-anagram-ii/)
- [1221. Split a String in Balanced Strings](../../1001-1500/1221-split-a-string-in-balanced-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/split-two-strings-to-make-palindrome/)
