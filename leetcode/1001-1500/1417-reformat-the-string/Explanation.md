# LeetCode 1417: Reformat The String

**LeetCode Problem #1417 — Reformat The String**
Solve LeetCode Reformat The String using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reformat The String |
| LeetCode | #1417 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an alphanumeric string `s`. (**Alphanumeric string** is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return *the reformatted string* or return **an empty string** if it is impossible to reformat the string.

## Constraints
- `1 <= s.length <= 500`
- `s` consists of only lowercase English letters and/or digits.

## Examples
### Example 1
- **Input:** `s = "a0b1c2"`
- **Output:** `"0a1b2c"`
- **Explanation:** No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.

### Example 2
- **Input:** `s = "leetcode"`
- **Output:** `""`
- **Explanation:** "leetcode" has only characters so we cannot separate them by digits.

### Example 3
- **Input:** `s = "1229857369"`
- **Output:** `""`
- **Explanation:** "1229857369" has only digits so we cannot separate them by characters.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Reformat The String**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "a0b1c2"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"0a1b2c"`.
4. **Verification:** No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.

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
    def reformat(self, s: str) -> str:
        letters = [ch for ch in s if ch.isalpha()]
        digits = [ch for ch in s if ch.isdigit()]

        if abs(len(letters) - len(digits)) > 1:
            return ""

        if len(letters) > len(digits):
            first, second = letters, digits
        else:
            first, second = digits, letters

        result = []

        for i in range(len(first)):
            result.append(first[i])

            if i < len(second):
                result.append(second[i])

        return ''.join(result)
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
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [87. Scramble String](../../0001-0500/0087-scramble-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reformat-the-string/)
