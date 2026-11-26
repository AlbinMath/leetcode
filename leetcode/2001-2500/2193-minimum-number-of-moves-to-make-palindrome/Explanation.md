# LeetCode 2193: Minimum Number of Moves to Make Palindrome

**LeetCode Problem #2193 — Minimum Number of Moves to Make Palindrome**
Solve LeetCode Minimum Number of Moves to Make Palindrome using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Moves to Make Palindrome |
| LeetCode | #2193 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting only of lowercase English letters.

In one **move**, you can select any two **adjacent** characters of `s` and swap them.

Return *the **minimum number of moves** needed to make* `s` *a palindrome*.

**Note** that the input will be generated such that `s` can always be converted to a palindrome.

## Constraints
- `1 <= s.length <= 2000`
- `s` consists only of lowercase English letters.
- `s` can be converted to a palindrome using a finite number of moves.

## Examples
### Example 1
- **Input:** `s = "aabb"`
- **Output:** `2`
- **Explanation:** We can obtain two palindromes from s, "abba" and "baab". 
- We can obtain "abba" from s in 2 moves: "a

### Example 2
- **Input:** `s = "letelt"`
- **Output:** `2`
- **Explanation:** One of the palindromes we can obtain from s in 2 moves is "lettel".
One of the ways we can obtain it is "lete

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Number of Moves to Make Palindrome**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aabb"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can obtain two palindromes from s, "abba" and "baab". 
- We can obtain "abba" from s in 2 moves: "a

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minMovesToMakePalindrome = function(s) {
    const chars = s.split("");
    let left = 0;
    let right = chars.length - 1;
    let moves = 0;

    while (left < right) {
        let k = right;

        // Find a matching character for chars[left]
        while (k > left && chars[k] !== chars[left]) {
            k--;
        }

        if (k === left) {
            // No match found: this character belongs in the middle
            [chars[left], chars[left + 1]] =
                [chars[left + 1], chars[left]];

            moves++;
        } else {
            // Move the matching character to the right end
            while (k < right) {
                [chars[k], chars[k + 1]] =
                    [chars[k + 1], chars[k]];

                k++;
                moves++;
            }

            left++;
            right--;
        }
    }

    return moves;
};
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
- [1482. Minimum Number of Days to Make m Bouquets](../../1001-1500/1482-minimum-number-of-days-to-make-m-bouquets/)
- [1671. Minimum Number of Removals to Make Mountain Array](../../1501-2000/1671-minimum-number-of-removals-to-make-mountain-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/)
