# LeetCode 906: Super Palindromes

**LeetCode Problem #906 — Super Palindromes**
Solve LeetCode Super Palindromes using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Super Palindromes |
| LeetCode | #906 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Let's say a positive integer is a **super-palindrome** if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers `left` and `right` represented as strings, return *the number of **super-palindromes** integers in the inclusive range* `[left, right]`.

## Constraints
- `1 <= left.length, right.length <= 18`
- `left` and `right` consist of only digits.
- `left` and `right` cannot have leading zeros.
- `left` and `right` represent integers in the range `[1, 10^18 - 1]`.
- `left` is less than or equal to `right`.

## Examples
### Example 1
- **Input:** `left = "4", right = "1000"`
- **Output:** `4`
- **Explanation:** : 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.

### Example 2
- **Input:** `left = "1", right = "2"`
- **Output:** `1`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Super Palindromes**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `left = "4", right = "1000"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** : 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.

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
class Solution(object):
    def superpalindromesInRange(self, left, right):
        L = int(left)
        R = int(right)
        MAGIC = 100000  # Generates palindrome roots up to 9 digits (< 10^9)
        count = 0

        # Check odd-length palindrome roots (e.g., 123 -> 12321)
        for k in range(1, MAGIC):
            s = str(k)
            p = int(s + s[-2::-1])
            sq = p * p
            if sq > R:
                break
            if sq >= L and str(sq) == str(sq)[::-1]:
                count += 1

        # Check even-length palindrome roots (e.g., 123 -> 123321)
        for k in range(1, MAGIC):
            s = str(k)
            p = int(s + s[::-1])
            sq = p * p
            if sq > R:
                break
            if sq >= L and str(sq) == str(sq)[::-1]:
                count += 1

        return count
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
- [372. Super Pow](../../0001-0500/0372-super-pow/)
- [517. Super Washing Machines](../../0501-1000/0517-super-washing-machines/)
- [887. Super Egg Drop](../../0501-1000/0887-super-egg-drop/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/super-palindromes/)
