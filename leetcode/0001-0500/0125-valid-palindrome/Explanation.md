# LeetCode 125: Valid Palindrome

**LeetCode Problem #125 — Valid Palindrome**
Solve LeetCode Valid Palindrome using PHP and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Palindrome |
| LeetCode | #125 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true`* if it is a **palindrome**, or *`false`* otherwise*.

## Constraints
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Examples
### Example 1
- **Input:** `s = "A man, a plan, a canal: Panama"`
- **Output:** `true`
- **Explanation:** "amanaplanacanalpanama" is a palindrome.

### Example 2
- **Input:** `s = "race a car"`
- **Output:** `false`
- **Explanation:** "raceacar" is not a palindrome.

### Example 3
- **Input:** `s = " "`
- **Output:** `true`
- **Explanation:** s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Valid Palindrome**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "A man, a plan, a canal: Panama"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** "amanaplanacanalpanama" is a palindrome.

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
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {
    function isPalindrome($s) {
        $left = 0;
        $right = strlen($s) - 1;

        while ($left < $right) {

            // Skip non-alphanumeric characters from left
            while ($left < $right && !ctype_alnum($s[$left])) {
                $left++;
            }

            // Skip non-alphanumeric characters from right
            while ($left < $right && !ctype_alnum($s[$right])) {
                $right--;
            }

            // Compare characters ignoring case
            if (strtolower($s[$left]) !== strtolower($s[$right])) {
                return false;
            }

            $left++;
            $right--;
        }

        return true;
    }
}
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
- [680. Valid Palindrome II](../../0501-1000/0680-valid-palindrome-ii/)
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [9. Palindrome Number](../../0001-0500/0009-palindrome-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-palindrome/)
