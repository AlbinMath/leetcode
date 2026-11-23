# LeetCode 3754: Concatenate Non-Zero Digits and Multiply by Sum I

**LeetCode Problem #3754 — Concatenate Non-Zero Digits and Multiply by Sum I**
Solve LeetCode Concatenate Non-Zero Digits and Multiply by Sum I using Kotlin and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Concatenate Non-Zero Digits and Multiply by Sum I |
| LeetCode | #3754 |
| Difficulty | Easy |
| Language | Kotlin |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n`.

Form a new integer `x` by concatenating all the **non-zero digits** of `n` in their original order. If there are no **non-zero** digits, `x = 0`.

Let `sum` be the **sum of digits** in `x`.

Return an integer representing the value of `x * sum`.

## Constraints
- `0 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `n = 10203004`
- **Output:** `12340`
- **Explanation:** The non-zero digits are 1, 2, 3, and 4. Thus, `x = 1234`. 
 The sum of digits is `sum = 1 + 2 + 3 + 4 = 10`. 
 Therefore, the answer is `x * sum = 1234 * 10 = 12340`.

### Example 2
- **Input:** `n = 1000`
- **Output:** `1`
- **Explanation:** The non-zero digit is 1, so `x = 1` and `sum = 1`. 
 Therefore, the answer is `x * sum = 1 * 1 = 1`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Concatenate Non-Zero Digits and Multiply by Sum I**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 10203004`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12340`.
4. **Verification:** The non-zero digits are 1, 2, 3, and 4. Thus, `x = 1234`. 
 The sum of digits is `sum = 1 + 2 + 3 + 4 = 10`. 
 Therefore, the answer is `x * sum = 1234 * 10 = 12340`.

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
Kotlin

## Source Code
- [solution.kt](./solution.kt)


```kotlin
class Solution {
    fun sumAndMultiply(n: Int): Long {
        var num = n
        var x = 0L
        var sum = 0L
        var place = 1L

        while (num > 0) {
            val digit = num % 10

            if (digit != 0) {
                x += digit * place
                sum += digit
                place *= 10
            }

            num /= 10
        }

        return x * sum
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
- [3756. Concatenate Non-Zero Digits and Multiply by Sum II](../../4001-4500/4136-concatenate-non-zero-digits-and-multiply-by-sum-ii/)
- [1281. Subtract the Product and Sum of Digits of an Integer](../../1001-1500/1406-subtract-the-product-and-sum-of-digits-of-an-integer/)
- [1837. Sum of Digits in Base K](../../1501-2000/1965-sum-of-digits-in-base-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/)
