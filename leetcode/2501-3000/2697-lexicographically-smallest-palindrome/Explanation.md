# LeetCode 2697: Lexicographically Smallest Palindrome

**LeetCode Problem #2697 — Lexicographically Smallest Palindrome**
Solve LeetCode Lexicographically Smallest Palindrome using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Smallest Palindrome |
| LeetCode | #2697 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string s consisting of **lowercase English letters**, and you are allowed to perform operations on it. In one operation, you can **replace** a character in s with another lowercase English letter.

Your task is to make s a **palindrome** with the **minimum** **number** **of operations** possible. If there are **multiple palindromes** that can be made using the **minimum** number of operations, make the **lexicographically smallest** one.

A string `a` is lexicographically smaller than a string `b` (of the same length) if in the first position where `a` and `b` differ, string `a` has a letter that appears earlier in the alphabet than the corresponding letter in `b`.

Return *the resulting palindrome string.*

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of only lowercase English letters .

## Examples
### Example 1
- **Input:** `s = "egcfe"`
- **Output:** `"efcfe"`
- **Explanation:** The minimum number of operations to make "egcfe" a palindrome is 1, and the lexicographically smallest palindrome string we can get by modifying one character is "efcfe", by changing 'g'.

### Example 2
- **Input:** `s = "abcd"`
- **Output:** `"abba"`
- **Explanation:** The minimum number of operations to make "abcd" a palindrome is 2, and the lexicographically smallest palindrome string we can get by modifying two characters is "abba".

### Example 3
- **Input:** `s = "seven"`
- **Output:** `"neven"`
- **Explanation:** The minimum number of operations to make "seven" a palindrome is 1, and the lexicographically smallest palindrome string we can get by modifying one character is "neven".

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Lexicographically Smallest Palindrome**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "egcfe"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"efcfe"`.
4. **Verification:** The minimum number of operations to make "egcfe" a palindrome is 1, and the lexicographically smallest palindrome string we can get by modifying one character is "efcfe", by changing 'g'.

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
    def makeSmallestPalindrome(self, s: str) -> str:
        a = list(s)
        i, j = 0, len(a) - 1
        while i < j:
            if a[i] != a[j]:
                m = min(a[i], a[j])
                a[i] = a[j] = m
            i += 1
            j -= 1
        return ''.join(a)
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
- [1061. Lexicographically Smallest Equivalent String](../../1001-1500/1061-lexicographically-smallest-equivalent-string/)
- [1625. Lexicographically Smallest String After Applying Operations](../../1501-2000/1625-lexicographically-smallest-string-after-applying-operations/)
- [2434. Using a Robot to Print the Lexicographically Smallest String](../../2001-2500/2434-using-a-robot-to-print-the-lexicographically-smallest-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-smallest-palindrome/)
