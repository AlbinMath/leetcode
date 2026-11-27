# LeetCode 2002: Maximum Product of the Length of Two Palindromic Subsequences

**LeetCode Problem #2002 — Maximum Product of the Length of Two Palindromic Subsequences**
Solve LeetCode Maximum Product of the Length of Two Palindromic Subsequences using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product of the Length of Two Palindromic Subsequences |
| LeetCode | #2002 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, find two **disjoint palindromic subsequences** of `s` such that the **product** of their lengths is **maximized**. The two subsequences are **disjoint** if they do not both pick a character at the same index.

Return *the **maximum** possible **product** of the lengths of the two palindromic subsequences*.

A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is **palindromic** if it reads the same forward and backward.

## Constraints
- `2 <= s.length <= 12`
- `s` consists of lowercase English letters only.

## Examples
### Example 1
- **Input:** `s = "leetcodecom"`
- **Output:** `9`
- **Explanation:** : An optimal solution is to choose "ete" for the 1^st subsequence and "cdc" for the 2^nd subsequence.
The product of their lengths is: 3 * 3 = 9.

### Example 2
- **Input:** `s = "bb"`
- **Output:** `1`
- **Explanation:** : An optimal solution is to choose "b" (the first character) for the 1^st subsequence and "b" (the second character) for the 2^nd subsequence.
The product of their lengths is: 1 * 1 = 1.

### Example 3
- **Input:** `s = "accbcaxxcxx"`
- **Output:** `25`
- **Explanation:** : An optimal solution is to choose "accca" for the 1^st subsequence and "xxcxx" for the 2^nd subsequence.
The product of their lengths is: 5 * 5 = 25.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Product of the Length of Two Palindromic Subsequences**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "leetcodecom"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** : An optimal solution is to choose "ete" for the 1^st subsequence and "cdc" for the 2^nd subsequence.
The product of their lengths is: 3 * 3 = 9.

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
/**
 * @param {string} s
 * @return {number}
 */
var maxProduct = function(s) {
    const n = s.length;
    const totalMasks = 1 << n;
    const palindromeLength = new Array(totalMasks).fill(0);

    // Calculate the length of each palindromic subsequence.
    for (let mask = 1; mask < totalMasks; mask++) {
        let left = 0;
        let right = n - 1;
        let length = 0;
        let isPalindrome = true;

        while (left <= right) {
            while (left < n && !(mask & (1 << left))) {
                left++;
            }

            while (right >= 0 && !(mask & (1 << right))) {
                right--;
            }

            if (left > right) break;

            if (s[left] !== s[right]) {
                isPalindrome = false;
                break;
            }

            if (left === right) {
                length++;
            } else {
                length += 2;
            }

            left++;
            right--;
        }

        if (isPalindrome) {
            palindromeLength[mask] = length;
        }
    }

    let answer = 0;

    // Try every pair of disjoint subsequences.
    for (let mask1 = 1; mask1 < totalMasks; mask1++) {
        if (palindromeLength[mask1] === 0) continue;

        for (let mask2 = mask1 + 1; mask2 < totalMasks; mask2++) {
            // The masks must not share any selected index.
            if ((mask1 & mask2) !== 0) continue;
            if (palindromeLength[mask2] === 0) continue;

            answer = Math.max(
                answer,
                palindromeLength[mask1] * palindromeLength[mask2]
            );
        }
    }

    return answer;
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
- [1960. Maximum Product of the Length of Two Palindromic Substrings](../../1501-2000/1960-maximum-product-of-the-length-of-two-palindromic-substrings/)
- [1464. Maximum Product of Two Elements in an Array](../../1001-1500/1464-maximum-product-of-two-elements-in-an-array/)
- [1913. Maximum Product Difference Between Two Pairs](../../1501-2000/1913-maximum-product-difference-between-two-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/)
